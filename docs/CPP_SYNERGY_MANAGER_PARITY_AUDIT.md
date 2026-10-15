# SynergyManager — auditoria de paridade Python/C++

## Fórmulas portadas
- `calculate_multiplier`: soma global de `1.0 + (níveis atingidos ^ 1.8) * 0.20` em termos de bônus, iniciando em 1.0.
- `get_all_multipliers`: retorna multiplicador individual para cada trait configurada.
- `get_trait_level`: conta milestones atingidos, retornando zero para trait desconhecida.
- `get_unit_synergy_bonus`: reproduz bônus ativo, bônus parcial, penalidade fora da composição e multiplicador opcional de `comp_focus`.

## API
A classe nativa `tft_engine.SynergyManagerNative` recebe um mapa trait -> lista de milestones. `set_state(active_traits, partial_traits)` define o snapshot que em Python é mantido por `update(board)`; os métodos de fórmula aceitam os mesmos valores de entrada.

## Escopo e limites
Esta mudança porta as quatro fórmulas solicitadas e testa paridade direta. A montagem de milestones parte dos mesmos valores `effects[].minUnits` que o Python lê de `traits.json`. Não altera o loop de combate nem liga automaticamente esses bônus ao poder das unidades: isso seria uma mudança de semântica do treinamento, separada da migração do gerenciador.
