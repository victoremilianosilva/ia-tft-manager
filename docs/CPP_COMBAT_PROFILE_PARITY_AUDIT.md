# CombatProfileManager — auditoria de paridade C++/Python

## Escopo implementado
O módulo nativo `CombatProfileEngine` reproduz a inferência de papel por palavras-chave da habilidade e atributos, os cinco IDs de papel, o desempate pela ordem `TANK, CARRY, SUPPORT, FIGHTER, ASSASSIN`, flags de frontline/backline, extração de texto de habilidade e o mapeamento de entrada básica de combate. A API está exposta em `tft_engine`: `combat_profile_get_profile`, `combat_profile_get_role`, `combat_profile_is_frontline`, `combat_profile_is_backline` e `combat_profile_build_combat_input`.

## Compatibilidade e limites
- Papel padrão para unidade ausente é `FIGHTER`; `get_role` mantém o fallback para papel inválido na API Python.
- A inferência não usa traits, assim como o Python.
- A API nativa é stateless e não replica o cache mutável por identificador do `CombatProfileManager`. Portanto, alteração dos stats de uma unidade já cacheada continua sendo comportamento Python específico; a paridade dos cálculos é garantida para unidades sem cache prévio.
- A estrutura `CombatInput` já armazena campos de habilidades, itens e traits, mas o loop de `CombatEngine` ainda não os executa como mecânicas ativas. Esta etapa não ativa essas mecânicas; isso é uma migração separada do motor de combate.
- `build_combat_input` continua sendo um conversor de dados básicos, não uma simulação e não inclui habilidades/itens/traits.

## Validação
`tests/test_combat_profile_parity.py` compara inferência, campos de perfil, flags de posicionamento e o dicionário de entrada com a implementação Python. O workflow de paridade executa esse teste com `REQUIRE_CPP_PARITY=1`.
