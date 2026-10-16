# Economia e loja

## EconomyEngine

`cpp/include/lobby/EconomyEngine.hpp` define o estado econômico mutável por jogador: ouro, nível, XP, sequências e decomposição do ouro recebido na rodada. A classe fornece operações de gasto/crédito, juros, bônus de sequência, compra de XP, XP passivo, registro de vitória/derrota, resolução da economia por rodada e valor de venda.

Constantes de contrato no código incluem reroll por 2 de ouro, compra de XP por 4 de ouro que concede 4 XP, 2 XP por rodada, nível máximo 10, teto de juros 5 e 1 ouro por vitória PvP. A lógica detalhada de ouro-base e XP por nível está na implementação C++, não deve ser duplicada em Python.

## ShopEngine e UnitPool

`ShopEngine` possui cinco ofertas por jogador, usa o nível para as odds de custo, retira cópias do estoque global e suporta lock/unlock da loja. `reroll` substitui ofertas; `take_unit` transfere uma oferta para o fluxo de compra e `return_current_shop` devolve ofertas quando necessário.

A tabela de odds é exposta por `odds_by_level()` para testes de equivalência com a configuração anterior. O estoque global é compartilhado pelos jogadores da mesma lobby, portanto uma cópia ofertada/retirada deve ser refletida no pool.

## Fluxo de compra/venda

A engine coordena o pagamento, movimentação entre loja/banco/tabuleiro e devolução ao pool. As máscaras sinalizam previamente ações indisponíveis, mas a engine ainda é responsável por validar e aplicar a ação.

## Testes

- `cpp/tests/test_economy_engine.cpp`
- `cpp/tests/test_shop_engine.cpp`
- `cpp/tests/test_unit_pool.cpp`
- `cpp/tests/test_tft_engine_pool.cpp`

Para o formato das ações, consulte [contratos e dados](contracts-and-data.md).
