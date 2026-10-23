# Auditoria estratégica TFT

- Registros válidos: **6000**
- Jogadores listados: **8**
- Erros de leitura: **0**

> Alertas são indícios para revisão, não prova de que outra ação seria melhor.

## Resumo por jogador

| Jogador | Ativos | Seeds | Ações de movimento | Unidades movidas | Passes | Δ ouro médio | Recompensa média | Suspeitas | Ciclos confirmados | Máscara inválida |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 540 | 2 | 108 | 184 | 135 | 0.019 | 0.003 | 14 | 0 | 0 |
| 1 | 660 | 2 | 173 | 317 | 144 | 0.076 | 0.001 | 28 | 0 | 0 |
| 2 | 590 | 2 | 228 | 410 | 116 | 0.007 | 0.001 | 33 | 0 | 0 |
| 3 | 710 | 2 | 267 | 491 | 156 | 0.004 | -0.006 | 57 | 0 | 0 |
| 4 | 540 | 2 | 177 | 319 | 111 | 0.041 | -0.002 | 36 | 0 | 0 |
| 5 | 590 | 2 | 127 | 224 | 184 | 0.027 | 0.004 | 16 | 0 | 0 |
| 6 | 650 | 2 | 185 | 341 | 204 | 0.002 | -0.001 | 33 | 0 | 0 |
| 7 | 600 | 2 | 174 | 315 | 212 | 0.005 | 0.010 | 31 | 0 | 0 |

## Detalhes e alertas

### Jogador 0
- Contagem de ações: {'other_5': 107, 'pass': 135, 'buy': 123, 'move_bench': 83, 'reroll': 67, 'move_board': 25}
- Variações de ouro positivas/negativas: 146/178
- Probabilidade média selecionada: 0.703; abaixo de 0,05: 0
- Cabeças com máscara verificável: 986; violações: 0
- Seleções diferentes da opção top-1: 0
- Movimentos reais de unidade reconstruídos: 184
- Steps com mudança de composição/estratégia: 379
- Ciclos confirmados por retorno ao mesmo estado: 0
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=17: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=17: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=8: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=11: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=14: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=14: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=31: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=31: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=32: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=32: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=32: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=33: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=33: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=33: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]

### Jogador 1
- Contagem de ações: {'other_5': 126, 'pass': 144, 'buy': 142, 'reroll': 75, 'move_bench': 134, 'move_board': 39}
- Variações de ouro positivas/negativas: 179/201
- Probabilidade média selecionada: 0.685; abaixo de 0,05: 0
- Cabeças com máscara verificável: 1274; violações: 0
- Seleções diferentes da opção top-1: 0
- Movimentos reais de unidade reconstruídos: 317
- Steps com mudança de composição/estratégia: 462
- Ciclos confirmados por retorno ao mesmo estado: 0
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=8: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=11: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=21: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=21: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=26: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=26: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=27: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=27: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=28: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=32: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=32: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=33: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=33: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=33: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=35: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=35: movimento idêntico 3x: [3, 0, 0, 4, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=35: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 4, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 4, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=36: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=36: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=2: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=2: movimento idêntico 3x: [3, 0, 0, 6, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=10: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=10: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=11: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=11: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=16: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=16: movimento idêntico 3x: [3, 0, 0, 3, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=16: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]

### Jogador 2
- Contagem de ações: {'other_5': 83, 'pass': 116, 'buy': 102, 'move_bench': 146, 'reroll': 61, 'move_board': 82}
- Variações de ouro positivas/negativas: 131/156
- Probabilidade média selecionada: 0.659; abaixo de 0,05: 0
- Cabeças com máscara verificável: 1231; violações: 0
- Seleções diferentes da opção top-1: 0
- Movimentos reais de unidade reconstruídos: 410
- Steps com mudança de composição/estratégia: 444
- Ciclos confirmados por retorno ao mesmo estado: 0
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=2: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=2: movimento idêntico 3x: [3, 0, 0, 6, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=10: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=10: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=11: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=11: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=16: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=16: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=17: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=17: padrão alternado em 4 movimentos: [(3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=22: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=22: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=23: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=23: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=23: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=24: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=27: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=27: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=31: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=31: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=10: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=10: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=10: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=14: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=14: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=15: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=15: padrão alternado em 4 movimentos: [(3, 0, 0, 2, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 2, 0, 0), (3, 0, 0, 10, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=16: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=17: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=17: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 1, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 1, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=23: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=23: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=23: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]

### Jogador 3
- Contagem de ações: {'other_5': 94, 'pass': 156, 'buy': 115, 'move_bench': 223, 'move_board': 44, 'reroll': 78}
- Variações de ouro positivas/negativas: 159/178
- Probabilidade média selecionada: 0.693; abaixo de 0,05: 0
- Cabeças com máscara verificável: 1453; violações: 0
- Seleções diferentes da opção top-1: 0
- Movimentos reais de unidade reconstruídos: 491
- Steps com mudança de composição/estratégia: 523
- Ciclos confirmados por retorno ao mesmo estado: 0
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=10: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=10: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=10: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=14: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=14: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=15: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=15: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=17: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=17: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=23: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=23: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=24: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=24: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=24: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=26: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=26: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=27: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=28: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=28: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=29: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=29: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 1, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 1, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=30: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=31: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=31: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=34: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=34: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=35: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=35: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 4, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 4, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=36: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=37: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=37: movimento idêntico 3x: [3, 0, 0, 3, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=37: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=38: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=38: movimento idêntico 3x: [3, 0, 0, 3, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=38: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=7: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=7: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=7: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=9: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=9: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=13: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=13: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=16: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=16: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=16: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=22: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=22: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=23: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=23: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 4, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 4, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=24: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=24: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=24: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=25: movimento idêntico 4x: [3, 0, 0, 5, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=25: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=25: padrão alternado em 4 movimentos: [(3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=26: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=26: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]

### Jogador 4
- Contagem de ações: {'other_5': 92, 'pass': 111, 'buy': 108, 'move_bench': 137, 'move_board': 40, 'reroll': 52}
- Variações de ouro positivas/negativas: 133/151
- Probabilidade média selecionada: 0.691; abaixo de 0,05: 0
- Cabeças com máscara verificável: 1094; violações: 0
- Seleções diferentes da opção top-1: 0
- Movimentos reais de unidade reconstruídos: 319
- Steps com mudança de composição/estratégia: 392
- Ciclos confirmados por retorno ao mesmo estado: 0
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=7: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=7: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=7: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=9: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=9: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=13: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=13: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=15: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=15: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=16: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=16: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=24: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=24: movimento idêntico 3x: [3, 0, 0, 3, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=24: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=25: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=25: movimento idêntico 3x: [3, 0, 0, 3, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=25: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=26: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=26: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=28: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=28: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 1, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 1, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=3: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=5: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=5: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 6, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 6, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=20: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=20: movimento idêntico 3x: [3, 0, 0, 3, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=20: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=21: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=21: movimento idêntico 3x: [3, 0, 0, 3, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=21: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=22: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=23: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=23: movimento idêntico 3x: [3, 0, 0, 3, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=23: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=25: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=25: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]

### Jogador 5
- Contagem de ações: {'other_5': 103, 'pass': 184, 'buy': 121, 'move_bench': 93, 'reroll': 55, 'move_board': 34}
- Variações de ouro positivas/negativas: 150/166
- Probabilidade média selecionada: 0.690; abaixo de 0,05: 0
- Cabeças com máscara verificável: 1068; violações: 0
- Seleções diferentes da opção top-1: 0
- Movimentos reais de unidade reconstruídos: 224
- Steps com mudança de composição/estratégia: 380
- Ciclos confirmados por retorno ao mesmo estado: 0
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=3: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=5: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=5: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 6, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 6, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=8: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=8: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=22: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=22: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 4, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 4, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=23: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=26: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=28: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=34: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=34: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=34: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=35: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=35: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=35: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]

### Jogador 6
- Contagem de ações: {'other_5': 86, 'pass': 204, 'buy': 101, 'reroll': 74, 'move_bench': 147, 'move_board': 38}
- Variações de ouro positivas/negativas: 145/166
- Probabilidade média selecionada: 0.697; abaixo de 0,05: 0
- Cabeças com máscara verificável: 1207; violações: 0
- Seleções diferentes da opção top-1: 0
- Movimentos reais de unidade reconstruídos: 341
- Steps com mudança de composição/estratégia: 426
- Ciclos confirmados por retorno ao mesmo estado: 0
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=8: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=8: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=14: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=14: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=17: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=17: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=17: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=18: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=18: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=18: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=22: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=23: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=23: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 1, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 1, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=24: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=24: movimento idêntico 3x: [3, 0, 0, 4, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=24: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 4, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 4, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=25: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=25: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=26: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=28: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=13: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=14: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=14: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 4, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 4, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=15: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=15: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 4, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 4, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=17: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=17: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=18: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=18: movimento idêntico 3x: [3, 0, 0, 3, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=18: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=19: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=19: movimento idêntico 3x: [3, 0, 0, 3, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=19: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]

### Jogador 7
- Contagem de ações: {'other_5': 64, 'pass': 212, 'buy': 85, 'move_bench': 139, 'move_board': 35, 'reroll': 65}
- Variações de ouro positivas/negativas: 116/142
- Probabilidade média selecionada: 0.702; abaixo de 0,05: 0
- Cabeças com máscara verificável: 1097; violações: 0
- Seleções diferentes da opção top-1: 0
- Movimentos reais de unidade reconstruídos: 315
- Steps com mudança de composição/estratégia: 395
- Ciclos confirmados por retorno ao mesmo estado: 0
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=9: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=9: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=11: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=11: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=15: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=17: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=18: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=19: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=21: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 1, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 1, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=24: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=24: movimento idêntico 3x: [3, 0, 0, 3, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261022 round=24: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 3, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=10: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=10: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=15: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=15: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=20: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=20: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=21: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=21: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=21: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=26: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=26: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=28: movimento idêntico 3x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=28: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=32: movimento idêntico 4x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=32: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=32: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=33: movimento idêntico 5x: [3, 0, 0, 10, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=33: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop por padrão de ação (não confirmado):** seed=20261023 round=33: padrão alternado em 4 movimentos: [(3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 10, 0, 0), (3, 0, 0, 17, 0, 0)]

## Limitações dos dados

- O JSONL registra ação, round, ouro antes/depois, recompensas, máscaras e diagnósticos.
- O schema v2 inclui snapshots antes/depois de tabuleiro, banco e loja; identidade da unidade, origem/destino, estratégia e diferenças de composição.
- Ciclo confirmado significa retorno ao mesmo estado de tabuleiro+banco (incluindo UUIDs expostos pela engine), não prova por si só que a ação foi estrategicamente ruim.
- Quando a engine não expõe UUID, o fallback champion/ordinal tem confiança menor e pode não distinguir cópias idênticas.
- A máscara só pode ser validada quando diagnostics contém mask e selected. Ausência de diagnóstico não conta como violação.
- A variação líquida de ouro não é necessariamente o custo da ação.
- Os rótulos de ações 0–6 são hipóteses; confirme os enums atuais da engine antes de usar as contagens oficialmente.

## Erros de leitura

Nenhum.
