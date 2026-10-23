import random
import numpy as np
import json
import os
from SynergyManager import SynergyManager
from collections import deque
import uuid
from CombatProfileManager import CombatProfileManager, UnitRole
from enum import IntEnum
import numpy as np
from numba import njit
import math  # 🧹 para math.tanh

class Strategy(IntEnum):

    # =========================================================
    # 💰 ECONOMIA
    # Guarda gold, joga safe
    # =========================================================
    ECON = 0

    # =========================================================
    # 🛡️ ESTABILIZAÇÃO
    # Roll moderado pra fortalecer board
    # =========================================================
    STABILIZE = 1

    # =========================================================
    # 🚀 FAST 8
    # Sobe level rápido
    # =========================================================
    FAST8 = 2

    # =========================================================
    # 🎲 SLOW ROLL
    # Fica em level alvo procurando 3*
    # =========================================================
    SLOWROLL = 3

    # =========================================================
    # 🔥 ALL IN
    # Gasta tudo pra sobreviver
    # =========================================================
    ALL_IN = 4

    # =========================================================
    # 📈 WIN STREAK
    # Mantém força máxima pra streakar
    # =========================================================
    WINSTREAK = 5

    # =========================================================
    # 🩸 LOSS STREAK
    # Aceita perder pra ganhar economia
    # =========================================================
    LOSS_STREAK = 6

class ActionType(IntEnum):
    BUY = 0
    REROLL = 1
    BUY_XP = 2
    MOVE_BENCH = 3
    MOVE_BOARD = 4
    SELL = 5
    PASS = 6

@njit
def _combat_simulation_numba(
    ally_hp, ally_dps, ally_interval, ally_range, ally_row, ally_col, ally_role, ally_armor,
    enemy_hp, enemy_dps, enemy_interval, enemy_range, enemy_row, enemy_col, enemy_role, enemy_armor,
    max_time, dt
):
    n_allies = len(ally_hp)
    n_enemies = len(enemy_hp)

    # Estados de vida
    ally_alive = np.ones(n_allies, dtype=np.bool_)
    enemy_alive = np.ones(n_enemies, dtype=np.bool_)

    # Próximo ataque
    ally_next = np.zeros(n_allies, dtype=np.float32)
    enemy_next = np.zeros(n_enemies, dtype=np.float32)

    # Cópias dos arrays de HP (serão modificados)
    ally_hp_cur = ally_hp.copy()
    enemy_hp_cur = enemy_hp.copy()

    tick = 0.0
    while tick < max_time:
        # --- Aliados atacam ---
        for i in range(n_allies):
            if not ally_alive[i]:
                continue
            if tick < ally_next[i]:
                continue

            # Seleciona alvo (inimigo)
            best_j = -1
            best_dist = 999999
            # Se for assassino (role 4), prioriza carries
            if ally_role[i] == 4:  # ASSASSIN
                # Primeiro procura entre inimigos vivos que sejam CARRY (role 1)
                for j in range(n_enemies):
                    if not enemy_alive[j]:
                        continue
                    if enemy_role[j] == 1:  # CARRY
                        dist = abs(ally_row[i] - enemy_row[j]) + abs(ally_col[i] - enemy_col[j])
                        if dist < best_dist:
                            best_dist = dist
                            best_j = j
                # Se não achou carry, escolhe qualquer inimigo (já vai ser feito abaixo)
            if best_j == -1:
                # Seleção padrão: alvo mais próximo (distância Manhattan)
                best_dist = 999999
                for j in range(n_enemies):
                    if not enemy_alive[j]:
                        continue
                    dist = abs(ally_row[i] - enemy_row[j]) + abs(ally_col[i] - enemy_col[j])
                    # Se atirador de longo alcance (range >= 3), pode dar prioridade a frontline? não implementado aqui.
                    if dist < best_dist:
                        best_dist = dist
                        best_j = j

            if best_j == -1:
                continue

            # Calcula dano
            damage = max(5.0, ally_dps[i] * 0.55)
            # Armadura do alvo
            armor = enemy_armor[best_j]
            reduction = 100.0 / (100.0 + armor)
            final_damage = damage * reduction
            enemy_hp_cur[best_j] -= final_damage
            if enemy_hp_cur[best_j] <= 0:
                enemy_alive[best_j] = False
            ally_next[i] = tick + ally_interval[i]

        # --- Inimigos atacam ---
        for j in range(n_enemies):
            if not enemy_alive[j]:
                continue
            if tick < enemy_next[j]:
                continue

            # Inimigo ataca o aliado mais próximo
            best_i = -1
            best_dist = 999999
            for i in range(n_allies):
                if not ally_alive[i]:
                    continue
                dist = abs(enemy_row[j] - ally_row[i]) + abs(enemy_col[j] - ally_col[i])
                if dist < best_dist:
                    best_dist = dist
                    best_i = i
            if best_i == -1:
                continue

            damage = max(5.0, enemy_dps[j] * 0.55)
            armor = ally_armor[best_i]
            reduction = 100.0 / (100.0 + armor)
            final_damage = damage * reduction
            ally_hp_cur[best_i] -= final_damage
            if ally_hp_cur[best_i] <= 0:
                ally_alive[best_i] = False
            enemy_next[j] = tick + enemy_interval[j]

        tick += dt

    return ally_alive, enemy_alive, ally_hp_cur, enemy_hp_cur

@njit
def _positioning_score_numba(role_matrix, rows, cols):
    score = 0.0
    carry_positions = []
    for r in range(rows):
        for c in range(cols):
            if role_matrix[r, c] == 2:
                carry_positions.append((r, c))
    for r in range(rows):
        for c in range(cols):
            role = role_matrix[r, c]
            if role == 0:
                continue
            neighbors = 0
            tanks_adjacent = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        nrole = role_matrix[nr, nc]
                        if nrole != 0:
                            neighbors += 1
                            if nrole == 1:
                                tanks_adjacent += 1
            if role == 1:  # tank
                if r <= 1:
                    score += 1.2   # aumentado de 1.0
                else:
                    score -= 2.0   # aumentado de -1.5
                if tanks_adjacent >= 1:
                    score += 0.4
            elif role == 2:  # carry
                if r >= 2:
                    score += 1.8   # aumentado de 1.2
                else:
                    score -= 3.5   # drasticamente penalizado
                score += tanks_adjacent * 0.8
                if c in (0, cols - 1):
                    score += 0.5   # canto é bom para carry
                if neighbors <= 1:
                    score += 0.5
                if neighbors >= 4:
                    score -= 0.8
            elif role == 3:  # assassin
                # Assassino NÃO deve estar na frontline
                if r <= 1:
                    score -= 2.0   # penalidade alta
                # Assassino gosta de laterais
                if c in (0, cols - 1):
                    score += 0.7
                if r >= 2:
                    score += 0.5
            elif role == 4:  # fighter
                if r <= 1:
                    score += 0.3
                else:
                    score -= 0.2
    # Bônus de proteção para carries
    for (r, c) in carry_positions:
        protected = False
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and role_matrix[nr, nc] == 1 and nr < r:
                    protected = True
                    break
            if protected:
                break
        if protected:
            score += 1.5   # aumentado de 1.2
        else:
            score -= 1.5   # aumentado de -1.0
    return math.tanh(score * 0.07)  # mantém sensibilidade

class MiniTFTEnv:
    def __init__(
        self,
        units_path="C:/Users/Victor/Desktop/Ideia louca/FRAMEWORK/units.json",
        traits_path="C:/Users/Victor/Desktop/Ideia louca/FRAMEWORK/traits.json",
    ):
        self.max_rounds = 45
        self.rows, self.cols = 4, 7
        self.max_bench = 9

        self.combat_profile_mgr = CombatProfileManager()
        self.champions = self._load_champions(units_path)
        self.synergy_mgr = SynergyManager(traits_path)
   
        # --- Progressão e Probabilidades ---
        self.xp_to_next = {1: 2, 2: 2, 3: 6, 4: 12, 5: 20, 6: 32, 7: 50, 8: 80, 9: 999}
        self.shop_odds = {
            1: [1, 0, 0, 0, 0],
            2: [1, 0, 0, 0, 0],
            3: [0.75, 0.25, 0, 0, 0],
            4: [0.55, 0.30, 0.15, 0, 0],
            5: [0.45, 0.33, 0.20, 0.02, 0],
            6: [0.25, 0.40, 0.30, 0.05, 0],
            7: [0.19, 0.30, 0.35, 0.15, 0.01],
            8: [0.16, 0.20, 0.35, 0.25, 0.04],
            9: [0.09, 0.15, 0.30, 0.30, 0.16],
        }

        self.stage_damage_map = {
            1: 0,
            2: 1,
            3: 2,
            4: 4,
            5: 6,
            6: 9,
            7: 14
        }
        self.enemy_stage_power = {
            2: 8,
            3: 12,
            4: 18,
            5: 28,
            6: 42,
            7: 60
        }

        # ===== TRACKING =====
        self.action_count_this_round = 0
        self.max_actions_per_round = 20
        self.units_bought_this_round = []
        self.bench_stay_duration = [0] * self.max_bench
        self._cache_valid = False
        self._cached_board_power = 0.0

        # ===== NOVO (PRO PLAYER) =====
        self.comp_direction = {}
        self.comp_strength = 0.0
        self.last_purchased_id = None
        self.useless_move_count = 0
        self.comp_traits = {}
        self.comp_locked = False
        self.xp_bought_this_round = 0
        self.comp_focus = {}
        self.reroll_count_this_round = 0
        self.turn_spend_count = 0
        self.turn_gold_spent = 0
        self.unit_counts = {}
        
        # ===== ANTI LOOP =====
        self.move_count = 0
        self.useless_move_count = 0
        self.unit_move_cooldown = {}
        self.turn = 0
        self.previous_position_signatures  = set()
        self._last_bench_swap = None
        self._last_board_swap = None
        self._last_move_key = None
        self._last_move_key_bench = None
        self._combat_sim_cache = {}
        self._unit_last_move = {}        # (unit_uuid, board_pos) -> turn
        self._last_bench_action = None   # (bench_slot, board_pos, turn)
        self._last_board_action = None   # (from_pos, to_pos, turn)
        self._stabilize_start_round = 0
        self._last_bench_move_key = set()   # (unit_uuid, bench_slot, board_pos)
        self._bench_board_pos_cooldown = {}   # board_pos -> turn do último movimento bem-sucedido

        # ===== STRATEGY =====
        self.strategy = Strategy.ECON
        self.upgraded_units = set()
        self.last_bought_unit = None
        self.strategy_lock = 0
        self.strategy_switch_count = 0
        self.last_strategy = None
        self.last_purchased_uuid = None
        self.last_sold_uuid = None
        self.purchase_sell_block = 0
        self.econ_streak = 0
        self.slowroll_no_upgrade_counter = 0

        # ===== CACHES DE DESEMPENHO (NOVOS) =====
        self._impact_cache = {}
        self._comp_cache = {}
        self._sim_cache = {}
        self._unit_set_version = 0
        self._last_unit_set_hash = None
        self._last_board_synergy_hash = None
        self._expected_power_cache = {}
        self._avg_power_cache = {}
        self._last_board_power = 0
        self._last_high_cost_count = 0   # FIX: para reward delta de unidades caras

        # 🧹 OTIMIZAÇÕES ADICIONAIS
        self._all_units_cache = []          # cache de todas as unidades
        self._pair_count = 0                # contador incremental de pares
        self._steps_since_comp_update = 0   # para reduzir frequência de _update_comp_direction
        self.role_matrix = np.zeros((self.rows, self.cols), dtype=np.int8)  # matriz de papéis para Numba

        self._trait_embedding_dim = 8
        self._trait_synergy_matrix = {}  # (trait_a, trait_b) -> score
        self._trait_to_idx = {}  # mapeamento nome -> índice
        self._trait_embeddings = None  # será usado na política

        self._build_trait_index()          # mapeia nome da trait -> índice
        self._last_combat_won = False
        self._last_syn_count = 0

        self.reset()

    # =========================================================
    # 🔥 CACHE SYSTEM
    # =========================================================
    def _invalidate_cache(self):
        self._cache_valid = False
        self._combat_sim_cache.clear()

    def _invalidate_unit_caches(self):
        """Chame sempre que o conjunto de unidades (bench+board) for modificado."""
        self._impact_cache.clear()
        self._comp_cache.clear()
        self._sim_cache.clear()
        self._unit_set_version += 1
        self._avg_power_cache.clear()
        self._expected_power_cache.clear()
        self._cache_valid = False
        # 🧹 invalidar cache de todas as unidades
        self._all_units_cache = []
        # 🧹 recalcular pair_count e role_matrix
        self._rebuild_pair_count()
        self._rebuild_role_matrix()
        self._combat_sim_cache.clear()

    def _update_synergy_if_needed(self):
        """Só atualiza sinergias se o tabuleiro mudou desde a última vez."""
        current_hash = self._get_board_hash()
        if current_hash != self._last_board_synergy_hash:
            self.synergy_mgr.update(self.board)
            self._last_board_synergy_hash = current_hash

    def sanitize_action(self, action):

        # =====================================================
        # 🎯 ARRAY -> STRUCTURED ACTION
        # =====================================================

        if isinstance(action, np.ndarray):

            action = action.tolist()

        if isinstance(action, (list, tuple)):

            return {

                "type": int(action[0]),

                "shop_slot": int(action[1]),

                "bench_slot": int(action[2]),

                "board_target": int(action[3]),

                "board_source": int(action[4]),

                "board_move_target": int(action[5]),
            }

        # =====================================================
        # 🧠 ALREADY DICT
        # =====================================================

        return {

            "type": int(action.get("type", 0)),

            "shop_slot": int(
                action.get("shop_slot", 0)
            ),

            "bench_slot": int(
                action.get("bench_slot", 0)
            ),

            "board_target": int(
                action.get("board_target", 0)
            ),

            "board_source": int(
                action.get("board_source", 0)
            ),

            "board_move_target": int(
                action.get("board_move_target", 0)
            ),
        }
    
    # =========================================================
    # STEP (CORE)
    # =========================================================
    def step(self, action):

        reward = 0.0

        done = False

        info = {"round_end": False}

        # =====================================================
        # 🧠 SANITIZE ACTION
        # =====================================================

        action = self.sanitize_action(action)

        action_type = action["type"]

        self.action_count_this_round += 1

        self.turn += 1

        # =====================================================
        # 🧠 STRATEGY UPDATE
        # =====================================================

        self._update_strategy()

        # 🧹 OTIMIZAÇÃO: _update_comp_direction agora executa a cada 2 steps
        self._update_comp_direction()

        self._update_comp_focus()

        if self._should_lock_comp():

            self.comp_locked = True

        # =====================================================
        # ⭐ PREV STARS
        # =====================================================

        self.prev_total_stars = sum(

            u["star"]

            for r in self.board

            for u in r

            if u
        )

        # =====================================================
        # 🛒 BUY
        # =====================================================

        if action_type == ActionType.BUY:

            shop_slot = action["shop_slot"]

            # ================================================
            # VALIDATE
            # ================================================

            if shop_slot < 0 or shop_slot >= 5:

                return (
                    self._get_state(),
                    -0.5,
                    False,
                    info
                )

            unit = self.shop[shop_slot]

            if not self._is_valid_unit(unit):

                return (
                    self._get_state(),
                    -0.5,
                    False,
                    info
                )

            # ================================================
            # BUY
            # ================================================

            reward += self._compra_unidade(
                shop_slot
            )

            # ================================================
            # COMP CHECK
            # ================================================

            if (

                self.comp_locked

                and not self._should_buy_unit(unit)
            ):

                reward -= 1.0

        # =====================================================
        # 🔄 REROLL
        # =====================================================

        elif action_type == ActionType.REROLL:

            reward += self._reroll()

        # =====================================================
        # ⬆️ BUY XP
        # =====================================================

        elif action_type == ActionType.BUY_XP:

            reward += self._buy_xp()

        # =====================================================
        # 🔄 MOVE BENCH -> BOARD
        # =====================================================

        elif action_type == ActionType.MOVE_BENCH:

            bench_slot = action["bench_slot"]

            board_target = action["board_target"]

            # ================================================
            # PRE SYNERGY
            # ================================================

            before_syn = {

                t: self.synergy_mgr.get_trait_level(t, c)

                for t, c in (
                    self.synergy_mgr.active_traits.items()
                )
            }

            # ================================================
            # MOVE
            # ================================================

            reward += self._move_bench_to_board(

                bench_slot,

                board_target
            )

            # ================================================
            # UPDATE SYNERGY
            # ================================================

            self._update_synergy_if_needed()

            # ================================================
            # POSITIONING
            # ================================================

            positioning_score = self._evaluate_board_positioning()

            reward += positioning_score

            # ================================================
            # POST SYNERGY
            # ================================================

            after_syn = {

                t: self.synergy_mgr.get_trait_level(t, c)

                for t, c in (
                    self.synergy_mgr.active_traits.items()
                )
            }

            for trait in after_syn:

                before = before_syn.get(
                    trait,
                    0
                )

                after = after_syn.get(
                    trait,
                    0
                )

                # ============================================
                # SYNERGY GAIN
                # ============================================

                if after > before:

                    reward += (
                        after - before
                    ) * 0.3

                # ============================================
                # SYNERGY LOSS
                # ============================================

                elif after < before:

                    reward -= (
                        before - after
                    ) * 0.3

            # ================================================
            # BEST SWAP BONUS
            # ================================================

            best_swap = self._find_best_swap()

            if best_swap:

                best_action = self._best_swap_to_action(
                    best_swap
                )

                current_action = (

                    bench_slot,
                    board_target
                )

                if current_action == best_action:

                    reward += 0.05

            # ================================================
            # MOVE SPAM PENALTY
            # ================================================

            if self.move_count >= 4:

                reward -= (
                    self.move_count * 0.05
                )

        # =====================================================
        # 🔄 MOVE BOARD -> BOARD
        # =====================================================

        elif action_type == ActionType.MOVE_BOARD:

            from_pos = action["board_source"]

            to_pos = action["board_move_target"]

            reward += self._move_board_unit(

                from_pos,

                to_pos
            )

        # =====================================================
        # 💸 SELL
        # =====================================================

        elif action_type == ActionType.SELL:

            reward += self._vender_unidade(

                action["bench_slot"]
            )

        # =====================================================
        # ⏭ PASS
        # =====================================================

        elif action_type == ActionType.PASS:

            reward += self._resolve_round(info)
            # FIX: useless_move_count agora decai em _resolve_round (// 2).
            # Reset para 0 aqui cancelava o decaimento e ensinava que PASS = amnésia total.

            # ================================================
            # 🚫 PASS SPAM
            # ================================================

            reward -= 0.01

        # =====================================================
        # 💀 TERMINAL
        # =====================================================

        if self.hp <= 0:

            reward -= 20

            done = True

        if self.round > self.max_rounds:

            reward += 10

            done = True

        # =====================================================
        # 📊 REWARD NORMALIZATION
        # =====================================================
        # power_delta apenas para ações que NÃO são de movimento.
        # Movimentos já computam power_delta internamente — aplicar aqui seria contar duas vezes.
        current_power = self._get_board_power_cached()
        power_delta = current_power - self._last_board_power
        if action_type not in (ActionType.MOVE_BENCH, ActionType.MOVE_BOARD):
            reward += power_delta * 0.15
        self._last_board_power = current_power

        # FIX: high_cost_count como delta de transição — só recompensa mudanças,
        # nunca o estado estático. Evita reward passivo que dominava o sinal.
        board_units = [u for row in self.board for u in row if u]
        high_cost_count = sum(1 for u in board_units if u.get("cost", 1) >= 3)
        high_cost_delta = high_cost_count - self._last_high_cost_count
        if high_cost_delta > 0:
            reward += high_cost_delta * 0.5   # recompensa por colocar unidade cara
        elif high_cost_delta < 0:
            reward += high_cost_delta * 0.2   # penalidade leve por remover
        self._last_high_cost_count = high_cost_count

        # Penalidade por bench vazio (muitas vendas)
        bench_count = sum(1 for u in self.bench if u is not None)
        if bench_count == 0 and len(board_units) < self.level:
            reward -= 2.0

        # FIX: clip simples — tanh comprimia rewards medianos perto de zero,
        # tornando imperceptível a diferença entre ações boas e medianas.
        reward = float(np.clip(reward, -8.0, 8.0))

        # =====================================================
        # 🚀 RETURN
        # =====================================================
        if done:
            self._update_synergy_matrix(self._get_active_traits(), self._last_combat_won)



        return (

            self._get_state(),

            reward,

            done,

            info
        )

    # =========================================================
    # ROUND
    # =========================================================
    def _resolve_round(self, info):
        reward = 0.0

        info["round_end"] = True

        reward += self._resolve_round_rewards()
       
        # =========================================================
        # 💰 ECONOMIA BASE
        # =========================================================
        interest = min(self.gold // 10, 5)

        self.gold += 5 + interest
        self.xp += 2

        if self.level < 9 and self.xp >= self.xp_to_next.get(self.level, 999):
            self.level += 1
            self.xp = 0

        # =========================================================
        # 🧹 RESET ROUND
        # =========================================================
        self.units_bought_this_round = []
        self.action_count_this_round = 0
        self.move_count = 0
        for i in range(self.max_bench):
            if self.bench[i]:
                self.bench_stay_duration[i] += 1
            else:
                self.bench_stay_duration[i] = 0
        self._update_comp_focus()
        self.last_purchased_id = None
        self.last_bought_unit = None
        self.xp_bought_this_round = 0
        self.reroll_count_this_round = 0
        self.turn = 0
        self.unit_move_cooldown.clear()
        self.turn_spend_count = 0
        self.turn_gold_spent = 0
        self.previous_position_signatures.clear()
        self._last_bench_move_key.clear()
        self._unit_last_move.clear()
        self._bench_board_pos_cooldown.clear()
        self._last_bench_action = None
        self._last_board_action = None

        self._last_bench_swap = None
        self._last_board_swap = None

        # FIX: decaimento por round em vez de reset abrupto para 0.
        # Reset abrupto ensinava a IA que PASS "zera" a penalidade imediatamente,
        # criando o loop de PASS spam. Decaimento mantém memória de loops recentes.
        self.useless_move_count = max(0, self.useless_move_count // 2)

        # =========================================================
        # 🔄 NEXT ROUND
        # =========================================================
        self.round += 1
        self.shop = self._roll_shop()

        return reward

    # =========================================================
    # COMPRA
    # =========================================================
    def _compra_unidade(self, action):
        unit = self.shop[action]

        if not self._is_valid_unit(unit):
            return 0.0

        impacto = self._get_unit_board_impact(unit)

        comp_score = self._get_unit_comp_score(unit)

        upgrade_value = self._get_upgrade_value(unit)

        sim_impact = self._get_simulated_impact(unit)

        reward = 0.0

        units_on_board = sum(1 for row in self.board for u in row if u)

        bench_units = [u for u in self.bench if u]

        bench_full = len(bench_units) >= self.max_bench

        current_stage, _ = self._get_stage_info()

        # =========================================================
        # 🚫 BENCH FULL
        # =========================================================
        if bench_full and upgrade_value <= 0:
            return -0.5

        # =========================================================
        # 🌱 EARLY GAME
        # =========================================================
        if current_stage <= 2:

            if units_on_board == 0:
                reward += 0.8

            reward += 0.1

        # =========================================================
        # 📈 UPGRADE CHECK
        # =========================================================
        all_owned = self._get_all_units()

        copies = [
            u
            for u in all_owned
            if (u["id"] == unit["id"] and u["star"] == unit["star"])
        ]

        is_upgrade = False

        if len(copies) >= 2:  # já tem duas, esta será a terceira
            reward += self._upgrade_unit(
                unit["id"],
                unit["star"],
                extra_unit=unit,  # passa a unidade da loja como extra
            )

            self._invalidate_cache()

            self._invalidate_unit_caches()

            self._rebuild_unit_counts()

            is_upgrade = True

            reward += 1.5  # reduzido

        # =========================================================
        # 📦 ADD UNIT
        # =========================================================
        if not is_upgrade:

            free_slot = self._get_free_bench_slot()

            if free_slot is None:
                return -0.5

            self.bench[free_slot] = unit

            key = (unit["id"], unit["star"])

            self.unit_counts[key] = self.unit_counts.get(key, 0) + 1

            # 🧹 Atualiza pair_count
            self._update_pair_count_add(unit)
        
        # =========================================================
        # 💸 COST
        # =========================================================
        cost = unit["cost"]

        self.gold -= cost

        self.shop[action] = None

        self.turn_spend_count += 1

        self.turn_gold_spent += cost

        # =========================================================
        # 📈 UPGRADE BONUS
        # =========================================================
        if is_upgrade:

            if self.turn_spend_count <= 2:
                self.turn_spend_count *= 0.5

        # =========================================================
        # 🧠 TRACKING
        # =========================================================
        self.last_bought_unit = action

        self.units_bought_this_round.append(unit["id"])

        self.last_purchased_id = unit["id"]
        self.last_purchased_uuid = unit["uuid"]
        self.purchase_sell_block = 0

        # =========================================================
        # ⚔️ UNIT VALUE
        # =========================================================
        final_impact = 0.6 * impacto + 0.4 * sim_impact

        if final_impact > 0.8:
            reward += 0.7
        elif final_impact > 0.5:
            reward += 0.4
        elif final_impact > 0.2:
            reward += 0.1
        else:
            reward -= 0.2

        reward += sim_impact * 0.4

        reward += comp_score * 0.1

        # =========================================================
        # 🧩 PAIR VALUE
        # =========================================================
        if len(copies) == 1:
            reward += 0.4

        # =========================================================
        # 🚫 BAD UNIT
        # =========================================================
        if impacto < 0.2 and comp_score < 0.2:
            reward -= 0.4

        # =========================================================
        # 💸 LIGHT COST PENALTY
        # =========================================================
        reward -= cost * 0.08

        if self.strategy == Strategy.STABILIZE:
            if final_impact > 0.6:
                reward += 1.0  # bônus extra por comprar unidade forte
            elif final_impact < 0.2 and upgrade_value == 0:
                reward -= 1.2  # penalidade extra por comprar lixo

        self._invalidate_unit_caches()

        self._rebuild_unit_counts()

        return reward

    # =========================================================
    # MOVIMENTO
    # =========================================================
    def _move_bench_to_board(self, bench_slot, board_pos):

        reward = 0.0

        r, c = divmod(board_pos, 7)

        unit_b = self.bench[bench_slot]
        unit_f = self.board[r][c]

        if unit_b is None:
            return -1.0

        key = (unit_b["uuid"], bench_slot, board_pos)

        # =========================================================
        # ANTI LOOP DE ESTADO
        # =========================================================

        simulated_sig = self._simulate_full_state_signature(
            bench_slot,
            board_pos
        )

        if simulated_sig in self.previous_position_signatures:
            return -8.0

        # =========================================================
        # REGRA DE NÍVEL
        # =========================================================

        current_board_units = sum(
            1
            for row in self.board
            for u in row
            if u is not None
        )

        if unit_f is None:
            new_board_units = current_board_units + 1
        else:
            new_board_units = current_board_units

        if new_board_units > self.level:

            self.useless_move_count += 1

            return -6.0

        # =========================================================
        # SWAP CONSIGO MESMO
        # =========================================================

        if unit_f and unit_b["uuid"] == unit_f["uuid"]:
            reward -= 2.0

        # =========================================================
        # CONTROLE DE MOVIMENTAÇÃO
        # =========================================================

        self.move_count += 1

        if self.move_count > 8:
            reward -= 1.0

        last_turn = self.unit_move_cooldown.get(
            unit_b["uuid"],
            -999
        )

        if self.turn - last_turn < 3:
            reward -= 1.5

        # =========================================================
        # BOARD POWER ANTES
        # =========================================================

        before_power = self._get_board_power_cached()

        # =========================================================
        # EXECUTA TROCA
        # =========================================================

        self.bench[bench_slot], self.board[r][c] = (
            unit_f,
            unit_b
        )

        self._rebuild_role_matrix()
        self._update_synergy_if_needed()

        self._invalidate_cache()
        self._invalidate_unit_caches()

        # =========================================================
        # BOARD POWER DEPOIS
        # =========================================================

        after_power = self._get_board_power_cached()

        power_delta = after_power - before_power

        # =========================================================
        # GANHO / PERDA DE FORÇA
        # =========================================================

        if power_delta > 0:

            reward += power_delta * 0.5

            self.useless_move_count = max(
                0,
                self.useless_move_count - 2
            )

        else:

            reward += power_delta * 2.0

        # =========================================================
        # MOVIMENTO INÚTIL
        # =========================================================

        if abs(power_delta) < 0.50:

            self.useless_move_count += 1

            reward -= (
                0.5 +
                self.useless_move_count * 0.4
            )

        # =========================================================
        # MUITOS MOVIMENTOS INÚTEIS
        # =========================================================

        if self.useless_move_count >= 5:

            reward -= (
                self.useless_move_count * 0.75
            )

        if self.useless_move_count >= 8:

            reward -= 8.0

        # =========================================================
        # COOLDOWNS
        # =========================================================

        self.unit_move_cooldown[
            unit_b["uuid"]
        ] = self.turn

        if unit_f:

            self.unit_move_cooldown[
                unit_f["uuid"]
            ] = self.turn

        # =========================================================
        # HISTÓRICO
        # =========================================================

        self._last_bench_swap = (
            bench_slot,
            board_pos,
            unit_b["uuid"],
            unit_f["uuid"] if unit_f else None
        )

        self._last_bench_move_key.add(key)

        self._unit_last_move[
            (unit_b["uuid"], board_pos)
        ] = self.turn

        self._last_bench_action = (
            bench_slot,
            board_pos,
            self.turn
        )

        # =========================================================
        # SALVA ESTADO VISITADO
        # =========================================================

        self.previous_position_signatures.add(
            simulated_sig
        )

        self._bench_board_pos_cooldown[
            board_pos
        ] = self.turn

        # =========================================================
        # CLIP MAIS AMPLO
        # =========================================================

        return np.clip(reward, -10.0, 5.0)

    # =========================================================
    # 🔄 BOARD -> BOARD MOVE
    # =========================================================
    def _move_board_unit(self, from_pos, to_pos):

        reward = 0.0

        r1, c1 = divmod(from_pos, 7)
        r2, c2 = divmod(to_pos, 7)

        if from_pos == to_pos:
            return -1.0

        unit_a = self.board[r1][c1]
        unit_b = self.board[r2][c2]

        if unit_a is None:
            return -1.0

        # Salva referência da unidade movida
        moved_unit = unit_a

        # =========================================================
        # 🚫 TROCA CONSIGO MESMO
        # =========================================================

        if unit_b is not None and unit_a["uuid"] == unit_b["uuid"]:
            reward -= 2.0

        # =========================================================
        # 🔁 REVERSÃO IMEDIATA
        # =========================================================

        if self._last_board_swap is not None:

            last_from, last_to, last_uuid_a, last_uuid_b = self._last_board_swap

            if (
                from_pos == last_to
                and to_pos == last_from
                and moved_unit["uuid"] == last_uuid_b
            ):
                reward -= 5.0
                self.useless_move_count += 2

        # =========================================================
        # ⏳ COOLDOWN DA UNIDADE
        # =========================================================

        last_turn = self.unit_move_cooldown.get(
            moved_unit["uuid"],
            -999
        )

        if self.turn - last_turn < 3:
            reward -= 2.0

        # =========================================================
        # 📊 SCORE ANTES
        # =========================================================

        before_score = self._evaluate_board_positioning()

        # =========================================================
        # EXECUTA TROCA
        # =========================================================

        self.board[r1][c1], self.board[r2][c2] = (
            self.board[r2][c2],
            self.board[r1][c1]
        )

        self._rebuild_role_matrix()
        self._invalidate_cache()
        self._invalidate_unit_caches()

        # =========================================================
        # 📊 SCORE DEPOIS
        # =========================================================

        after_score = self._evaluate_board_positioning()

        delta = after_score - before_score

        # =========================================================
        # GANHO / PERDA ASSIMÉTRICA
        # =========================================================

        if delta > 0:

            reward += delta * 1.0

            self.useless_move_count = max(
                0,
                self.useless_move_count - 2
            )

        else:

            reward += delta * 4.0

        # =========================================================
        # MOVIMENTO INÚTIL
        # =========================================================

        if delta < 0.25:

            self.useless_move_count += 1

            reward -= (
                0.75 +
                self.useless_move_count * 0.3
            )

        elif delta < 0.50:

            self.useless_move_count += 0.5

            reward -= 0.25

        # =========================================================
        # SWAP COM VAZIO SEM BENEFÍCIO
        # =========================================================

        if unit_b is None and delta < 0.50:

            reward -= 1.5

            self.useless_move_count += 1

        # =========================================================
        # CONTROLE DE SPAM
        # =========================================================

        self.move_count += 1

        if self.move_count > 8:
            reward -= 1.0

        # =========================================================
        # LOOP EXATO
        # =========================================================

        move_key = (
            moved_unit["uuid"],
            from_pos,
            to_pos
        )

        if (
            hasattr(self, "_last_move_key")
            and move_key == self._last_move_key
        ):
            reward -= 8.0
            self.useless_move_count += 2

        self._last_move_key = move_key

        # =========================================================
        # MUITOS MOVIMENTOS INÚTEIS
        # =========================================================

        if self.useless_move_count >= 5:

            reward -= (
                self.useless_move_count * 0.75
            )

        if self.useless_move_count >= 8:

            reward -= 8.0

        # =========================================================
        # HISTÓRICO
        # =========================================================

        self.unit_move_cooldown[
            moved_unit["uuid"]
        ] = self.turn

        self._unit_last_move[
            (moved_unit["uuid"], to_pos)
        ] = self.turn

        self._last_board_swap = (
            from_pos,
            to_pos,
            moved_unit["uuid"],
            unit_b["uuid"] if unit_b else None
        )

        self._last_board_action = (
            from_pos,
            to_pos,
            self.turn
        )

        # =========================================================
        # ASSINATURA DE ESTADO
        # =========================================================

        board_sig = self._board_position_signature()

        self.previous_position_signatures.add(
            board_sig
        )

        # =========================================================
        # CLIP MAIS AMPLO
        # =========================================================

        return np.clip(reward, -10.0, 5.0)

    # =========================================================
    # VENDA
    # =========================================================
    def _vender_unidade(self, action):
        reward = 0.0

        unit = self.bench[action]

        if not unit:
            return -0.5

        # =========================================================
        # 🛡️ BLOQUEIO ANTI-COMPRA-VENDA RÁPIDA
        # =========================================================
        if self.purchase_sell_block > 0:
            return -2.0

        if (
            self.last_purchased_uuid == unit["uuid"]
            and self.turn < 2
        ):
            reward -= 3.0
            self.purchase_sell_block = 2
            self.last_sold_uuid = unit["uuid"]

        # =========================================================
        # 📊 AVALIAÇÃO DA UNIDADE
        # =========================================================
        impact = self._get_unit_board_impact(unit)
        comp_score = self._get_unit_comp_score(unit)
        upgrade_value = self._get_upgrade_value(unit)
        is_core = self._is_core_unit(unit)

        bench_count = sum(
            1 for u in self.bench
            if u is not None
        )

        units_on_board = sum(
            1 for row in self.board
            for u in row
            if u is not None
        )

        # =========================================================
        # 🎯 SCORE RELATIVO DA UNIDADE
        # =========================================================
        unit_score = (
            impact * 2.0 +
            comp_score * 1.5 +
            upgrade_value * 2.5
        )

        bench_scores = []

        for u in self.bench:

            if u is None:
                continue

            score = (
                self._get_unit_board_impact(u) * 2.0 +
                self._get_unit_comp_score(u) * 1.5 +
                self._get_upgrade_value(u) * 2.5
            )

            bench_scores.append(score)

        if bench_scores:
            avg_bench_score = np.mean(bench_scores)
            worst_bench_score = min(bench_scores)
        else:
            avg_bench_score = 0.0
            worst_bench_score = 0.0

        is_junk = unit_score <= avg_bench_score * 0.5

        is_very_junk = (
            unit_score <= worst_bench_score + 0.05
        )

        # =========================================================
        # ✅ VENDA DE UNIDADES RUINS
        # =========================================================
        if is_very_junk:
            reward += 4.0

        elif is_junk:
            reward += 2.5

        # =========================================================
        # BENCH CHEIO
        # =========================================================
        bench_fill_ratio = bench_count / self.max_bench

        if bench_fill_ratio >= 0.9:

            if is_junk:
                reward += 3.0

            elif is_very_junk:
                reward += 4.0

            else:
                reward -= 1.0

        # =========================================================
        # ❌ VENDA DE UNIDADES BOAS
        # =========================================================
        if not is_junk:

            if upgrade_value > 0:
                reward -= 3.0

            if is_core:
                reward -= 4.0

            if impact > 0.8:
                reward -= 3.0

            if comp_score > 1.2:
                reward -= 2.0

        # =========================================================
        # 🚫 NÃO SE AUTO-DESTRUIR
        # =========================================================
        if units_on_board <= 1 and bench_count == 1:
            reward -= 2.0

        # =========================================================
        # 🧠 AJUSTE POR ESTRATÉGIA
        # =========================================================
        if self.strategy == Strategy.ECON:

            if is_junk:
                reward += 1.0

        elif self.strategy == Strategy.STABILIZE:

            if is_junk:
                reward += 1.0

            elif impact > 0.5:
                reward -= 1.0

        elif self.strategy == Strategy.SLOWROLL:

            if unit["cost"] <= 2 and is_junk:
                reward += 0.8

        elif self.strategy == Strategy.FAST8:

            if not is_core and upgrade_value == 0:
                reward += 0.8

        # =========================================================
        # 💰 EXECUTA VENDA
        # =========================================================
        self.gold += unit["cost"]

        self.bench[action] = None

        key = (unit["id"], unit["star"])

        if key in self.unit_counts:
            self.unit_counts[key] -= 1

            if self.unit_counts[key] <= 0:
                del self.unit_counts[key]

        self._update_pair_count_remove(unit)

        self._invalidate_unit_caches()

        self._rebuild_unit_counts()

        # =========================================================
        # LIBEROU ESPAÇO NO BENCH
        # FIX: só dá o bônus se a bench estava CHEIA antes da venda.
        # Antes dava +0.5 a toda venda, incentivando vender tudo.
        # =========================================================
        new_bench_count = sum(
            1 for u in self.bench
            if u is not None
        )

        bench_was_full = bench_count >= self.max_bench - 1
        if bench_was_full and new_bench_count < bench_count:
            reward += 1.5

        if is_junk:
            self.useless_move_count = max(
                0,
                self.useless_move_count - 2
            )

        # =========================================================
        # CLIP FINAL
        # =========================================================
        return np.clip(reward, -6.0, 10.0)

    # =========================================================
    # XP
    # =========================================================
    def _buy_xp(self):
        if self.gold < 4 or self.level >= 10:
            return -0.5

        stage, _ = self._get_stage_info()

        board_power = self._get_board_power_cached()

        avg_power = self._get_avg_board_power()

        power_ratio = board_power / (avg_power + 1e-6)

        reward = -0.08

        cost = 4

        units_on_board = sum(1 for row in self.board for u in row if u)

        # =========================================================
        # 📈 TIMING
        # =========================================================
        if stage <= 2:
            reward -= 0.6
        elif stage >= 4:
            reward += 0.15

        # =========================================================
        # ⚔️ BOARD STATE
        # =========================================================
        if power_ratio < 0.78:
            reward -= 1.0
        elif power_ratio < 0.92:
            reward -= 0.4
        elif power_ratio > 1.08:
            reward += 0.2

        # =========================================================
        # 🧠 UNIT CAP PRESSURE
        # =========================================================
        if units_on_board >= self.level:
            reward += 0.2
        else:
            reward -= 0.25

        # =========================================================
        # 🚀 PRE LEVEL
        # =========================================================
        xp_needed = self.xp_to_next[self.level] - self.xp

        if xp_needed <= 4:
            reward += 0.4

        # =========================================================
        # 🔥 WIN STREAK
        # =========================================================
        if self.win_streak >= 3:
            reward += 0.25

        # =========================================================
        # 🩸 LOSS STREAK
        # =========================================================
        if self.lose_streak >= 3:
            reward -= 0.3

        # =========================================================
        # 🎯 STRATEGY
        # =========================================================

        # =========================================================
        # 💰 ECON
        # =========================================================
        if self.strategy == Strategy.ECON:

            if self.gold < 30:
                reward -= 0.7
            elif self.gold >= 50:
                reward += 0.1

        # =========================================================
        # ⚔️ STABILIZE
        # Dentro de _buy_xp, na seção da estratégia STABILIZE (aproximadamente linha 1800)
        elif self.strategy == Strategy.STABILIZE:
            if power_ratio < 0.9:
                reward -= 3.0   # antes -1
            else:
                reward += 0.1
            # Adiciona penalidade extra se board tem poucas unidades
            if units_on_board <= 2:
                reward -= 2.0

        # =========================================================
        # 🚀 FAST8
        # =========================================================
        elif self.strategy == Strategy.FAST8:

            reward += 0.6
            if stage >= 4:
                reward += 0.25
            if self.gold >= 50:
                reward += 0.25

        # =========================================================
        # 🎲 REROLL
        # =========================================================
        elif self.strategy == Strategy.SLOWROLL:

            reward -= 0.8
            if self.level in [5, 6]:
                reward -= 0.3

        # =========================================================
        # 🔥 WINSTREAK
        # =========================================================
        elif self.strategy == Strategy.WINSTREAK:

            reward += 0.3
            if power_ratio > 1.0:
                reward += 0.2

        # =========================================================
        # 🩸 LOSS_STREAK
        # =========================================================
        elif self.strategy == Strategy.LOSS_STREAK:

            reward -= 0.7
            if self.gold < 50:
                reward -= 0.3

        # =========================================================
        # 💀 LOW HP
        # =========================================================
        if self.hp < 35:

            if power_ratio < 0.9:
                reward -= 0.5
            else:
                reward += 0.2

        # =========================================================
        # 💸 APPLY XP
        # =========================================================
        self.gold -= cost

        self.xp += cost

        self.turn_spend_count += 1

        self.turn_gold_spent += cost

        self.xp_bought_this_round += 1

        # =========================================================
        # 📈 LEVEL UP
        # =========================================================
        leveled = False

        if self.xp >= self.xp_to_next[self.level]:

            self.level += 1

            self.xp = 0

            leveled = True

        if leveled:
            reward += 0.7  # mantém
            if power_ratio >= 0.9:
                reward += 0.25
            # NOVO: se subiu de nível mas board continua fraco, penaliza
            if power_ratio < 0.8 and self.strategy == Strategy.STABILIZE:
                reward -= 1.5
            if self.strategy == Strategy.FAST8:
                reward += 0.4

        return np.clip(reward, -4.0, 4.0)

    # =========================================================
    # REROLL
    # =========================================================
    def _reroll(self):
        self.reroll_count_this_round += 1
        if self.gold < 2:
            return -0.8
        stage, _ = self._get_stage_info()
        board_power = self._get_board_power_cached()
        avg_power = self._get_avg_board_power()
        power_ratio = board_power / (avg_power + 1e-6)
        old_value = sum(self._get_unit_comp_score(u) for u in self.shop if u)
        reward = 0.0
        cost = 2
        self.gold -= cost
        self.shop = self._roll_shop()
        self.turn_spend_count += 1
        self.turn_gold_spent += cost
        new_value = sum(self._get_unit_comp_score(u) for u in self.shop if u)
        delta_shop = new_value - old_value
        reward += np.tanh(delta_shop * 0.15) * 1.2   # maior peso para melhoria real
        if new_value > old_value:
            reward += 0.3
        elif new_value < old_value:
            reward -= 0.2
        if new_value < 1.5:
            reward -= 0.3

        if self.strategy == Strategy.ECON:
            reward -= 1.0
            if self.gold < 30:
                reward -= 0.5
            if stage <= 3:
                reward -= 0.3
        elif self.strategy == Strategy.STABILIZE:
            # Bônus reduzido drasticamente
            reward += 0.8   # antes 2.0
            if power_ratio < 0.9:
                reward += 0.3   # antes 1.0
            if self.hp < 50:
                reward += 0.2   # antes 0.5
        elif self.strategy == Strategy.FAST8:
            reward -= 1.0
            if self.level < 8:
                reward -= 0.5
            if stage >= 4:
                reward -= 0.3
        elif self.strategy == Strategy.SLOWROLL:
            reward += 1.0
            if 50 <= self.gold <= 70:
                reward += 0.5
            if stage >= 3:
                reward += 0.3
            if self.level <= 6:
                reward += 0.3
        elif self.strategy == Strategy.ALL_IN:
            reward += 1.0
            if self.hp < 35:
                reward += 0.5
            if power_ratio < 0.85:
                reward += 0.3
            if self.gold <= 20:
                reward += 0.1
        elif self.strategy == Strategy.WINSTREAK:
            if power_ratio > 1.0:
                reward += 0.5
            if self.hp > 70:
                reward += 0.25
            if self.gold < 30:
                reward -= 0.4
        elif self.strategy == Strategy.LOSS_STREAK:
            reward -= 1.3
            if stage <= 3:
                reward -= 0.7
            if self.gold < 50:
                reward -= 0.5

        # Penalidades por timing e spam
        if stage <= 2:
            reward -= 1.3
        elif stage == 3:
            reward -= 0.3
        if power_ratio > 1.05:
            reward -= 0.7
        elif power_ratio < 0.85:
            reward += 0.25
        if self.gold > 50:
            reward += 0.25
        elif self.gold < 20:
            reward -= 0.5
        reward -= 0.1 * (self.reroll_count_this_round ** 1.2)
        if self.reroll_count_this_round > 6:
            reward -= 0.8
        if self.reroll_count_this_round > 10:
            reward -= 1.5

        bench_full = sum(1 for u in self.bench if u is not None) >= self.max_bench
        if bench_full:
            useful_in_shop = 0
            for unit in self.shop:
                if unit is None:
                    continue
                impact = self._get_unit_board_impact(unit)
                upgrade_val = self._get_upgrade_value(unit)
                if impact > 0.2 or upgrade_val > 0:
                    useful_in_shop += 1
            if useful_in_shop > 0:
                reward -= 0.4 * useful_in_shop
                self.useless_move_count += 0.5

        return reward

    # =========================================================
    # MASKS (OTIMIZADA)
    # =========================================================
    def _get_action_masks(self):

        return {

            # =====================================================
            # 🎯 ACTION TYPE
            # =====================================================

            "type_mask": self._get_type_mask(),

            # =====================================================
            # 🛒 BUY
            # =====================================================

            "shop_mask": self._get_shop_mask(),

            # =====================================================
            # 🔄 BENCH SOURCE
            # =====================================================

            "bench_source_mask": self._get_bench_source_mask(),

            # =====================================================
            # 🔄 BOARD SOURCE
            # =====================================================

            "board_source_mask": self._get_board_source_mask(),

            # =====================================================
            # 🎯 GENERIC BOARD TARGET
            # (MOVE_BENCH)
            # =====================================================

            "board_target_mask": self._get_board_target_mask(),

            # =====================================================
            # 🔥 AUTOREGRESSIVE TARGETS
            # =====================================================

            "board_move_target_masks":
                self._get_all_board_move_target_masks(),
        }

    # =========================================================
    # 🎯 TYPE MASK
    # =========================================================
    def _get_type_mask(self):

        mask = np.ones(
            len(ActionType),
            dtype=np.float32
        )

        board = self.board
        bench = self.bench
        gold = self.gold
        strategy = self.strategy

        stage, _ = self._get_stage_info()

        units_on_board = sum(
            1 for row in board for u in row if u is not None
        )

        bench_count = sum(
            1 for u in bench if u is not None
        )

        can_place_unit = (
            units_on_board < self.level
        )

        # =====================================================
        # 🚫 ACTION LIMIT
        # =====================================================

        if (
            self.action_count_this_round
            >= self.max_actions_per_round
        ):

            mask[:] = 0

            mask[ActionType.PASS] = 1

            return mask

        # =====================================================
        # 💰 GOLD RULES
        # =====================================================

        if gold < 2:

            mask[ActionType.REROLL] = 0

        if gold < 4:

            mask[ActionType.BUY_XP] = 0

        # =====================================================
        # 🧠 STRATEGY FILTER
        # =====================================================

        power_ratio = 1.0

        if strategy in (

            Strategy.STABILIZE,
            Strategy.WINSTREAK,
            Strategy.ALL_IN

        ):

            board_power = (
                self._get_board_power_cached()
            )

            avg_power = (
                self._get_avg_board_power()
            )

            power_ratio = (
                board_power / (avg_power + 1e-6)
            )

        if strategy == Strategy.ECON:

            if stage <= 3:

                mask[ActionType.REROLL] = 0

            if gold < 30 and stage <= 3:

                mask[ActionType.BUY_XP] = 0

        elif strategy == Strategy.STABILIZE:

            if power_ratio < 0.9:

                mask[ActionType.BUY_XP] = 0
            # Dentro de _get_type_mask, antes de retornar a mask
            if self.xp_bought_this_round >= 2:
                mask[ActionType.BUY_XP] = 0

        elif strategy == Strategy.FAST8:

            mask[ActionType.REROLL] = 0

        elif strategy == Strategy.SLOWROLL:

            if gold < 50:

                mask[ActionType.REROLL] = 0

            mask[ActionType.BUY_XP] = 0

        elif strategy == Strategy.LOSS_STREAK:

            mask[ActionType.REROLL] = 0
            mask[ActionType.BUY_XP] = 0

        # =====================================================
        # 🛒 BUY
        # =====================================================

        shop_mask = self._get_shop_mask()

        if shop_mask.sum() == 0:

            mask[ActionType.BUY] = 0

        # =====================================================
        # 🔄 MOVE BENCH
        # =====================================================

        bench_mask = (
            self._get_bench_source_mask()
        )

        if bench_mask.sum() == 0:

            mask[ActionType.MOVE_BENCH] = 0

        # =====================================================
        # 💸 SELL
        # =====================================================

        if bench_mask.sum() == 0:

            mask[ActionType.SELL] = 0

        # =====================================================
        # 🔄 MOVE BOARD
        # =====================================================

        if not self._has_valid_board_move():

            mask[ActionType.MOVE_BOARD] = 0

        # =====================================================
        # 🚫 FORCE PLACE RULE
        # =====================================================

        if can_place_unit and bench_count > 0:

            mask[ActionType.MOVE_BOARD] = 0

            mask[ActionType.PASS] = 0

        # =====================================================
        # 🚨 FAILSAFE
        # =====================================================

        if mask.sum() == 0:

            mask[ActionType.PASS] = 1

        return mask

    # =========================================================
    # 🛒 SHOP MASK
    # =========================================================
    def _get_shop_mask(self):

        mask = np.zeros(
            5,
            dtype=np.float32
        )

        gold = self.gold

        strategy = self.strategy

        # =====================================================
        # 🚫 BENCH FULL
        # =====================================================

        bench_count = sum(
            1 for u in self.bench if u is not None
        )

        if bench_count >= self.max_bench:

            return mask

        # =====================================================
        # 🧠 MAIN TRAIT
        # =====================================================

        main_trait = None

        if self.comp_locked and self.comp_traits:

            main_trait = max(

                self.comp_traits,

                key=self.comp_traits.get
            )

        # =====================================================
        # 🛒 LOOP
        # =====================================================

        for i in range(5):

            unit = self.shop[i]

            if unit is None:
                continue

            if gold < unit["cost"]:
                continue

            # =================================================
            # 🧠 COMP FILTER
            # =================================================

            if self.comp_locked and main_trait:

                if (
                    main_trait
                    not in unit.get("traits", [])
                ):
                    continue

            impact = (
                self._get_simulated_impact(unit)
            )

            # =================================================
            # 🧠 STRATEGY FILTERS
            # =================================================

            if strategy == Strategy.ECON:

                if (

                    unit["cost"] >= 4
                    and impact < 0.4
                    and gold < 40

                ):
                    continue

            elif strategy == Strategy.STABILIZE:

                if impact < 0.15:
                    continue

            elif strategy == Strategy.FAST8:

                stage, _ = self._get_stage_info()

                if (

                    stage >= 4
                    and unit["cost"] <= 2
                    and impact < 0.3

                ):
                    continue

            elif strategy == Strategy.SLOWROLL:

                if (

                    unit["cost"] >= 4
                    and impact < 0.5

                ):
                    continue

            mask[i] = 1

        return mask


    # =========================================================
    # 🔄 BENCH SOURCE MASK
    # =========================================================
    def _get_bench_source_mask(self):
        mask = np.zeros(9, dtype=np.float32)

        board_impacts = []

        for row in self.board:
            for unit in row:
                if unit is not None:
                    board_impacts.append(unit.get("impact", 0.0))

        weakest_board = min(board_impacts) if board_impacts else 0.0

        for i, unit in enumerate(self.bench):

            if unit is None:
                continue

            impact = unit.get("impact", 0.0)

            units_on_board = sum(
                1 for row in self.board
                for u in row if u is not None
            )

            board_not_full = units_on_board < self.level

            if board_not_full:
                mask[i] = 1
                continue

            if impact >= weakest_board - 0.2:
                mask[i] = 1

        return mask

    # =========================================================
    # 🎯 (MOVE_BENCH)
    # =========================================================
    def _get_board_move_target_mask(
        self,
        from_pos
    ):

        mask = np.zeros(
            28,
            dtype=np.float32
        )

        # =====================================================
        # FORÇA PASS APÓS MUITOS MOVIMENTOS INÚTEIS
        # =====================================================

        if self.useless_move_count >= 5:
            return mask

        r1, c1 = divmod(from_pos, 7)

        source_unit = self.board[r1][c1]

        if source_unit is None:
            return mask

        before_score = self._evaluate_board_positioning()

        for to_pos in range(28):

            if to_pos == from_pos:
                continue

            r2, c2 = divmod(to_pos, 7)

            # =====================================================
            # COOLDOWN DE POSIÇÃO
            # =====================================================

            key = (
                source_unit["uuid"],
                to_pos
            )

            last_turn = self._unit_last_move.get(
                key,
                -999
            )

            if self.turn - last_turn < 3:
                continue

            # =====================================================
            # ANTI REVERSÃO
            # =====================================================

            if self._last_board_action:

                last_from, last_to, _ = (
                    self._last_board_action
                )

                if (
                    from_pos == last_to
                    and
                    to_pos == last_from
                ):
                    continue

            # =====================================================
            # ASSINATURA FUTURA
            # =====================================================

            future_sig = (
                self._simulate_board_swap_signature(
                    from_pos,
                    to_pos
                )
            )

            if (
                future_sig
                in self.previous_position_signatures
            ):
                continue

            # =====================================================
            # SIMULA TROCA
            # =====================================================

            self.board[r1][c1], self.board[r2][c2] = (
                self.board[r2][c2],
                self.board[r1][c1]
            )

            self._rebuild_role_matrix()

            try:

                after_score = (
                    self._evaluate_board_positioning()
                )

            finally:

                self.board[r1][c1], self.board[r2][c2] = (
                    self.board[r2][c2],
                    self.board[r1][c1]
                )

                self._rebuild_role_matrix()

            delta = after_score - before_score

            # =====================================================
            # FILTRO DE QUALIDADE
            # =====================================================

            # movimento claramente ruim
            if delta < -0.25:
                continue

            # =====================================================
            # LIBERA
            # =====================================================

            mask[to_pos] = 1

        return mask
    
    # =========================================================
    # 🔄 BOARD SOURCE MASK
    # =========================================================
    def _get_board_source_mask(self):

        mask = np.zeros(
            28,
            dtype=np.float32
        )

        for pos in range(28):

            r, c = divmod(pos, 7)

            unit = self.board[r][c]

            if unit is None:
                continue

            target_mask = self._get_board_move_target_mask(
                pos
            )

            if target_mask.sum() > 0:
                mask[pos] = 1

        return mask


    # =========================================================
    # 🔥 VALID MOVE CHECK
    # =========================================================
    def _has_valid_board_move(self):

        source_mask = self._get_board_source_mask()

        valid_sources = np.where(
            source_mask == 1
        )[0]

        for source in valid_sources:

            target_mask = self._get_board_move_target_mask(
                source
            )

            if target_mask.sum() > 0:
                return True

        return False


    # =========================================================
    # 🔥 ALL TARGET MASKS
    # =========================================================
    def _get_all_board_move_target_masks(self):

        masks = []

        for from_pos in range(28):

            masks.append(
                self._get_board_move_target_mask(
                    from_pos
                )
            )

        return np.stack(masks)


    # =========================================================
    # 🎯 CONDITIONAL TARGET MASK
    # =========================================================
    def _get_board_target_mask(self):
        mask = np.zeros(28, dtype=np.float32)

        units_on_board = sum(
            1 for row in self.board
            for u in row if u is not None
        )

        can_place_unit = units_on_board < self.level

        bench_indices = [
            i for i, u in enumerate(self.bench)
            if u is not None
        ]

        for pos in range(28):

            r, c = divmod(pos, 7)
            target_unit = self.board[r][c]

            # ==================================================
            # Não pode colocar em slot vazio se board já está cheia
            # ==================================================
            if target_unit is None and not can_place_unit:
                continue

            if not bench_indices:
                continue

            allowed_for_any = False

            for bench_idx in bench_indices:

                unit = self.bench[bench_idx]

                if unit is None:
                    continue

                # ==================================================
                # 1) Repetição exata
                # ==================================================
                key = (unit["uuid"], bench_idx, pos)

                if key in self._last_bench_move_key:
                    continue

                # ==================================================
                # 2) Cooldown por posição
                # ==================================================
                last_turn_board = self._bench_board_pos_cooldown.get(pos, -999)

                if self.turn - last_turn_board < 3:
                    continue

                # ==================================================
                # 3) Filtro de impacto
                # Evita trocar unidade forte por fraca
                # ==================================================
                if target_unit is not None:

                    bench_impact = unit.get("impact", 0.0)
                    board_impact = target_unit.get("impact", 0.0)

                    # margem pequena para permitir exploração
                    if bench_impact < board_impact - 0.3:
                        continue

                allowed_for_any = True
                break

            if allowed_for_any:
                mask[pos] = 1

        return mask

    # =========================================================
    # COMBATE (OTIMIZADO COM PRÉ-ALOCAÇÃO)
    # =========================================================
    def _simulate_combat(self, use_cache=True):
        # =========================================================
        # 1. CÁLCULO DO BÔNUS TÁTICO ALIADO (baseado no board real)
        # =========================================================
        
        # Gerar chave de cache se necessário
        if use_cache:
            board_sig = self._board_position_signature()  # assinatura do board+bench
            stage, _ = self._get_stage_info()
            cache_key = (board_sig, self.level, stage)
            if cache_key in self._combat_sim_cache:
                return self._combat_sim_cache [cache_key]
        
        position_score = self.combat_profile_mgr.evaluate_positioning(self.board)
        carry_score = self.combat_profile_mgr.evaluate_main_carry_safety(
            self.board, self._get_unit_board_impact
        )

        frontline_units = 0
        backline_units = 0
        tanks_frontline = 0
        carries_frontline = 0
        frontline_cols = []
        carry_protected_count = 0
        isolated_carries = 0
        clump_penalty = 0.0

        for row in range(4):
            for col in range(7):
                unit = self.board[row][col]
                if not unit:
                    continue
                role = unit.get("role")
                if self.combat_profile_mgr.is_frontline(row):
                    frontline_units += 1
                else:
                    backline_units += 1
                if role == UnitRole.TANK and self.combat_profile_mgr.is_frontline(row):
                    tanks_frontline += 1
                    frontline_cols.append(col)
                if role == UnitRole.CARRY and self.combat_profile_mgr.is_frontline(row):
                    carries_frontline += 1
                if role == UnitRole.CARRY:
                    nearby_allies = 0
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            if dr == 0 and dc == 0:
                                continue
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < 4 and 0 <= nc < 7 and self.board[nr][nc]:
                                nearby_allies += 1
                    if nearby_allies >= 2:
                        carry_protected_count += 1
                    if nearby_allies == 0:
                        isolated_carries += 1
                adjacent = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < 4 and 0 <= nc < 7 and self.board[nr][nc]:
                            adjacent += 1
                if adjacent >= 4:
                    clump_penalty += 0.1

        frontline_width_bonus = 0.0
        if len(frontline_cols) >= 2:
            width = max(frontline_cols) - min(frontline_cols)
            frontline_width_bonus = min(0.8, width * 0.1)

        tactical_bonus = 0.0
        tactical_bonus += position_score * 0.2
        tactical_bonus += carry_score * 0.25
        tactical_bonus += min(tanks_frontline, 3) * 0.3
        tactical_bonus += frontline_width_bonus
        tactical_bonus += carry_protected_count * 0.2
        tactical_bonus -= isolated_carries * 0.25
        tactical_bonus -= carries_frontline * 0.8
        tactical_bonus -= clump_penalty

        # =========================================================
        # 2. CÁLCULO DO BÔNUS TÁTICO INIMIGO (simulado)
        # =========================================================
        stage, _ = self._get_stage_info()
        enemy_count = max(1, self.level)
        frontline_enemies = min(enemy_count, 4)
        backline_enemies = enemy_count - frontline_enemies
        enemy_tanks = min(frontline_enemies, 2)
        enemy_carries = min(backline_enemies, 2)

        enemy_tactical_bonus = 0.0
        enemy_tactical_bonus += min(enemy_tanks, 3) * 0.3
        enemy_tactical_bonus += min(enemy_carries, 2) * 0.2
        if frontline_enemies >= 2:
            width = min(6, frontline_enemies - 1)
            enemy_tactical_bonus += min(0.8, width * 0.1)
        if enemy_carries > 0 and enemy_tanks > 0:
            enemy_tactical_bonus += 0.4
        if frontline_enemies >= 5:
            enemy_tactical_bonus -= 0.2

        # =========================================================
        # 3. CONSTRUÇÃO DAS UNIDADES (aliadas e inimigas) - PRÉ-ALOCAÇÃO
        # =========================================================
        MAX_UNITS = 28
        ally_hp_arr = np.zeros(MAX_UNITS, dtype=np.float32)
        ally_dps_arr = np.zeros(MAX_UNITS, dtype=np.float32)
        ally_row_arr = np.zeros(MAX_UNITS, dtype=np.int32)
        ally_col_arr = np.zeros(MAX_UNITS, dtype=np.int32)
        ally_attack_interval_arr = np.zeros(MAX_UNITS, dtype=np.float32)
        ally_attack_range_arr = np.zeros(MAX_UNITS, dtype=np.int32)
        ally_role_arr = np.zeros(MAX_UNITS, dtype=np.int32)
        ally_armor_arr = np.zeros(MAX_UNITS, dtype=np.float32)

        n_allies = 0
        for row in range(4):
            for col in range(7):
                unit = self.board[row][col]
                if not unit:
                    continue
                profile = unit.get("combat_profile", {})
                hp_bonus = 1.0 + tactical_bonus * 0.2
                dps_bonus = 1.0 + tactical_bonus * 0.15
                ally_hp_arr[n_allies] = profile.get("max_hp", profile.get("hp", 600)) * hp_bonus
                ally_dps_arr[n_allies] = profile.get("dps", 30) * dps_bonus
                ally_row_arr[n_allies] = row
                ally_col_arr[n_allies] = col
                ally_attack_interval_arr[n_allies] = profile.get("attack_interval", 1.0)
                ally_attack_range_arr[n_allies] = profile.get("attack_range", 1)
                role = unit.get("role", UnitRole.FIGHTER)
                ally_role_arr[n_allies] = int(role)
                ally_armor_arr[n_allies] = profile.get("armor", 0)
                n_allies += 1

        # Inimigos
        base_hp = 500 + stage * 120
        base_dps = 35 + stage * 8
        enemy_hp = base_hp * (1 + enemy_tactical_bonus * 0.2)
        enemy_dps = base_dps * (1 + enemy_tactical_bonus * 0.15)

        enemy_hp_arr = np.zeros(MAX_UNITS, dtype=np.float32)
        enemy_dps_arr = np.zeros(MAX_UNITS, dtype=np.float32)
        enemy_attack_interval = np.zeros(MAX_UNITS, dtype=np.float32)
        enemy_attack_range = np.zeros(MAX_UNITS, dtype=np.int32)
        enemy_row = np.zeros(MAX_UNITS, dtype=np.int32)
        enemy_col = np.zeros(MAX_UNITS, dtype=np.int32)
        enemy_role = np.zeros(MAX_UNITS, dtype=np.int32)
        enemy_armor = np.zeros(MAX_UNITS, dtype=np.float32)

        for i in range(enemy_count):
            enemy_hp_arr[i] = enemy_hp
            enemy_dps_arr[i] = enemy_dps
            enemy_attack_interval[i] = 1.0
            enemy_attack_range[i] = 1
            enemy_row[i] = 0 if i < 4 else 1
            enemy_col[i] = i % 7
            enemy_role[i] = UnitRole.FIGHTER
            enemy_armor[i] = 0.0

        # =========================================================
        # 4. SIMULAÇÃO DE COMBATE (versão Numba) com slices
        # =========================================================
        (ally_alive, enemy_alive, ally_hp_final, enemy_hp_final) = _combat_simulation_numba(
            ally_hp_arr[:n_allies],
            ally_dps_arr[:n_allies],
            ally_attack_interval_arr[:n_allies],
            ally_attack_range_arr[:n_allies],
            ally_row_arr[:n_allies],
            ally_col_arr[:n_allies],
            ally_role_arr[:n_allies],
            ally_armor_arr[:n_allies],
            enemy_hp_arr[:enemy_count],
            enemy_dps_arr[:enemy_count],
            enemy_attack_interval[:enemy_count],
            enemy_attack_range[:enemy_count],
            enemy_row[:enemy_count],
            enemy_col[:enemy_count],
            enemy_role[:enemy_count],
            enemy_armor[:enemy_count],
            max_time=30.0,
            dt=0.5
        )

        # Processa resultados
        survived_allies = np.sum(ally_alive)
        deaths = n_allies - survived_allies
        ally_score = np.sum(ally_hp_final[ally_alive])
        enemy_score = np.sum(enemy_hp_final[enemy_alive])
        # Verifica se algum carry aliado sobreviveu
        carry_alive = False
        for i in range(n_allies):
            if ally_alive[i] and ally_role_arr[i] == UnitRole.CARRY:
                carry_alive = True
                break

        won = ally_score >= enemy_score
        score = (ally_score - enemy_score) * 0.01
        ticks = 30.0

        result = {
            "win": won,
            "survived_units": int(survived_allies),
            "deaths": int(deaths),
            "carry_survived": carry_alive,
            "ticks": ticks,
            "score": score,
            "tactical_bonus_ally": tactical_bonus,
            "tactical_bonus_enemy": enemy_tactical_bonus,
            "carries_frontline": carries_frontline,
            "frontline_units": frontline_units,
            "backline_units": backline_units,
            "tanks_frontline": tanks_frontline
        }

        # Armazena no cache
        if use_cache:
            self._combat_sim_cache [cache_key] = result

        return result

    # =========================================================
    # ANTI LOOP
    # =========================================================
    def _board_position_signature(self):
        sig = []
        for r in range(self.rows):
            for c in range(self.cols):
                u = self.board[r][c]
                if u is None:
                    sig.append(".")
                else:
                    role = self.combat_profile_mgr.get_role(u)
                    sig.append(f"B:{role}:{u['name']}:{u['star']}")
        bench_items = []
        for u in self.bench:
            if u is None:
                bench_items.append(".")
            else:
                role = self.combat_profile_mgr.get_role(u)
                bench_items.append(f"b:{role}:{u['name']}:{u['star']}")
        bench_items.sort()
        sig.extend(bench_items)
        return tuple(sig)   # achatado

    def _simulate_full_state_signature(self, bench_slot, board_pos):
        r, c = divmod(board_pos, 7)
        temp_board = [row[:] for row in self.board]
        temp_bench = self.bench[:]
        # Troca
        temp_board[r][c], temp_bench[bench_slot] = temp_bench[bench_slot], temp_board[r][c]
        sig = []
        # Board
        for rr in range(self.rows):
            for cc in range(self.cols):
                u = temp_board[rr][cc]
                sig.append("." if u is None else f"B:{self.combat_profile_mgr.get_role(u)}:{u['name']}:{u['star']}")
        # Bench (ordenado)
        bench_items = []
        for u in temp_bench:
            bench_items.append("." if u is None else f"b:{self.combat_profile_mgr.get_role(u)}:{u['name']}:{u['star']}")
        bench_items.sort()
        sig.extend(bench_items)
        return tuple(sig)   # tupla achatada
    
    def _simulate_board_swap_signature(self, from_pos, to_pos):
        """Simula a troca entre duas posições do board e retorna a assinatura completa."""
        r1, c1 = divmod(from_pos, 7)
        r2, c2 = divmod(to_pos, 7)
        
        temp_board = [row[:] for row in self.board]
        temp_bench = self.bench[:]  # bench não muda, mas incluímos para assinatura completa
        
        # Troca
        temp_board[r1][c1], temp_board[r2][c2] = temp_board[r2][c2], temp_board[r1][c1]
        
        # Gera assinatura (mesmo código de _get_full_state_signature)
        sig = []
        for r in range(self.rows):
            for c in range(self.cols):
                u = temp_board[r][c]
                if u is None:
                    sig.append(".")
                else:
                    role = self.combat_profile_mgr.get_role(u)
                    sig.append(f"B:{role}:{r}:{c}")
        bench_items = []
        for u in temp_bench:
            if u is None:
                bench_items.append(".")
            else:
                role = self.combat_profile_mgr.get_role(u)
                bench_items.append(f"b:{role}:{u['name']}:{u['star']}")
        bench_items.sort()
        sig.extend(bench_items)
        return tuple(sig)
    
    # =========================================================
    # REWARD
    # =========================================================
    def _resolve_round_rewards(self):
        reward = 0

        reward += self._reward_strategy_alignment()
        reward += self._combat_reward()
        reward += self._reward_board_fill()
        reward += self._streak_reward()
        reward += self._level_timing_reward()
        reward += self._reward_bench()
        reward += self._position_reward()
        reward += self._synergy_rewards()

        return reward
    
    def _reward_strategy_alignment(self):
        reward = 0.0
        stage, round_in_stage = self._get_stage_info()

        if self.strategy == Strategy.FAST8:
            level = self.level
            
            # 1. Bônus por atingir nível 8 no timing ideal
            if level >= 8:
                ideal_stage_for_8 = 4.0
                current_stage_float = stage + (round_in_stage / 7.0)
                timing_score = max(0, 1.0 - (current_stage_float - ideal_stage_for_8) * 0.5)
                timing_score = min(1.0, timing_score)
                reward += timing_score * 2.0
            else:
                if stage >= 4:
                    delay = (stage - 4) * 0.5 + (round_in_stage / 14.0)
                    reward -= min(2.0, delay)
            
            # 2. Recompensa por manter gold (mais generosa)
            if self.gold >= 50:
                reward += 1.5
            elif self.gold >= 40:
                reward += 0.8
            elif self.gold < 20 and level < 8:
                reward -= 0.8
            
            # 3. Bônus/penalidade por board power
            board_power = self._get_board_power_cached()
            expected_power = self._expected_board_power()
            power_ratio = board_power / (expected_power + 1e-6)
            if level >= 8:
                if power_ratio >= 0.9:
                    reward += 0.8
                elif power_ratio < 0.6:
                    reward -= 2.0   # penalidade maior
                elif power_ratio < 0.7:
                    reward -= 1.0
            
            # 4. Bônus por pre-level
            expected_level = 4 + stage
            level_diff = level - expected_level
            if level_diff > 0:
                reward += min(1.5, level_diff * 0.4)
            elif level_diff < 0 and stage >= 3:
                reward -= min(1.5, abs(level_diff) * 0.5)   # penalidade maior

        elif self.strategy == Strategy.ECON:
            board_stable = self._is_board_stable()
            gold = self.gold

            if stage <= 2:
                target_gold = 20
            elif stage <= 4:
                target_gold = 40
            else:
                target_gold = 30

            diff = gold - target_gold
            if diff > 0:
                bonus = min(1.0, diff / (target_gold * 0.5))
                reward += bonus
            else:
                penalty = max(-2.0, diff / (target_gold * 0.3))
                reward += penalty

            if gold > 55:
                excess = (gold - 55) / 30
                reward -= min(1.0, excess)

            # Bônus por gold alto com board estável
            if gold >= 50 and board_stable:
                reward += 0.8
            
            # Penalidade forte por gold alto e board fraco
            if not board_stable and gold > 40:
                reward -= 2.0   # aumentado de -0.8
            
            # Removido o bônus de streak (era inútil)
            # (opcional: manter um controle simples, mas sem recompensa)

        elif self.strategy == Strategy.SLOWROLL:
            gold = self.gold
            level = self.level
            target_level = 6
            low_cost_units = sum(1 for row in self.board for u in row if u and u.get("cost", 1) <= 2)
            if low_cost_units >= 4 and stage <= 4:
                target_level = 5

            if 50 <= gold <= 70:
                reward += 1.0
            elif gold > 70:
                excess = (gold - 70) / 30
                reward -= min(1.0, excess)
            elif gold < 50:
                reward -= 1.5
            elif gold < 40:
                reward -= 2.0

            if gold > 60 and self.reroll_count_this_round > 0:
                reward += 0.3 * min(3, self.reroll_count_this_round)

            # Penalidade maior por nível errado
            if level == target_level:
                reward += 1.5
            elif level > target_level + 1:
                reward -= 3.0
            elif level > target_level:
                reward -= 1.5   # antes -0.5

            # Bônus por upgrades (apenas para unidades de qualidade)
            pairs = 0
            almost_3 = 0
            for (uid, star), count in self.unit_counts.items():
                # Verifica se a unidade é boa (impacto alto) – simplificado: usa comp_score ou custo
                # Pega uma unidade de exemplo para avaliar qualidade
                unit_example = None
                for u in self._get_all_units():
                    if u["id"] == uid and u["star"] == star:
                        unit_example = u
                        break
                if unit_example is not None:
                    impact = self._get_unit_board_impact(unit_example)
                    if impact < 0.4 and star == 1:
                        continue   # ignora lixo
                if star == 1 and count >= 2:
                    pairs += 1
                    if count >= 3:
                        almost_3 += 1
                elif star == 2 and count >= 2:
                    almost_3 += 1

            reward += pairs * 0.4
            reward += almost_3 * 1.2

            three_star_count = sum(1 for row in self.board for u in row if u and u["star"] >= 3)
            reward += three_star_count * 5.0

            if not hasattr(self, 'slowroll_no_upgrade_counter'):
                self.slowroll_no_upgrade_counter = 0
            if pairs == 0 and almost_3 == 0 and three_star_count == 0:
                self.slowroll_no_upgrade_counter += 1
                reward -= min(3.0, self.slowroll_no_upgrade_counter * 0.3)
            else:
                self.slowroll_no_upgrade_counter = max(0, self.slowroll_no_upgrade_counter - 1)

            # Penalidade extra por bench cheio durante SLOWROLL
            bench_count = sum(1 for u in self.bench if u)
            if bench_count >= 7:
                reward -= 1.0
            elif bench_count >= 5:
                reward -= 0.4

            if stage in (3, 4) and level <= 6:
                reward += 0.5

        elif self.strategy == Strategy.STABILIZE:
            gold = self.gold
            board_power = self._get_board_power_cached()
            avg_power = self._get_avg_board_power()
            power_ratio = board_power / (avg_power + 1e-6)
            hp = self.hp

            # Gasto inteligente: bônus decaente (evita incentivar board fraco)
            if power_ratio < 0.85:
                reward += 0.8   # antes 1.5
                if self.turn_spend_count > 0:
                    reward += 0.5
            elif power_ratio < 0.95:
                reward += 0.4   # antes 0.5
            elif power_ratio > 1.05:
                reward -= 0.5

            if gold < 20:
                reward -= 2.0   # antes -1.0
            elif gold < 30:
                reward -= 0.5   # antes -0.3

            # Upgrades imediatos: valor maior
            near_upgrade = 0
            for (uid, star), count in self.unit_counts.items():
                if star == 1 and count == 2:
                    near_upgrade += 1
                elif star == 2 and count == 2:
                    near_upgrade += 2
            reward += near_upgrade * 0.8   # antes 0.4

            if hp < 50:
                reward += 1.0
            elif hp < 35:
                reward += 2.0

            if hasattr(self, 'last_board_power'):
                if self._get_board_power_cached() <= self.last_board_power * 1.02:
                    reward -= 0.8   # antes -0.5
            self.last_board_power = self._get_board_power_cached()

        elif self.strategy == Strategy.ALL_IN:
            gold = self.gold
            hp = self.hp
            board_power = self._get_board_power_cached()
            avg_power = self._get_avg_board_power()
            power_ratio = board_power / (avg_power + 1e-6)
            stage, _ = self._get_stage_info()

            spent = self.turn_gold_spent
            reward += min(2.0, spent * 0.1)

            # Penalidades por guardar gold suavizadas
            if gold > 15:
                reward -= 1.0   # antes -1.5
            elif gold > 5:
                reward -= 0.3   # antes -0.5

            if power_ratio > 0.95:
                reward += 1.5
            elif power_ratio > 1.05:
                reward += 2.5

            if hp < 25:
                reward += 2.0
            elif hp < 40:
                reward += 1.0

            # Penalidade maior por não rerrollar
            if self.reroll_count_this_round == 0 and gold >= 10:
                reward -= 2.0   # antes -1.0

        elif self.strategy == Strategy.WINSTREAK:
            streak = self.win_streak
            gold = self.gold
            board_power = self._get_board_power_cached()
            avg_power = self._get_avg_board_power()
            power_ratio = board_power / (avg_power + 1e-6)

            reward += min(2.0, streak * 0.3)

            if power_ratio > 1.1:
                reward += 2.0   # antes 1.0
            elif power_ratio < 1.0:
                reward -= 1.5

            # Bônus por gastar para manter a streak
            if self.turn_gold_spent > 0:
                reward += 0.3
            # Bônus adicional por gastar acima de 20 gold
            if self.turn_gold_spent > 20:
                reward += 0.5

            if gold > 50 and power_ratio < 1.05:
                reward -= 1.0

            if hasattr(self, 'last_win_streak'):
                if self.last_win_streak > 2 and streak == 0:
                    reward -= 3.0
            self.last_win_streak = streak

        elif self.strategy == Strategy.LOSS_STREAK:
            streak = self.lose_streak
            gold = self.gold
            stage, _ = self._get_stage_info()
            board_power = self._get_board_power_cached()
            avg_power = self._get_avg_board_power()
            power_ratio = board_power / (avg_power + 1e-6)

            if streak >= 2:
                reward += min(2.0, streak * 0.25)

            if gold >= 50:
                reward += 1.5
            elif gold >= 40:
                reward += 0.5
            elif gold < 30:
                reward -= 1.0

            # Penalidade maior por board forte
            if power_ratio > 0.95:
                reward -= 4.0   # antes -2.0
            elif self.turn_gold_spent > 5:
                reward -= 1.0

            if self.reroll_count_this_round > 0:
                reward -= 1.5
            if self.xp_bought_this_round > 0:
                reward -= 2.0

            # Recompensa por board fraco apenas se realmente estiver em loss streak
            if power_ratio < 0.6 and streak >= 2:
                reward += 1.0

        return reward
    
    def _combat_reward(self):
       
       # =========================================================
       # ⚔️ COMBATE (SIMULAÇÃO COM BÔNUS TÁTICO INTEGRADO)
       # =========================================================
       combat_result = self._simulate_combat()

       survived_units = combat_result["survived_units"]
       deaths = combat_result["deaths"]
       carry_survived = combat_result["carry_survived"]
       combat_ticks = combat_result["ticks"]
       carries_frontline = combat_result["carries_frontline"]
       frontline_units = combat_result["frontline_units"]
       backline_units = combat_result["backline_units"]
       tanks_frontline = combat_result["tanks_frontline"]
       
       reward = 0

       stage, _ = self._get_stage_info()

       # =========================================================
       # 🏆 WIN / LOSS
       # =========================================================
       if combat_result["win"]:
           reward += 6.0
           self.win_streak += 1
           self.lose_streak = 0
           reward += min(4, survived_units) * 0.2
           if carry_survived:
               reward += 1.0
           else:
               reward -= 1.5
           if combat_ticks <= 6:
               reward += 0.5
       else:
           reward -= 7.0
           hp_loss = int(self.stage_damage_map.get(stage, 10))
           extra_damage = 0
           if carries_frontline > 0:
               extra_damage += carries_frontline
           if tanks_frontline == 0:
               extra_damage += 1
           extra_damage += min(5, deaths // 2)
           self.hp -= max(2, hp_loss + extra_damage)
           self.lose_streak += 1
           self.win_streak = 0
           reward -= carries_frontline * 1.5
           if tanks_frontline == 0:
               reward -= 0.5
           if not carry_survived:
               reward -= 1.0
       
       # =========================================================
       # 🚫 POSITIONING RUIM
       # =========================================================
       if carries_frontline >= 2:
           reward -= 1.0

       if frontline_units == 0 and backline_units > 0:
           reward -= 1.5

       self._last_combat_won = combat_result["win"]
       return reward

    def _reward_board_fill(self):
        # =========================================================
        # 🚫 BOARD PROBLEMS
        # =========================================================
        stage, _ = self._get_stage_info()

        reward = 0.0

        # --- Obtém unidades reais ---
        board_units = [u for row in self.board for u in row if u]
        units_on_board = len(board_units)
        bench_units = [u for u in self.bench if u]   # lista de unidades (não tuplas)

        # --- Bônus/Penalidade por completude do board ---
        if units_on_board == self.level:
            reward += 3
        else:
            missing = self.level - units_on_board
            reward -= missing * 4

        # --- Comparação bench vs board (apenas se ambos tiverem unidades) ---
        if bench_units and board_units:
            best_bench = max(self._get_unit_board_impact(u) for u in bench_units)
            worst_board = min(self._get_unit_board_impact(u) for u in board_units)
            if best_bench > worst_board:
                reward -= 1.5

        # --- Penalidade por board completamente vazio ---
        if units_on_board == 0:
            reward -= 3.0
                # =========================================================
        # 🚫 DUPLICATAS
        # =========================================================
        seen = {}

        for u in board_units:

            key = (u["id"], u["star"])

            seen[key] = seen.get(key, 0) + 1

        for count in seen.values():

            if count > 1:
                reward -= 0.4 * (count - 1)

        if units_on_board < 3 and stage <= 3:
            reward -= (3 - units_on_board) * 2.0

        if stage <= 3:
            high_cost_units = sum(1 for u in board_units if u.get("cost", 1) >= 3)
            reward += high_cost_units * 1.0
        else:
            reward += high_cost_units * 0.3   # ou um valor menor, ex: 0.15
        return reward
    
    def _streak_reward(self):
        if self.win_streak >= 3:
            return 2
        if self.lose_streak >= 3:
            return 1.5 if self.gold >= 30 else -0.7
        return 0.0

    def _level_timing_reward(self):
        stage, round_in_stage = self._get_stage_info()
        reward = 0.0
        
        # Definição dos níveis alvo por estágio (momento ideal)
        # Formato: (stage, round) -> (nível alvo, bônus por estar no nível, penalidade por atraso)
        targets = {
            (2, 1): 4,   # 2-1: level 4
            (3, 2): 6,   # 3-2: level 6 (padrão)
            (4, 1): 7,   # 4-1: level 7 (alguns jogadores sobem para 7 aqui)
            (4, 5): 8,   # 4-5: level 8 (padrão fast 8)
            (5, 1): 8,   # 5-1: level 8 (se não subiu antes)
        }
        
        current_target = None
        current_round_target = None
        for (s, r), target in targets.items():
            if stage == s and round_in_stage >= r:
                # Encontra o alvo mais recente (para rounds posteriores)
                if current_round_target is None or r > current_round_target:
                    current_round_target = r
                    current_target = target
        
        if current_target is not None:
            diff = self.level - current_target
            
            # Bônus por estar no nível correto ou acima (pre-level)
            if diff >= 0:
                # Estar no nível alvo ou acima é bom, mas pre-level tem bônus extra
                if diff == 0:
                    reward += 1.2  # nível exato
                elif diff == 1:
                    reward += 1.8  # pre-level (subiu antes)
                elif diff >= 2:
                    reward += 2.0  # muito cedo (pode ser arriscado, mas recompensa)
            else:
                # Penalidade por atraso (exponencial)
                penalty = abs(diff) * 1.2
                reward -= min(3.0, penalty)
        
        # Bônus adicional por pre-level em momentos específicos (antes do round alvo)
        # Exemplo: subir para level 6 no 3-1 (antes do 3-2)
        pre_level_bonus = 0.0
        if stage == 3 and round_in_stage == 1 and self.level >= 6:
            pre_level_bonus += 1.5  # subiu para 6 antes do 3-2
        if stage == 4 and round_in_stage == 1 and self.level >= 7:
            pre_level_bonus += 2.0  # subiu para 7 antes do 4-1
        if stage == 4 and round_in_stage <= 3 and self.level >= 8:
            pre_level_bonus += 2.5  # subiu para 8 muito cedo (fast 8 agressivo)
        
        reward += pre_level_bonus
        
        # Penalidade por estar com nível muito baixo para o estágio (ex: level 5 no stage 4)
        expected_min_level = {1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 8}
        min_level = expected_min_level.get(stage, 5)
        if self.level < min_level:
            reward -= (min_level - self.level) * 1.0
        
        return reward
    
    def _reward_bench(self):
        reward = 0.0

        bench_units = [u for u in self.bench if u]
        bench_count = len(bench_units)

        # ===== 1. BÔNUS APENAS PARA PARES DE UNIDADES COM IMPACTO POSITIVO =====
        # Ignora completamente lixo
        counts_1 = {}
        counts_2 = {}
        for u in bench_units:
            impact = self._get_unit_board_impact(u)
            if u["star"] == 1:
                if impact < 0.4:  # ignora lixo
                    continue
                counts_1[u["id"]] = counts_1.get(u["id"], 0) + 1
            elif u["star"] == 2:
                if impact < 0.6:  # ignora lixo
                    continue
                counts_2[u["id"]] = counts_2.get(u["id"], 0) + 1

        for count in counts_1.values():
            if count >= 2:
                reward += 0.2 * (count // 2)
        for count in counts_2.values():
            if count >= 2:
                reward += 0.1 * (count // 2)

        # ===== 2. AVALIAÇÃO INDIVIDUAL (sem mudanças) =====
        for u in bench_units:
            impact = self._get_unit_board_impact(u)
            comp_score = self._get_unit_comp_score(u)
            upgrade_value = self._get_upgrade_value(u)

            if upgrade_value > 0:
                reward += 0.5
            if impact > 0.6 or comp_score > 1.2:
                reward += 0.05
            # Penalidade para lixo (ainda mais forte)
            if impact < 0.3 and comp_score < 0.3 and upgrade_value == 0:
                reward -= 0.8   # antes -0.2

        # ===== 3. PENALIDADE POR TEMPO PARADO (MAIS AGRESSIVA) =====
        for i in range(self.max_bench):
            u = self.bench[i]
            if u is None:
                continue
            stay = self.bench_stay_duration[i]
            impact = self._get_unit_board_impact(u)
            if stay >= 2:   # começa a penalizar no segundo round
                if impact < 0.3:
                    # Lixo: penalidade crescente por round (1.5, 3.0, 4.5...)
                    reward -= min(5.0, 1.5 * (stay - 1))
                elif impact < 0.6:
                    reward -= min(2.0, 0.8 * (stay - 1))
                # Unidades boas não são penalizadas por tempo parado

        # ===== 4. PENALIDADE POR DUPLICATAS EXCESSIVAS (>=3) =====
        duplicates = {}
        for u in bench_units:
            key = (u["id"], u["star"])
            duplicates[key] = duplicates.get(key, 0) + 1
        for count in duplicates.values():
            if count >= 3:
                reward -= 1.0 * (count - 2)   # antes -0.4

        # ===== 5. PENALIDADE POR BENCH MUITO CHEIO (MUITO MAIOR) =====
        if bench_count >= 8:
            reward -= 5.0   # antes -1.0
        elif bench_count >= 6:
            reward -= 2.5   # antes -0.4
        elif bench_count >= 4:
            reward -= 0.5   # pequena penalidade para bench moderadamente cheio

        # ===== 6. UNIDADES FORA DA COMP (já existe, ok) =====
        if self.comp_locked:
            for u in bench_units:
                if not self._is_core_unit(u):
                    impact = self._get_unit_board_impact(u)
                    if impact < 0.5:
                        reward -= 0.5   # antes -0.2

        # ===== 7. PENALIDADE EXTRA POR BENCH LOTADO COM LIXO =====
        # Agora muito mais severa
        junk_units = [u for u in bench_units 
                    if self._get_unit_board_impact(u) < 0.4 
                    and self._get_upgrade_value(u) == 0]
        junk_count = len(junk_units)
        if junk_count >= 2:
            # Penalidade exponencial: 2 lixo = -2.0, 3 lixo = -4.0, 4+ = -6.0
            reward -= min(6.0, junk_count * 1.5)
        
        return reward

    def _position_reward(self):
        reward = 0
        pos_score = self._evaluate_board_positioning()
        if pos_score < -0.5:
            reward -= 2.0   # penalidade por posicionamento desastroso
        elif pos_score > 0.6:
            reward += 1.0   # bônus por bom posicionamento
        return reward
            
    def _synergy_rewards(self):
        reward = 0
        self._update_synergy_if_needed()
        active_traits = self.synergy_mgr.active_traits
        stage, _ = self._get_stage_info()

        # Bônus por novas sinergias ativadas neste round
        current_syn_count = len(active_traits)
        last_syn_count = getattr(self, '_last_syn_count', 0)
        if current_syn_count > last_syn_count:
            reward += (current_syn_count - last_syn_count) * 2.0   # 2.0 por cada nova sinergia
        self._last_syn_count = current_syn_count

        if stage <= 3:
            for trait, count in active_traits.items():
                level = self.synergy_mgr.get_trait_level(trait, count)
                if level >= 1:
                    reward += 1.0   # bônus fixo por ter alguma sinergia ativa
                    if level >= 2:
                        reward += 1.5
        return reward

    # =========================================================
    # POWER (COM CACHE)
    # =========================================================
    def _calculate_unit_power(self, unit):
        return unit["cost"] * (1 + unit["star"] * 0.8)

    def _is_board_stable(self):
        power = self._get_board_power_cached()
        expected = self._expected_board_power()
        return power >= expected * 0.9

    def _get_avg_board_power(self):
        board_hash = self._get_board_hash()
        if board_hash not in self._avg_power_cache:
            total = 0.0
            count = 0
            for row in self.board:
                for u in row:
                    if u:
                        total += u.get("power", self._calculate_unit_power(u))
                        count += 1
            self._avg_power_cache[board_hash] = total / max(1, count)
        return self._avg_power_cache[board_hash]

    def _get_board_power_cached(self):
        if self._cache_valid:
            return self._cached_board_power
        self._update_synergy_if_needed()
        power = 0.0
        for row in self.board:
            for u in row:
                if u:
                    power += self._get_unit_comp_score(u)
        self._cached_board_power = power
        self._cache_valid = True
        return power

    def _evaluate_board(self, board):
        board_power = self._get_board_power_from_matrix(board)
        expected = self._expected_board_power()
        ratio = board_power / max(1.0, expected)
        score = 0.0
        if ratio > 1.25:
            score += 0.8
        elif ratio > 1.1:
            score += 0.5
        elif ratio > 0.95:
            score += 0.1
        elif ratio < 0.75:
            score -= 0.8
        elif ratio < 0.9:
            score -= 0.5
        strong_traits = sum(
            1
            for t, count in self.synergy_mgr.active_traits.items()
            if self.synergy_mgr.get_trait_level(t, count) >= 2
        )
        score += min(0.8, strong_traits * 0.15)
        return score

    def _evaluate_current_board(self):
        board_power = self._get_board_power_cached()
        expected = self._expected_board_power()
        ratio = board_power / max(1.0, expected)
        score = 0.0
        if ratio > 1.3:
            score += 1.0
        elif ratio > 1.15:
            score += 0.6
        elif ratio > 1.0:
            score += 0.25
        elif ratio < 0.7:
            score -= 1.0
        elif ratio < 0.9:
            score -= 0.6
        elif ratio < 1.0:
            score -= 0.2
        strong_traits = sum(
            1
            for t, count in self.synergy_mgr.active_traits.items()
            if self.synergy_mgr.get_trait_level(t, count) >= 2
        )
        score += min(0.8, strong_traits * 0.2)
        if hasattr(self, "last_power"):
            delta = board_power - self.last_power
            if delta > 2.0:
                score += 0.4
            elif delta < -1.5:
                score -= 0.5
        if self.hp < 50 and ratio < 1.0:
            score -= 0.25
        if self.hp < 30:
            score -= 0.4
        if self.strategy == Strategy.FAST8 and self.level >= 7:
            score += 0.2
        if self.strategy == Strategy.ECON and self.gold >= 50:
            score += 0.2
        return np.clip(score, -2.0, 2.0)

    def _expected_board_power(self):

        key = (self.round, self.level, self.hp)

        if key in self._expected_power_cache:
            return self._expected_power_cache[key]

        # =========================================================
        # 📈 BASE POR STAGE
        # =========================================================
        stage, _ = self._get_stage_info()

        stage_curve = {1: 6, 2: 14, 3: 26, 4: 42, 5: 65, 6: 90, 7: 120}

        expected = stage_curve.get(stage, 140)

        # =========================================================
        # 📊 LEVEL
        # =========================================================
        expected += self.level * 3.0

        # =========================================================
        # ⭐ STAR QUALITY
        # =========================================================
        two_star = 0
        three_star = 0

        for row in self.board:

            for u in row:

                if not u:
                    continue

                if u["star"] == 2:
                    two_star += 1

                elif u["star"] >= 3:
                    three_star += 1

        expected += two_star * 4.0
        expected += three_star * 10.0

        # =========================================================
        # 🧩 SYNERGY
        # =========================================================
        active_traits = len(self.synergy_mgr.active_traits)

        expected += active_traits * 3.0

        # =========================================================
        # 👥 BOARD SIZE
        # =========================================================
        units = sum(1 for row in self.board for u in row if u)

        expected += units * 2.5

        # =========================================================
        # 🛡️ FRONTLINE
        # =========================================================
        frontline = 0

        for r in range(2):

            for c in range(7):

                if self.board[r][c]:
                    frontline += 1

        expected += min(frontline, 3) * 3.0

        # =========================================================
        # 💾 CACHE
        # =========================================================
        self._expected_power_cache[key] = expected

        return expected

    def _get_board_power_from_matrix(self, board):
        power = 0.0
        for r in range(self.rows):
            for c in range(self.cols):
                unit = board[r][c]
                if unit is None:
                    continue
                power += self._get_unit_comp_score(unit)
        return power
    
    # =========================================================
    # 🧠 COMP DIRECTION (COM REDUÇÃO DE FREQUÊNCIA)
    # =========================================================
    def _update_comp_direction(self):
        # 🧹 executa a cada 2 steps
        self._steps_since_comp_update += 1
        if self._steps_since_comp_update < 2:
            return
        self._steps_since_comp_update = 0

        stage, _ = self._get_stage_info()
        all_units = self._get_all_units()
        if not all_units:
            self.comp_traits = {}
            self.comp_strength = 0.0
            self.comp_locked = False
            return
        if stage <= 2:
            self.comp_locked = False
            self.comp_traits = {}
            self.comp_strength = 0.0
            return

        trait_score = {}
        for u in all_units:
            cost = u.get("cost", 1)
            star = u.get("star", 1)
            base_val = 1.0 + (cost * 0.15) + (star - 1) * 0.5
            offensive_factor = self._get_offensive_factor(u)
            # O peso da unidade na trait é multiplicado pela sua ofensividade
            weighted_val = base_val * offensive_factor
            for trait in u.get("traits", []):
                trait_score[trait] = trait_score.get(trait, 0.0) + weighted_val

        # Bônus para sinergias ativas (também ponderado pela ofensividade média da trait)
        for trait, count in self.synergy_mgr.active_traits.items():
            if trait in trait_score:
                lvl = self.synergy_mgr.get_trait_level(trait, count)
                bonus = lvl * 2.0 + count * 0.3
                # Calcula a ofensividade média das unidades com esta trait
                units_with_trait = [u for u in all_units if trait in u.get("traits", [])]
                if units_with_trait:
                    avg_off = sum(self._get_offensive_factor(u) for u in units_with_trait) / len(units_with_trait)
                    bonus *= avg_off
                trait_score[trait] += bonus

        # Bônus para sinergias quase ativas (sem ponderação, mas mantido)
        for trait, count in self.synergy_mgr.partial_traits.items():
            if trait in trait_score:
                trait_score[trait] += 1.0 + count * 0.2

        for trait, focus in self.comp_focus.items():
            if trait in trait_score:
                trait_score[trait] *= 1.0 + min(0.4, focus * 0.08)

        sorted_traits = sorted(trait_score.items(), key=lambda x: x[1], reverse=True)
        new_comp_traits = {}
        if sorted_traits:
            main_trait, main_value = sorted_traits[0]
            new_comp_traits[main_trait] = main_value * 1.4
            for trait, val in sorted_traits[1:4]:
                if val > main_value * 0.35:
                    new_comp_traits[trait] = val * 0.5

        # Decisão de lock da comp
        if sorted_traits:
            top_trait, top_value = sorted_traits[0]
            second_value = sorted_traits[1][1] if len(sorted_traits) > 1 else 0
            gap = top_value - second_value
            ratio = top_value / (second_value + 1e-5)
            units_count = len(all_units)
            if not self.comp_locked and stage >= 3:
                if units_count >= 6 and (ratio > 1.6 or gap > 2.5):
                    self.comp_locked = True

        if self.comp_locked:
            active_core = sum(1 for t in self.comp_focus if trait_score.get(t, 0) > 2)
            if active_core == 0:
                self.comp_locked = False

        if self.comp_locked and len(self.comp_focus) > 0:
            combined = {}
            for trait, val in self.comp_focus.items():
                combined[trait] = val * 0.6
            for trait, val in trait_score.items():
                combined[trait] = combined.get(trait, 0.0) + val * 0.4
            sorted_combined = sorted(combined.items(), key=lambda x: x[1], reverse=True)
            new_comp_traits = {}
            if sorted_combined:
                main_trait, main_val = sorted_combined[0]
                new_comp_traits[main_trait] = main_val * 1.4
                for trait, val in sorted_combined[1:4]:
                    if val > main_val * 0.35:
                        new_comp_traits[trait] = val * 0.5

        for trait in list(self.comp_focus.keys()):
            self.comp_focus[trait] *= 0.95
            if self.comp_focus[trait] < 0.05:
                del self.comp_focus[trait]

        for trait, value in new_comp_traits.items():
            self.comp_focus[trait] = self.comp_focus.get(trait, 0.0) + value * 0.04
        for trait in self.comp_focus:
            self.comp_focus[trait] = min(self.comp_focus[trait], 5.0)

        if new_comp_traits:
            main_trait = max(new_comp_traits, key=new_comp_traits.get)
            self.comp_focus[main_trait] = self.comp_focus.get(main_trait, 0) + 0.8

        if self.comp_traits:
            overlap = sum(1 for t in new_comp_traits if t in self.comp_traits)
            if overlap == 0 and stage >= 4:
                for trait in self.comp_traits:
                    self.comp_focus[trait] = max(0.1, self.comp_focus.get(trait, 0.0)) * 1.1

        for trait in new_comp_traits:
            new_comp_traits[trait] = min(new_comp_traits[trait], 10.0)

        self.comp_traits = new_comp_traits
        if len(self.comp_traits) > 0:
            self.comp_strength = sum(self.comp_traits.values()) / (len(self.comp_traits) + 1e-5)
        else:
            self.comp_strength = 0.0

    def _should_lock_comp(self):
        stage, _ = self._get_stage_info()

        if self.strategy == Strategy.STABILIZE and hasattr(self, '_stabilize_start_round'):
            if self.round - self._stabilize_start_round >= 3 and self.win_streak == 0:
                return False
        strong_traits = [
            t for t, count in self.synergy_mgr.active_traits.items()
            if self.synergy_mgr.get_trait_level(t, count) >= 2
        ]
        board_power = self._get_board_power_cached()
        avg_power = self._get_avg_board_power()
        board_stable = board_power >= avg_power * 0.9

        # Impedir lock cedo sem ofensividade
        all_units = self._get_all_units()
        has_offensive_synergy = False
        if stage >= 4:
            for trait in strong_traits:
                units_with_trait = [u for u in all_units if trait in u.get("traits", [])]
                if units_with_trait:
                    avg_off = sum(self._get_offensive_factor(u) for u in units_with_trait) / len(units_with_trait)
                    if avg_off > 1.0:
                        has_offensive_synergy = True
                        break
            if not has_offensive_synergy:
                return False

        # Condições de lock: win streak de 3+ ou board forte estável a partir do estágio 4
        if self.win_streak >= 3:
            return True
        if stage >= 4 and board_stable:
            return True
        if stage >= 5:
            return True
        return False

    def _update_comp_focus(self):
        stage, _ = self._get_stage_info()
        decay = 0.88 if stage <= 3 else 0.92

        # 🔥 OTIMIZAÇÃO 1: remover itens com decaimento usando dict comprehension (mais rápido)
        self.comp_focus = {
            t: v * decay for t, v in self.comp_focus.items() if v * decay >= 0.04
        }

        main_trait = None
        if self.comp_traits:
            main_trait = max(self.comp_traits, key=self.comp_traits.get)

        # 🔥 OTIMIZAÇÃO 2: usar .get para evitar verificações repetidas
        active = self.synergy_mgr.active_traits
        partial = self.synergy_mgr.partial_traits
        focus = self.comp_focus

        # Processa traits ativos
        for trait, count in active.items():
            level = self.synergy_mgr.get_trait_level(trait, count)
            base = count * 0.2 + level * 0.9
            if trait == main_trait:
                gain = base * 2.5
            elif trait in self.comp_traits:
                gain = base * 0.9
            else:
                gain = base * 0.25
            if stage <= 2:
                gain *= 0.6
            focus[trait] = focus.get(trait, 0.0) + gain

        # Processa traits parciais
        for trait, count in partial.items():
            base = count * 0.08 + 0.35
            if trait == main_trait:
                gain = base * 1.6
            elif trait in self.comp_traits:
                gain = base * 0.7
            else:
                gain = base * 0.15
            focus[trait] = focus.get(trait, 0.0) + gain

        if self.comp_locked and main_trait:
            focus[main_trait] = focus.get(main_trait, 0.0) * 1.25

        # 🔥 OTIMIZAÇÃO 3: penalidade para traits fracas
        if main_trait:
            main_value = focus.get(main_trait, 0.0)
            # cria lista de traits para remover durante iteração
            for trait in list(focus.keys()):
                if trait == main_trait:
                    continue
                if focus[trait] < main_value * 0.3:
                    focus[trait] *= 0.75

        # Limita tamanho do dicionário (mantém top 5)
        if len(focus) > 5:
            top = sorted(focus.items(), key=lambda x: x[1], reverse=True)[:5]
            focus = dict(top)

        # 🔥 CORREÇÃO DO ERRO: incrementa main_trait com segurança
        if main_trait:
            focus[main_trait] = focus.get(main_trait, 0.0) + 1.2

        # Normalização
        total = sum(focus.values())
        if total > 0:
            norm_factor = 10.0 / total
            for trait in focus:
                focus[trait] = min(focus[trait] * norm_factor, 10.0)

        self.comp_focus = focus

    def _get_offensive_factor(self, unit):
        """Retorna um fator de ofensividade baseado no perfil de combate da unidade."""
        profile = unit.get("combat_profile", {})
        dps = profile.get("dps", 30)
        burst = profile.get("burst", 50)
        # Normalização: dps médio ~60, burst médio ~100
        factor = (dps / 60.0) * 0.7 + (burst / 100.0) * 0.3
        # Limitar entre 0.3 (muito defensivo) e 2.5 (muito ofensivo)
        return max(0.3, min(2.5, factor))

    def _update_synergy_matrix(self, active_traits, won):
        traits_list = list(active_traits.keys())
        for i in range(len(traits_list)):
            for j in range(i+1, len(traits_list)):
                a, b = traits_list[i], traits_list[j]
                key = (a, b) if a < b else (b, a)
                current = self._trait_synergy_matrix.get(key, 1.0)
                delta = 0.05 if won else -0.03
                new_val = max(0.5, min(2.0, current + delta))
                self._trait_synergy_matrix[key] = new_val
    
    def _get_unit_comp_score(self, unit):
        if not unit:
            return 0.0
        uid = unit["uuid"]
        if uid not in self._comp_cache:
            self._comp_cache[uid] = self._compute_unit_comp_score(unit)
        return self._comp_cache[uid]

    # =========================================================
    # STRATEGY 
    # =========================================================
    def _decide_strategy(self):
        s = self._evaluate_game_state()

        gold = s["gold"]
        hp = s["hp"]
        level = s["level"]

        stage, _ = s["stage"]

        board_power = s["board_power"]
        expected_power = s["expected_power"]

        power_diff = board_power - expected_power

        pairs = s["pair_count"]

        # =========================================================
        # DEFAULT
        # =========================================================
        strategy = Strategy.ECON

        # =========================================================
        # 🛡️ STABILIZE
        # =========================================================
        if hp < 45:

            strategy = Strategy.STABILIZE

        elif power_diff < -8:

            strategy = Strategy.STABILIZE

        # =========================================================
        # 🩸 LOSS STREAK
        # =========================================================
        #elif stage <= 3 and hp >= 70 and self.lose_streak >= 3 and gold >= 30:

            #strategy = Strategy.LOSS_STREAK

        # =========================================================
        # 📈 WIN STREAK
        # =========================================================
        elif self.win_streak >= 4 and power_diff >= 5:

            strategy = Strategy.WINSTREAK

        # =========================================================
        # 🎲 SLOWROLL
        # =========================================================
        #elif pairs >= 3 and gold >= 50 and level in [5, 6, 7]:

            #strategy = Strategy.SLOWROLL

        # =========================================================
        # 🚀 FAST8
        # =========================================================
        elif stage >= 3 and gold >= 50 and hp >= 60 and power_diff >= 0:

            strategy = Strategy.FAST8

        # =========================================================
        # 💰 ECON
        # =========================================================
        else:

            strategy = Strategy.ECON

        # =========================================================
        # 🔄 TRACK SWITCH
        # =========================================================
        if self.last_strategy is not None:

            if strategy != self.last_strategy:
                self.strategy_switch_count += 1

        self.last_strategy = strategy
        self.current_strategy = strategy

        return strategy

    def _compute_strategy_confidence(self, strategy, s):
        power_diff = s["board_power"] - s["expected_power"]

        gold = s["gold"]
        hp = s["hp"]
        level = s["level"]

        stage, _ = s["stage"]

        # =========================================================
        # 💰 ECON
        # =========================================================
        if strategy == Strategy.ECON:

            gold_score = min(1.0, gold / 50)
            hp_score = min(1.0, hp / 100)

            return gold_score * 0.65 + hp_score * 0.35

        # =========================================================
        # ⚔️ STABILIZE
        # =========================================================
        elif strategy == Strategy.STABILIZE:

            hp_pressure = 1.0 - min(1.0, hp / 100)

            weak_board = max(0.0, min(1.0, (-power_diff) / 8))

            return hp_pressure * 0.55 + weak_board * 0.45

        # =========================================================
        # 🚀 FAST8
        # =========================================================
        elif strategy == Strategy.FAST8:

            gold_score = min(1.0, gold / 70)
            hp_score = min(1.0, hp / 100)

            power_score = max(0.0, min(1.0, power_diff / 10))

            return gold_score * 0.45 + hp_score * 0.35 + power_score * 0.20

        # =========================================================
        # 🎲 REROLL
        # =========================================================
        elif strategy == Strategy.SLOWROLL:

            pair_score = 1.0 if s["has_pairs"] else 0.0

            econ_ok = min(1.0, gold / 50)

            low_level_bonus = 1.0 if level <= 6 else 0.3

            return pair_score * 0.5 + econ_ok * 0.3 + low_level_bonus * 0.2

        # =========================================================
        # 🔥 WINSTREAK
        # =========================================================
        elif strategy == Strategy.WINSTREAK:

            streak_score = min(1.0, s["win_streak"] / 6)

            hp_score = min(1.0, hp / 100)

            board_score = max(0.0, min(1.0, power_diff / 8))

            return streak_score * 0.45 + hp_score * 0.25 + board_score * 0.30

        # =========================================================
        # 🩸 LOSS_STREAK
        # =========================================================
        elif strategy == Strategy.LOSS_STREAK:

            lose_score = min(1.0, s["lose_streak"] / 6)

            econ_score = min(1.0, gold / 50)

            weak_board = max(0.0, min(1.0, (-power_diff) / 10))

            return lose_score * 0.5 + econ_score * 0.3 + weak_board * 0.2

        return 0.5

    def _update_strategy(self):

        # =========================================================
        # 🔒 LOCK
        # =========================================================
        if self.strategy_lock > 0:
            self.strategy_lock -= 1
            return

        s = self._evaluate_game_state()

        old_strategy = self.strategy

        new_strategy = self._decide_strategy()

        confidence = self._compute_strategy_confidence(new_strategy, s)

        # =========================================================
        # 🧠 HYSTERESIS
        # Evita troca toda hora
        # =========================================================
        switch_threshold = 0.72

        # troca mais fácil em emergência
        if new_strategy == Strategy.STABILIZE:
            switch_threshold = 0.60

        # troca mais difícil pra greed
        elif new_strategy in (Strategy.FAST8, Strategy.LOSS_STREAK):
            switch_threshold = 0.80

        # =========================================================
        # 🔄 TROCA
        # =========================================================
        if new_strategy != old_strategy:

            if confidence >= switch_threshold:

                self.strategy = new_strategy

                self.strategy_switch_count += 1

                self.last_strategy = old_strategy

                # =================================================
                # 🔒 LOCK DINÂMICO
                # =================================================
                if new_strategy == Strategy.STABILIZE:
                    self.strategy_lock = 1
                    self._stabilize_start_round = self.round

                elif new_strategy in (
                    Strategy.FAST8,
                    Strategy.SLOWROLL,
                ):
                    self.strategy_lock = 3

                else:
                    self.strategy_lock = 2

    def _evaluate_game_state(self):

        board_power = self._get_board_power_cached()
        expected_power = self._expected_board_power()

        pair_count = self._count_pairs()

        return {
            "gold": self.gold,
            "hp": self.hp,
            "level": self.level,
            "board_power": board_power,
            "expected_power": expected_power,
            "power_diff": board_power - expected_power,
            "has_pairs": pair_count > 0,
            "pair_count": pair_count,
            "win_streak": self.win_streak,
            "lose_streak": self.lose_streak,
            "stage": self._get_stage_info(),
            "bench_count": sum(1 for u in self.bench if u),
            "units_on_board": sum(1 for row in self.board for u in row if u),
            "avg_board_power": self._get_avg_board_power(),
        }

    def _count_pairs(self):
        # 🧹 agora usa o atributo incremental
        return self._pair_count
    
    # =========================================================
    # 🧠 POSITION (VERSÃO NUMBA)
    # =========================================================
    def _get_neighbors(self, r, c):

        neighbors = []

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:

                if dr == 0 and dc == 0:
                    continue

                nr = r + dr
                nc = c + dc

                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    neighbors.append((nr, nc))

        return neighbors
    
    def _evaluate_unit_placement(self, unit):

        if unit is None:
            return 0.0

        traits = unit.get("traits", [])

        score = 0.0

        # =========================================================
        # 🛡️ TANKS
        # =========================================================

        is_tank = self.combat_profile_mgr.is_tank(unit)

        # =========================================================
        # 🎯 CARRIES
        # =========================================================

        is_carry = self.combat_profile_mgr.is_carry(unit)

        # =========================================================
        # 🗡️ ASSASSINS
        # =========================================================

        is_assassin = self.combat_profile_mgr.is_assassin(unit)

        # =========================================================
        # 📊 BOARD SCAN
        # =========================================================

        frontline_count = 0
        backline_count = 0

        tanks_front = 0

        carries_back = 0

        for r in range(self.rows):

            for c in range(self.cols):

                u = self.board[r][c]

                if not u:
                    continue

                u_traits = u.get("traits", [])

                # frontline
                if r <= 1:
                    frontline_count += 1

                # backline
                if r >= 2:
                    backline_count += 1

                # tanks front
                if r <= 1 and (
                    "Bruiser" in u_traits or "Warden" in u_traits or "Tank" in u_traits
                ):
                    tanks_front += 1

                # carries back
                if r >= 2 and self.combat_profile_mgr.is_tank(u):
                    carries_back += 1

        # =========================================================
        # 🛡️ TANK VALUE
        # =========================================================

        if is_tank:

            if frontline_count < 2:
                score += 0.5

            score += 0.25

        # =========================================================
        # 🎯 CARRY VALUE
        # =========================================================

        if is_carry:

            if carries_back < 2:
                score += 0.4

            # precisa proteção
            if tanks_front >= 1:
                score += 0.3

        # =========================================================
        # 🗡️ ASSASSIN VALUE
        # =========================================================

        if is_assassin:

            # evita frontline assassin
            if frontline_count > 2:
                score -= 0.25

            score += 0.3

        # =========================================================
        # 📈 IMPACTO REAL
        # =========================================================

        score += self._get_unit_board_impact(unit) * 0.25

        return float(score)

    def _evaluate_board_positioning(self):
        # Aumentar o ganho da função Numba para dar mais variação
        raw_score = _positioning_score_numba(self.role_matrix, self.rows, self.cols)
        # Remapear de [-1,1] para [-2,2] aproximadamente
        stage, _ = self._get_stage_info()
        weight = 0.02 if stage <= 2 else (0.05 if stage == 3 else 0.08)
        return np.tanh(raw_score * 0.12) * weight * 2.5

    def _evaluate_positioning_score(self):

        score = 0.0

        board = self.board

        for r in range(4):

            for c in range(7):

                unit = board[r][c]

                if unit is None:
                    continue

                # =====================================================
                # 🧠 UNIT TYPES
                # =====================================================

                is_carry = unit.get("range", 1) >= 4

                is_tank = unit.get("hp", 0) >= 800

                is_assassin = "Assassin" in unit.get("traits", [])

                # =====================================================
                # 🎯 CARRY POSITIONING
                # =====================================================

                if is_carry:

                    # backline reward
                    score += r * 0.8

                    # safer corners
                    if c in (0, 6):
                        score += 0.25

                    # frontline punish
                    if r <= 1:
                        score -= 2.0

                # =====================================================
                # 🛡️ TANK POSITIONING
                # =====================================================

                if is_tank:

                    # frontline reward
                    score += (3 - r) * 0.6

                    # backline punish
                    if r >= 2:
                        score -= 1.0

                # =====================================================
                # 🗡️ ASSASSIN POSITIONING
                # =====================================================

                if is_assassin:

                    # side access reward
                    if c in (0, 6):
                        score += 0.4

                    # frontline jump angle
                    if r <= 1:
                        score += 0.2

                # =====================================================
                # 🧠 PROTECT CARRY
                # =====================================================

                if is_carry:

                    protected = False

                    for rr in range(max(0, r - 1), min(4, r + 2)):

                        for cc in range(max(0, c - 1), min(7, c + 2)):

                            if rr == r and cc == c:
                                continue

                            other = board[rr][cc]

                            if other is None:
                                continue

                            other_is_tank = other.get("hp", 0) >= 800

                            if other_is_tank:

                                protected = True
                                break

                        if protected:
                            break

                    if protected:
                        score += 1.0
                    else:
                        score -= 0.7

        return score
    
    # =========================================================
    # COMP SCORE (VERSÃO CACHEADA)
    # =========================================================
    def _compute_unit_comp_score(self, unit):
        score = 0.0
        traits = unit.get("traits", [])
        score += self.synergy_mgr.get_unit_synergy_bonus(unit, comp_focus=self.comp_focus)

        # Bônus progressivo por completar sinergias
        for trait in traits:
            current_count = self.synergy_mgr.active_traits.get(trait, 0)
            next_milestone = self._get_next_milestone(trait, current_count)
            if next_milestone:
                units_needed = next_milestone - current_count
                if units_needed == 1:
                    score += 5.0  # muito valioso
                elif units_needed == 2:
                    score += 2.5
                else:
                    score += 1.0
            else:
                score += 0.5

        main_trait = None
        if self.comp_traits:
            main_trait = max(self.comp_traits, key=self.comp_traits.get)
        for trait in traits:
            if trait == main_trait:
                score += 3.5
            elif trait in self.comp_traits:
                score += 1.2
            else:
                score -= 0.5

        for trait in traits:
            focus_strength = self.comp_focus.get(trait, 0)
            if focus_strength > 0:
                score += min(3.0, focus_strength * 0.4)
            else:
                score -= 0.1

        same = self._count_unit_copies(unit["id"])
        if same >= 9:
            score += 6.0
        elif same >= 3:
            score += 4.0
        elif same >= 2:
            score += 2.0

        score += (unit.get("star", 1) - 1) * 2.5
        score += unit.get("cost", 1) * 0.5

        if main_trait and main_trait not in traits:
            score -= 1.2
        if self.comp_locked and main_trait and main_trait not in traits:
            score -= 2.0
        return score

    def _compute_unit_board_impact(self, unit):
        combat_power = self._calculate_unit_combat_power(unit)
        score = combat_power * 0.5

        synergy_score = self.synergy_mgr.get_unit_synergy_bonus(unit, comp_focus=self.comp_focus)
        score += synergy_score * 0.6

        for trait in unit.get("traits", []):
            current = self.synergy_mgr.active_traits.get(trait, 0)
            before = self.synergy_mgr.get_trait_level(trait, current)
            after = self.synergy_mgr.get_trait_level(trait, current + 1)
            if after > before:
                score += 1.5 + before * 0.3

        comp_score = self._get_unit_comp_score(unit)
        score += comp_score * 0.25

        state, progress = self._get_upgrade_state(unit)
        if state == "pair":
            score += 1.2 + progress * 2.0
        elif state == "almost_3":
            score += 3.5 + progress * 5.5
        elif state == "done":
            score += 0.5

        units_on_board = sum(1 for r in self.board for u in r if u)
        if units_on_board < self.level:
            score += 1.5

        if comp_score < 0 and synergy_score <= 0 and combat_power < 1.5:
            score -= 3.0

        stage, _ = self._get_stage_info()
        # Estágio 1-3: flexível (multiplicador 0.9), estágio 4+: focado (0.6)
        out_of_comp_mult = 0.9 if stage <= 3 else 0.6

        main_trait = None
        if self.comp_traits:
            main_trait = max(self.comp_traits, key=self.comp_traits.get)
        has_main = main_trait in unit.get("traits", [])
        has_secondary = any(t in self.comp_traits for t in unit.get("traits", []))

        if has_main:
            score *= 1.5
        elif has_secondary:
            score *= 1.1
        else:
            score *= out_of_comp_mult

        if synergy_score <= 0 and combat_power < 1.5:
            score -= 2.5

        return math.tanh(score / 5.0) * 4.0

    # =========================================================
    # IMPACTO (VERSÃO CACHEADA)
    # =========================================================
    def _get_unit_board_impact(self, unit):
        if not unit:
            return -1.0
        uid = unit["uuid"]
        if uid not in self._impact_cache:
            self._impact_cache[uid] = self._compute_unit_board_impact(unit)
        return self._impact_cache[uid]

    def _get_simulated_impact(self, unit):
        if not unit:
            return 0.0
        uid = unit["uuid"]
        if uid in self._sim_cache:
            return self._sim_cache[uid]
        best_delta = -999.0
        current_power = self._get_board_power_cached()
        # Testa posições vazias
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] is None:
                    self.board[r][c] = unit
                    self._cache_valid = False
                    new_power = self._get_board_power_cached()
                    delta = new_power - current_power
                    self.board[r][c] = None
                    self._cache_valid = False
                    if delta > best_delta:
                        best_delta = delta
        # Testa substituir a unidade mais fraca do board
        board_units = [(r, c, u) for r in range(self.rows) for c in range(self.cols) if (u := self.board[r][c])]
        if board_units:
            worst = min(board_units, key=lambda x: self._get_unit_comp_score(x[2]))
            r, c, old_unit = worst
            original = self.board[r][c]
            self.board[r][c] = unit
            self._cache_valid = False
            new_power = self._get_board_power_cached()
            delta = new_power - current_power
            self.board[r][c] = original
            self._cache_valid = False
            if delta > best_delta:
                best_delta = delta
        self._sim_cache[uid] = math.tanh(best_delta * 0.05)
        return self._sim_cache[uid]

    def _calculate_unit_combat_power(self, unit):
        """Retorna poder de combate realista usando perfil de combate."""
        profile = unit.get("combat_profile", {})
        hp = profile.get("max_hp", profile.get("hp", 600))
        dps = profile.get("dps", 30)
        attack_interval = profile.get("attack_interval", 1.0)
        armor = profile.get("armor", 0)
        effective_dps = dps * (100.0 / (100.0 + armor))
        combat_power = (hp / 1000.0) * (effective_dps / 50.0) * (1.0 / max(0.5, attack_interval))
        star_mult = {1: 1, 2: 3, 3: 9}.get(unit.get("star", 1), 1)
        cost_mult = unit.get("cost", 1) ** 0.7
        return combat_power * star_mult * cost_mult
    
    # =========================================================
    # UPGRADE (VERSÃO OTIMIZADA)
    # =========================================================
    def _get_upgrade_state(self, unit):
        # 🧹 usando unit_counts para evitar varrer todas as unidades
        total_copies = 0
        for star in (1, 2, 3):
            count = self.unit_counts.get((unit["id"], star), 0)
            total_copies += count * (3**(star-1))
        if total_copies < 3:
            return "pair", total_copies / 3.0
        elif total_copies < 9:
            return "almost_3", (total_copies - 3) / 6.0
        else:
            return "done", 1.0

    def _unit_star_to_copies(self, star):
        return {1: 1, 2: 3, 3: 9}.get(star, 1)

    def _upgrade_unit(self, uid, star, extra_unit=None):
        self._cache_valid = False

        # Número de cópias a remover (3 para qualquer upgrade)
        to_remove = 3
        removed = 0
        removed_units = []

        # 1. Remover do bench (índices e unidades)
        bench_items = [(i, u) for i, u in enumerate(self.bench) if u]
        for idx, u in bench_items:
            if removed >= to_remove:
                break
            if u["id"] == uid and u["star"] == star:
                self.bench[idx] = None
                removed_units.append(u)
                removed += 1

        # 2. Remover do board
        if removed < to_remove:
            board_items = [
                (r, c, self.board[r][c])
                for r in range(self.rows)
                for c in range(self.cols)
                if self.board[r][c]
            ]
            for r, c, u in board_items:
                if removed >= to_remove:
                    break
                if u["id"] == uid and u["star"] == star:
                    self.board[r][c] = None
                    removed_units.append(u)
                    removed += 1

        # 3. Se fornecido, remover o extra_unit (unidade da loja)
        if extra_unit is not None and removed < to_remove:
            # Não precisa remover de lugar nenhum, apenas contar como uma cópia
            removed_units.append(extra_unit)
            removed += 1

        # Se não conseguiu remover 3 cópias, algo errado (não deveria acontecer)
        if removed < to_remove:
            # Fallback: tenta remover mais uma vez do bench/board (pode ter havido race condition)
            for idx, u in bench_items:
                if removed >= to_remove:
                    break
                if u["id"] == uid and u["star"] == star and u not in removed_units:
                    self.bench[idx] = None
                    removed_units.append(u)
                    removed += 1
            if removed < to_remove:
                for r, c, u in board_items:
                    if removed >= to_remove:
                        break
                    if u["id"] == uid and u["star"] == star and u not in removed_units:
                        self.board[r][c] = None
                        removed_units.append(u)
                        removed += 1

        # Atualiza unit_counts (remover as cópias)
        for u in removed_units:
            key = (u["id"], u["star"])
            if key in self.unit_counts:
                self.unit_counts[key] -= 1
                if self.unit_counts[key] <= 0:
                    del self.unit_counts[key]
            # 🧹 atualiza pair_count para cada remoção
            self._update_pair_count_remove(u)

        # --- FASE 2: CRIAR A NOVA UNIDADE ---
        champ_base = (
            self.champions[uid]
            if isinstance(uid, int)
            else next((c for c in self.champions if c["id"] == uid), None)
        )
        if champ_base is None:
            # Fallback: usar o primeiro campeão com mesmo nome
            name = removed_units[0]["name"] if removed_units else "Unknown"
            champ_base = next(
                (c for c in self.champions if c["name"] == name), self.champions[0]
            )
        new_unit = self._create_unit(champ_base)
        new_unit["star"] = star + 1

        # --- FASE 3: ESCOLHER LOCAL (board com prioridade se houver espaço) ---
        current_board_units = sum(1 for row in self.board for u in row if u)
        placed = False

        if current_board_units < self.level:
            # Tenta colocar no board
            for r in range(self.rows):
                for c in range(self.cols):
                    if self.board[r][c] is None:
                        self.board[r][c] = new_unit
                        placed = True
                        break
                if placed:
                    break

        if not placed:
            # Tenta colocar no bench
            for i in range(len(self.bench)):
                if self.bench[i] is None:
                    self.bench[i] = new_unit
                    placed = True
                    break

        # Se não há espaço no bench (deveria haver, pois removemos três), falha segura
        if not placed:
            # Fallback: coloca no board forçado (remove a unidade mais fraca se necessário)
            for r in range(self.rows):
                for c in range(self.cols):
                    if self.board[r][c] is None:
                        self.board[r][c] = new_unit
                        placed = True
                        break
                if placed:
                    break
            if not placed:
                # Último recurso: substitui a primeira unidade do board
                for r in range(self.rows):
                    for c in range(self.cols):
                        if self.board[r][c] is not None:
                            self.board[r][c] = new_unit
                            placed = True
                            break
                    if placed:
                        break

        # Atualiza unit_counts com a nova unidade
        new_key = (new_unit["id"], new_unit["star"])
        self.unit_counts[new_key] = self.unit_counts.get(new_key, 0) + 1
        # 🧹 atualiza pair_count para a nova unidade
        self._update_pair_count_add(new_unit)

        # Recompensa (escalonada pelo custo da unidade)
        reward = 0.0
        cost_mult = new_unit.get("cost", 1) * 0.3
        if new_unit["star"] == 2:
            if (uid, star + 1) not in self.upgraded_units:
                self.upgraded_units.add((uid, star + 1))
                reward += 2.0 + cost_mult
        elif new_unit["star"] == 3:
            stage, _ = self._get_stage_info()
            if stage < 4:
                reward -= 0.5
            reward += 5.0 + cost_mult * 2

        self._update_synergy_if_needed()
        self._invalidate_unit_caches()
        return reward
    
    # =========================================================
    # FIND BEST SWAP (OTIMIZADO)
    # =========================================================
    def _find_best_swap(self, top_k=2):
        bench_units = [(i, u) for i, u in enumerate(self.bench) if u]
        board_units = [
            (r, c, u)
            for r in range(self.rows)
            for c in range(self.cols)
            if (u := self.board[r][c])
        ]
        if not bench_units or not board_units:
            return None
        bench_scores = [(i, u, self._get_unit_board_impact(u)) for i, u in bench_units]
        board_scores = [
            (r, c, u, self._get_unit_board_impact(u)) for r, c, u in board_units
        ]
        top_bench = sorted(bench_scores, key=lambda x: x[2], reverse=True)[:top_k]
        worst_board = sorted(board_scores, key=lambda x: x[3])[:top_k]
        base_score = self._evaluate_current_board()
        best = None
        best_gain = -1e9
        for b_idx, b_unit, b_score in top_bench:
            for r, c, f_unit, f_score in worst_board:
                if f_unit and b_unit["uuid"] == f_unit["uuid"]:
                    continue
                raw_gain = b_score - f_score
                if raw_gain < 0.05:
                    continue
                original = self.board[r][c]
                self.board[r][c] = b_unit
                self._cache_valid = False
                sim_score = self._evaluate_board(self.board)
                delta = sim_score - base_score
                self.board[r][c] = original
                self._cache_valid = False
                final_gain = delta * 1.2 + raw_gain * 0.3
                if final_gain > best_gain:
                    best_gain = final_gain
                    best = {"bench_idx": b_idx, "row": r, "col": c, "gain": final_gain}
        if best is None or best_gain < 0.08:
            return None
        return best

    def _best_swap_to_action(self, swap):
        if swap is None:
            return None
        b = swap["bench_idx"]
        r = swap["row"]
        c = swap["col"]
        action = 7 + (b * 28 + r * 7 + c)
        return action if 7 <= action <= 258 else None

    # =========================================================
    # STATE (ADVANCED)
    # =========================================================
    def _get_state(self):

        self._update_synergy_if_needed()

        current_stage, round_in_stage = self._get_stage_info()

        # =====================================================
        # 📊 BOARD
        # =====================================================
        units_board = sum(1 for u in self.board if u)
        units_on_board = [u for u in self.bench if u]
        free_slots = self.level - units_board

        bench_count = sum(1 for u in self.bench if u)

        total_power = sum(self._calculate_unit_power(u) for u in units_on_board)

        board_unit_count = len(units_on_board) / max(1, self.level)

        bench_strength = math.tanh(self._get_bench_strength() / 20.0)  # 🧹 math.tanh

        # =====================================================
        # 📈 STREAKS
        # =====================================================
        win_streak = min(self.win_streak, 10) / 10.0

        lose_streak = min(self.lose_streak, 10) / 10.0

        # =====================================================
        # 🧠 STRATEGY VECTOR
        # =====================================================
        NUM_STRATEGIES = len(Strategy)

        strategy_vec = [0.0] * NUM_STRATEGIES

        strategy_idx = int(self.strategy.value)

        if 0 <= strategy_idx < NUM_STRATEGIES:
            strategy_vec[strategy_idx] = 1.0

        # =====================================================
        # 🧠 STRATEGY FEATURES
        # =====================================================
        is_econ = 1.0 if self.strategy == Strategy.ECON else 0.0

        is_aggressive = (
            1.0 if self.strategy in [Strategy.STABILIZE, Strategy.ALL_IN] else 0.0
        )

        is_greed = (
            1.0
            if self.strategy in [Strategy.ECON, Strategy.FAST8, Strategy.LOSS_STREAK]
            else 0.0
        )

        is_reroll = 1.0 if (self.strategy == Strategy.SLOWROLL) else 0.0

        strategy_switches = min(self.strategy_switch_count, 20) / 20.0

        # =====================================================
        # 📊 POWER DELTA
        # =====================================================
        expected_power = self._expected_board_power()

        power_delta = np.clip((total_power - expected_power) / 20.0, -1.0, 1.0)

        # =====================================================
        # 📦 BASE STATE
        # =====================================================
        state = [
            # =========================
            # CORE
            # =========================
            self.gold / 100,
            self.hp / 100,
            self.level / 9,
            self.round / self.max_rounds,
            math.tanh(total_power / 100.0),  # 🧹 math.tanh
            board_unit_count,
            bench_strength,
            win_streak,
            lose_streak,
            power_delta,
            # =========================
            # STRATEGY
            # =========================
            *strategy_vec,
            is_econ,
            is_aggressive,
            is_greed,
            is_reroll,
            strategy_switches,
        ]

        # =====================================================
        # 🧩 BOARD UNITS
        # =====================================================
        for r in range(self.rows):

            for c in range(self.cols):

                u = self.board[r][c]

                if u:

                    impact = math.tanh(self._get_unit_board_impact(u) * 0.3)  # 🧹 math.tanh

                    comp_score = math.tanh(self._get_unit_comp_score(u) * 0.3)  # 🧹 math.tanh

                    role = u.get("role", 0) / 5.0

                    state.extend(
                        [u["cost"] / 5, u["star"] / 3, impact, comp_score, role]
                    )

                else:
                    state.extend([0.0, 0.0, 0.0, 0.0, 0.0])

        # =====================================================
        # 🪑 BENCH
        # =====================================================
        for u in self.bench:

            if u:

                impact = math.tanh(self._get_unit_board_impact(u) * 0.3)  # 🧹 math.tanh

                comp_score = math.tanh(self._get_unit_comp_score(u) * 0.3)  # 🧹 math.tanh

                role = u.get("role", 0) / 5.0

                state.extend([u["cost"] / 5, u["star"] / 3, impact, comp_score, role])

            else:
                state.extend([0.0, 0.0, 0.0, 0.0, 0.0])

        # =====================================================
        # 🛒 SHOP
        # =====================================================
        for u in self.shop:

            if u:

                impact = math.tanh(self._get_unit_board_impact(u) * 0.3)  # 🧹 math.tanh

                comp_score = math.tanh(self._get_unit_comp_score(u) * 0.3)  # 🧹 math.tanh

                sim = self._get_simulated_impact(u)

                role = u.get("role", 0) / 5.0

                state.extend([u["cost"] / 5, impact, comp_score, sim, role])

            else:
                state.extend([0.0, 0.0, 0.0, 0.0, 0.0])


        state.extend(
            [
                current_stage / 7,
                round_in_stage / 7,
                len(units_on_board) / 10,
                sum(1 for u in self.bench if u) / self.max_bench,
                self.reroll_count_this_round / 10,
            ]
        )

        # =====================================================
        # ✨ SYNERGIES
        # =====================================================
        active_vals = list(self.synergy_mgr.active_traits.values())

        for i in range(5):

            state.append(active_vals[i] / 10 if i < len(active_vals) else 0.0)

        position_score = self._evaluate_board_positioning()

        frontline_count = 0
        backline_carries = 0
        protected_carries = 0
        for r in range(self.rows):
            for c in range(self.cols):
                unit = self.board[r][c]
                if unit is None:
                    continue
                if self.combat_profile_mgr.is_tank(unit) and r <= 1:
                    frontline_count += 1
                if self.combat_profile_mgr.is_carry(unit):
                    if r >= 2:
                        backline_carries += 1
                    for nr, nc in self._get_neighbors(r, c):
                        neighbor = self.board[nr][nc]
                        if neighbor and self.combat_profile_mgr.is_tank(neighbor) and nr < r:
                            protected_carries += 1
                            break

        state.extend(
            [
                position_score,
                frontline_count / 4,
                backline_carries / 4,
                protected_carries / 4,
            ]
        )

        trait_vec = [0.0] * len(self._trait_to_idx)
        for trait, count in self.synergy_mgr.active_traits.items():
            if trait in self._trait_to_idx:
                idx = self._trait_to_idx[trait]
                trait_vec[idx] = min(1.0, count / 10.0)  # normalizar
        state.extend(trait_vec)

        state.extend([
            free_slots / 10.0,
            units_board / max(self.level, 1),
        ])

        # =====================================================
        # FINAL
        # =====================================================
        return np.array(state, dtype=np.float32)

    # =========================================================
    # MÉTODOS AUXILIARES
    # =========================================================
    def _get_bench_strength(self):
        strength = 0.0
        for u in self.bench:
            if not u:
                continue
            val = 1.0
            val *= 1 + 0.8 * (u["star"] - 1)
            val *= 1 + 0.3 * u["cost"]
            val += self.synergy_mgr.get_unit_synergy_bonus(u)
            strength += val
        return strength

    def _get_board_hash(self):
        board_state = []
        bench_state = []
        for r in range(self.rows):
            for c in range(self.cols):
                u = self.board[r][c]
                if u:
                    board_state.append((u["name"], u["star"], r, c))
        for u in self.bench:
            if u:
                bench_state.append((u["name"], u["star"]))
        econ_state = (self.gold // 5, self.level)
        board_state = tuple(sorted(board_state))
        bench_state = tuple(sorted(bench_state))
        return (board_state, bench_state, econ_state)

    def _is_valid_unit(self, unit):
        return (
            unit is not None
            and isinstance(unit, dict)
            and unit.get("id") is not None
            and unit.get("cost") is not None
        )  

    def _should_buy_unit(self, unit):
        if not self._is_valid_unit(unit):
            return False
        impact = self._get_unit_board_impact(unit)
        upgrade_value = self._get_upgrade_value(unit)
        bench_units = [u for u in self.bench if u is not None]
        bench_count = len(bench_units)
        max_bench = self.max_bench
        stage, _ = self._get_stage_info()

        if impact < -0.8 and upgrade_value == 0:
            return False

        # Top traits da comp atual
        top_traits = sorted(self.comp_traits, key=self.comp_traits.get, reverse=True)[:3] if self.comp_traits else []
        is_in_top_trait = any(t in unit.get("traits", []) for t in top_traits)

        if bench_count <= 4:
            if stage <= 2:
                return impact >= 0.0 or upgrade_value > 0 or is_in_top_trait
            if upgrade_value > 0:
                return True
            if impact > 0.3:
                return True
            return is_in_top_trait
        if 5 <= bench_count <= 6:
            if upgrade_value > 0:
                return True
            if impact > 0.6:
                return True
            if unit["cost"] >= 3 and is_in_top_trait and impact > 0.2:
                return True
            return False
        if bench_count >= 7:
            if upgrade_value >= 0.6:
                return True
            if impact > 1.2:
                return True
            return False
        if bench_count >= max_bench:
            if upgrade_value >= 0.6:
                return True
            return False
        return False
    
    def _get_upgrade_value(self, unit):
        if not unit:
            return 0.0
        count = self.unit_counts.get((unit["id"], unit["star"]), 0)
        # Precisa de 3 cópias para upgrade
        if count >= 3:
            return 1.0
        if count == 2:
            return 0.6
        if count == 1:
            return 0.2
        return 0.0

    def _is_core_trait(self, unit):
        return any(t in self.comp_traits for t in unit.get("traits", []))

    def _count_copies(self, unit):
        uid = unit["id"]
        star = unit["star"]
        return sum(
            1 for u in self._get_all_units() if u["id"] == uid and u["star"] == star
        )
    
    def _get_unit_copies(self, unit):
        if not unit:
            return 0
        star = unit.get("star", 1)
        return {1: 1, 2: 3, 3: 9}.get(star, 1)

    def _count_unit_copies(self, unit_id):
        total = 0
        for u in self._get_all_units():
            if u["id"] == unit_id:
                total += self._get_unit_copies(u)
        return total

    def _get_free_bench_slot(self):
        for i, u in enumerate(self.bench):
            if u is None:
                return i
        return None

    def _is_core_unit(self, unit):
        for trait in unit.get("traits", []):
            if self.comp_focus.get(trait, 0) > 2.5:
                return True
        return False

    def _rebuild_unit_counts(self):
        self.unit_counts.clear()
        for u in self._get_all_units():
            key = (u["id"], u["star"])
            self.unit_counts[key] = self.unit_counts.get(key, 0) + 1

    def _get_next_milestone(self, trait_name, current_count):
        milestones = self.synergy_mgr.milestones.get(trait_name, [])
        for m in milestones:
            if m > current_count:
                return m
        return None

    # 🧹 NOVOS MÉTODOS PARA CACHE DE UNIDADES E PAIR COUNT
    def _get_all_units(self):
        if not self._all_units_cache:
            units = []
            for row in self.board:
                for u in row:
                    if u:
                        units.append(u)
            for u in self.bench:
                if u:
                    units.append(u)
            self._all_units_cache = units
        return self._all_units_cache

    def _rebuild_pair_count(self):
        """Reconstrói self._pair_count do zero."""
        counts = {}
        for u in self._get_all_units():
            uid = u["id"]
            counts[uid] = counts.get(uid, 0) + 1
        self._pair_count = sum(1 for cnt in counts.values() if cnt == 2)

    def _update_pair_count_add(self, unit):
        """Atualiza pair_count ao adicionar uma unidade."""
        uid = unit["id"]
        current = sum(1 for u in self._get_all_units() if u["id"] == uid)
        if current == 1:
            self._pair_count += 1
        elif current == 2:
            self._pair_count -= 1

    def _update_pair_count_remove(self, unit):
        """Atualiza pair_count ao remover uma unidade."""
        uid = unit["id"]
        # contagem ANTES da remoção (incluindo a própria unidade)
        current = sum(1 for u in self._get_all_units() if u["id"] == uid)
        if current == 2:
            self._pair_count -= 1
        elif current == 3:
            self._pair_count += 1

    def _rebuild_role_matrix(self):
        """Reconstrói a matriz de papéis a partir do board atual."""
        for r in range(self.rows):
            for c in range(self.cols):
                unit = self.board[r][c]
                if unit is None:
                    self.role_matrix[r, c] = 0
                else:
                    role = unit.get("role", UnitRole.FIGHTER)
                    if role == UnitRole.TANK:
                        self.role_matrix[r, c] = 1
                    elif role == UnitRole.CARRY:
                        self.role_matrix[r, c] = 2
                    elif role == UnitRole.ASSASSIN:
                        self.role_matrix[r, c] = 3
                    else:
                        self.role_matrix[r, c] = 4

    def _get_active_traits(self):
        """Conta sinergias apenas do Tabuleiro (Unidades únicas)."""
        traits = {}
        seen_ids = set()
        for row in self.board:
            for u in row:
                if u and u["id"] not in seen_ids:
                    seen_ids.add(u["id"])
                    for t in u["traits"]:
                        traits[t] = traits.get(t, 0) + 1
        return traits

    def _debug_comp(self):
        data = {
            "strategy": self.strategy,
            "direction": [],
            "focus": [],
            "locked": self.comp_locked,
            "strategy_switch_count": self.strategy_switch_count,
        }

        if not self.comp_traits:
            return data

        # 🎯 Direção atual
        top = sorted(self.comp_traits.items(), key=lambda x: x[1], reverse=True)
        data["direction"] = [(t, round(v, 2)) for t, v in top]

        # 🔥 Memória
        focus = sorted(self.comp_focus.items(), key=lambda x: x[1], reverse=True)[:5]
        data["focus"] = [(t, round(v, 2)) for t, v in focus]

        return data

    # =========================================================
    # MÉTODOS DE RESET, CARGA, UTILITÁRIOS
    # =========================================================
    def reset(self):
        self.gold = 0
        self.hp = 100
        self.level = 1
        self.xp = 0
        self.round = 1
        self.board = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.bench = [None for _ in range(self.max_bench)]
        c = random.choice([x for x in self.champions if x["cost"] == 1])
        self.bench[0] = self._create_unit(c)
        self.shop = self._roll_shop()
        self.units_bought_this_round = []
        self.action_count_this_round = 0
        self.move_count = 0
        self._cached_board_power = 0.0
        self.bench_stay_duration = [0] * self.max_bench
        self.last_purchased_id = None
        self.win_streak = 0
        self.lose_streak = 0
        self._update_synergy_if_needed()
        self.useless_move_count = 0
        self.upgraded_units = set()
        self.reroll_count_this_round = 0
        self.comp_traits = {}
        self.comp_strength = 0.0
        self.last_states = []
        self.strategy = Strategy.ECON
        self.strategy_lock = 0
        self.turn_spend_count = 0
        self.turn_gold_spent = 0
        if self.bench[0]:
            key = (self.bench[0]["id"], self.bench[0]["star"])
            self.unit_counts[key] = 1
        for u in self.bench:
            if u:
                key = (u["id"], u["star"])
                self.unit_counts[key] = self.unit_counts.get(key, 0) + 1
        for row in self.board:
            for u in row:
                if u:
                    key = (u["id"], u["star"])
                    self.unit_counts[key] = self.unit_counts.get(key, 0) + 1
        self._invalidate_unit_caches()
        self._rebuild_unit_counts()
        self._expected_power_cache.clear()
        self._avg_power_cache.clear()
        self._last_board_synergy_hash = None
        self.econ_streak = 0
        self.slowroll_no_upgrade_counter = 0
        self._last_bench_swap = None
        self._last_board_swap = None
        self.last_action_key = None
        self.last_action_key_bench = None
        # 🧹 inicializa role_matrix
        self._rebuild_role_matrix()
        # 🧹 reseta contadores de otimização
        self._steps_since_comp_update = 0
        self._pair_count = 0
        self._rebuild_pair_count()
        self._last_syn_count = 0
        self._stabilize_start_round = 0
        self._unit_last_move = {}        # (unit_uuid, board_pos) -> turn
        self._last_bench_action = None   # (bench_slot, board_pos, turn)
        self._last_board_action = None   # (from_pos, to_pos, turn)
        self._last_board_power = 0
        self._last_high_cost_count = 0   # FIX: para reward delta de unidades caras
        self.previous_position_signatures.clear()
        self._last_bench_move_key.clear()
        self._unit_last_move.clear()

        self._last_bench_action = None
        self._last_board_action = None

        self._last_bench_swap = None
        self._last_board_swap = None

        return self._get_state()

    def _load_champions(self, path):
        if not os.path.exists(path):
            return [{"id": 0, "name": "dummy", "cost": 1, "traits": ["none"]}]
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        units = data["units"]
        for unit in units:
            self.combat_profile_mgr.process_unit(unit)
        return units

    def _create_unit(self, champ):
        return {
            "id": (
                self.champions.index(champ) if champ in self.champions else champ["id"]
            ),
            "name": champ["name"],
            "cost": champ["cost"],
            "traits": champ.get("traits", []),
            "star": champ.get("star", 1),
            "uuid": str(uuid.uuid4()),
        }

    def _get_stage_info(self):
        if self.round <= 3:
            return 1, self.round
        adj_round = self.round - 4
        return (adj_round // 7) + 2, (adj_round % 7) + 1

    def _build_trait_index(self):
        all_traits = set()
        for unit in self.champions:
            for t in unit.get("traits", []):
                all_traits.add(t)
        self._trait_to_idx = {t: i for i, t in enumerate(sorted(all_traits))}

    def _roll_shop(self):
        odds = self.shop_odds[self.level]
        shop = []
        for _ in range(5):
            cost = random.choices([1, 2, 3, 4, 5], weights=odds)[0]
            pool = [c for c in self.champions if c["cost"] == cost]
            shop.append(self._create_unit(random.choice(pool)) if pool else None)
        return shop