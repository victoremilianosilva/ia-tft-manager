
# Contrato da API Python ↔ C++ do TFT

Status: interface inicial; motor ainda não implementado.

## Módulo

- Nome: `tft_engine`
- Classe: `tft_engine.TFTLobby(seed=0)`
- Uma instância representa uma lobby de oito jogadores.
- PPO, policy, rollout buffer e checkpoints continuam em Python.

## reset(seed=None)

Retorna um dicionário contendo:

- `observations`: float32, shape `(8, obs_dim)`
- `action_masks`: lista de máscaras dos oito jogadores
- `episode_id`: identificador da partida
- `observation_dim`: dimensão das observações

## step(actions)

Recebe oito ações, cada uma com seis componentes:

1. `type`: 7 opções
2. `shop_slot`: 5 opções
3. `bench_slot`: 9 opções
4. `board_target`: 28 opções
5. `board_source`: 28 opções
6. `board_move_target`: 28 opções

Retorna:

- `observations`: `(8, obs_dim)`
- `rewards`: `(8,)`
- `dones`: `(8,)`
- `lobby_done`: término global da partida
- `action_masks`: máscaras atualizadas
- `info`: rodada e quantidade de jogadores vivos

## Máscaras

- `type_mask`: `(7,)`
- `shop_mask`: `(5,)`
- `bench_source_mask`: `(9,)`
- `board_target_mask`: `(28,)`
- `board_source_mask`: `(28,)`
- `board_move_target_masks`: `(28, 28)`
- `bench_move_source_mask`: `(9,)`
- `bench_to_board_target_masks`: `(9, 28)`

True significa ação válida.

As dimensões e a semântica devem ser confirmadas contra
`Trainer.ACTION_DIMS`, `Trainer.MASK_SHAPES` e `ActionMaskManager`.

## Responsabilidade de vector_lobby_env.py

1. Criar uma instância nativa por lobby.
2. Converter as ações do PPO para a entrada nativa.
3. Agregar as saídas no formato vetorizado atual.
4. Preservar o auto-reset após o término da lobby.
5. Disponibilizar as máscaras ao Trainer.

## Regras

- Não mudar as dimensões da policy durante a migração.
- C++ será responsável pelo estado, regras, recompensas e máscaras.
- O binding deve devolver arrays NumPy próprios.
- Manter o backend Python até passar nos testes de equivalência.
- Validar reset, step, máscaras, recompensas, eliminações, partidas
  completas, seeds e integração com PPO.

## Próximos passos

1. Implementar `cpp/src/TFTLobbyEngine.cpp`.
2. Integrar o módulo ao CMake.
3. Adaptar `vector_lobby_env.py`.
4. Criar testes de equivalência Python/C++.
