# Combate

## Componentes

- `CombatInput.hpp`: contexto do combate, times, unidades, posições, itens, traits, habilidade e modificadores de entrada.
- `CombatEngine.hpp/.cpp`: simula o combate por `CombatEngine::simulate(const CombatInput&)`.
- `CombatResult.hpp`: resultado final e eventos tipados, incluindo ataques, dano, habilidades, movimentação e mortes.
- `CombatProfileEngine.hpp`: calcula/normaliza perfis de role a partir de atributos e pistas do campeão.
- `TFTEngine`: integra o resultado do combate ao ciclo de lobby, HP, vitórias/derrotas, recompensas e eventos públicos.

## Modelo de execução

A engine de combate recebe um snapshot de entrada e devolve um resultado. O lobby é responsável por preparar o contexto correto, aplicar as consequências do resultado à partida e expor o resultado aos consumidores. O viewer usa eventos e snapshots efetivamente retornados; ele não deve inferir frames de combate que a API não expõe.

## Perfis

Os perfis de combate distinguem `TANK`, `CARRY`, `SUPPORT`, `FIGHTER` e `ASSASSIN`. O perfil contém flags de linha de frente/traseira e atributos de combate. O catálogo gerado pode trazer `combat_profile` pré-calculado; o contrato deve permanecer compatível com o formato esperado pela engine.

## Auditoria e paridade

A engine retorna eventos estruturados para permitir testes determinísticos e comparações de resultados. A entrada precisa ser uma fixture explícita para que duas implementações possam ser comparadas no mesmo cenário; comparações de partidas aleatórias não isolam divergências semânticas.

Testes: `cpp/tests/test_combat_engine.cpp`, `tests/test_combat_engine.py`, `tests/test_combat_events.py`, `tests/test_combat_movement.py`, `tests/test_combat_stats.py`, `tests/test_combat_timeout.py`, `tests/test_determinismo_combate_cpp.py` e `tests/test_integracao_combate_cpp.py`.
