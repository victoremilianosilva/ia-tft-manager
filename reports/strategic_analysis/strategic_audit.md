# Auditoria estratégica TFT

- Registros válidos: **5920**
- Jogadores listados: **8**
- Erros de leitura: **0**

> Alertas são indícios para revisão, não prova de que outra ação seria melhor.

## Resumo por jogador

| Jogador | Ativos | Seeds | Movimentos | Passes | Δ ouro médio | Recompensa ação média | Recompensas negativas | Suspeitas de loop | Violações de máscara |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 640 | 2 | 206 | 73 | 0.008 | -0.001 | 373 | 16 | 0 |
| 1 | 610 | 2 | 234 | 125 | 0.044 | 0.001 | 285 | 35 | 0 |
| 2 | 740 | 2 | 313 | 83 | 0.008 | 0.002 | 407 | 32 | 0 |
| 3 | 620 | 2 | 267 | 96 | 0.008 | 0.000 | 322 | 32 | 0 |
| 4 | 550 | 2 | 289 | 128 | 0.033 | -0.007 | 232 | 75 | 0 |
| 5 | 740 | 2 | 191 | 119 | 0.005 | -0.001 | 398 | 11 | 0 |
| 6 | 440 | 2 | 135 | 56 | 0.002 | 0.007 | 235 | 17 | 0 |
| 7 | 490 | 2 | 154 | 80 | 0.014 | 0.006 | 263 | 15 | 0 |

## Detalhes e alertas

### Jogador 0
- Contagem de ações: {'other_5': 139, 'buy': 159, 'move_bench': 99, 'pass': 73, 'move_board': 107, 'reroll': 63}
- Variações de ouro positivas/negativas: 195/211
- Probabilidade média selecionada: 0.649; abaixo de 0,05: 0
- Cabeças com máscara verificável: 1350; violações: 0
- Seleções diferentes da opção top-1: 0
- **Possível loop:** seed=20261022 round=9: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=9: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261022 round=10: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261022 round=16: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=16: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 21, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 21, 0, 0)]
- **Possível loop:** seed=20261022 round=17: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261022 round=26: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=26: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0)]
- **Possível loop:** seed=20261022 round=33: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop:** seed=20261022 round=33: padrão alternado em 4 movimentos: [(3, 0, 0, 5, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261023 round=2: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=2: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261023 round=4: movimento idêntico 4x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=4: movimento idêntico 3x: [3, 0, 0, 21, 0, 0]
- **Possível loop:** seed=20261023 round=4: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 21, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 21, 0, 0)]
- **Possível loop:** seed=20261023 round=7: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]

### Jogador 1
- Contagem de ações: {'move_bench': 174, 'pass': 125, 'buy': 104, 'move_board': 60, 'other_5': 86, 'reroll': 61}
- Variações de ouro positivas/negativas: 139/152
- Probabilidade média selecionada: 0.660; abaixo de 0,05: 0
- Cabeças com máscara verificável: 1268; violações: 0
- Seleções diferentes da opção top-1: 0
- **Possível loop:** seed=20261022 round=21: movimento idêntico 4x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=21: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261022 round=22: movimento idêntico 3x: [3, 0, 0, 0, 0, 0]
- **Possível loop:** seed=20261022 round=22: movimento idêntico 5x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=22: padrão alternado em 4 movimentos: [(3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261022 round=23: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=23: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=24: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=24: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=26: movimento idêntico 4x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=26: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261022 round=33: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop:** seed=20261023 round=5: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=5: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261023 round=7: movimento idêntico 4x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=7: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261023 round=15: movimento idêntico 4x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=15: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop:** seed=20261023 round=15: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop:** seed=20261023 round=16: movimento idêntico 4x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=16: movimento idêntico 4x: [3, 0, 0, 5, 0, 0]
- **Possível loop:** seed=20261023 round=16: padrão alternado em 4 movimentos: [(3, 0, 0, 5, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261023 round=17: movimento idêntico 5x: [3, 0, 0, 5, 0, 0]
- **Possível loop:** seed=20261023 round=17: movimento idêntico 4x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=17: padrão alternado em 4 movimentos: [(3, 0, 0, 5, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261023 round=18: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop:** seed=20261023 round=23: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=24: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop:** seed=20261023 round=24: movimento idêntico 5x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=25: movimento idêntico 5x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=25: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop:** seed=20261023 round=25: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop:** seed=20261023 round=26: movimento idêntico 5x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=26: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop:** seed=20261023 round=26: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 5, 0, 0)]

### Jogador 2
- Contagem de ações: {'other_5': 117, 'buy': 147, 'move_bench': 158, 'pass': 83, 'reroll': 80, 'move_board': 155}
- Variações de ouro positivas/negativas: 181/220
- Probabilidade média selecionada: 0.615; abaixo de 0,05: 0
- Cabeças com máscara verificável: 1630; violações: 0
- Seleções diferentes da opção top-1: 0
- **Possível loop:** seed=20261022 round=5: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=5: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=5: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261022 round=6: movimento idêntico 4x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=6: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=6: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261022 round=7: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=23: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=23: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261022 round=24: movimento idêntico 5x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=24: movimento idêntico 3x: [3, 0, 0, 0, 0, 0]
- **Possível loop:** seed=20261022 round=24: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261022 round=29: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop:** seed=20261022 round=29: padrão alternado em 4 movimentos: [(3, 0, 0, 5, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261022 round=30: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop:** seed=20261022 round=34: movimento idêntico 4x: [3, 0, 0, 5, 0, 0]
- **Possível loop:** seed=20261022 round=34: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=34: padrão alternado em 4 movimentos: [(3, 0, 0, 5, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261023 round=6: movimento idêntico 3x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261023 round=6: padrão alternado em 4 movimentos: [(3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261023 round=8: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=8: movimento idêntico 3x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261023 round=8: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0)]
- **Possível loop:** seed=20261023 round=9: movimento idêntico 4x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261023 round=9: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=9: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0)]
- **Possível loop:** seed=20261023 round=11: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=11: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0)]
- **Possível loop:** seed=20261023 round=21: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=21: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261023 round=37: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=37: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 5, 0, 0)]

### Jogador 3
- Contagem de ações: {'move_bench': 140, 'pass': 96, 'buy': 107, 'reroll': 65, 'move_board': 127, 'other_5': 85}
- Variações de ouro positivas/negativas: 142/164
- Probabilidade média selecionada: 0.623; abaixo de 0,05: 0
- Cabeças com máscara verificável: 1346; violações: 0
- Seleções diferentes da opção top-1: 0
- **Possível loop:** seed=20261022 round=3: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=3: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261022 round=4: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=4: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261022 round=11: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=11: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261022 round=13: movimento idêntico 4x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=13: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261022 round=15: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=15: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261022 round=17: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=17: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 21, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 21, 0, 0)]
- **Possível loop:** seed=20261022 round=22: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=22: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 21, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 21, 0, 0)]
- **Possível loop:** seed=20261022 round=25: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop:** seed=20261023 round=4: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=4: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261023 round=5: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=5: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261023 round=6: movimento idêntico 4x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=6: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261023 round=7: movimento idêntico 3x: [3, 0, 0, 0, 0, 0]
- **Possível loop:** seed=20261023 round=7: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=7: padrão alternado em 4 movimentos: [(3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261023 round=9: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=9: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261023 round=10: movimento idêntico 4x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=10: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=10: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261023 round=22: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=22: movimento idêntico 4x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261023 round=22: padrão alternado em 4 movimentos: [(3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0)]

### Jogador 4
- Contagem de ações: {'move_bench': 286, 'pass': 128, 'reroll': 66, 'buy': 41, 'other_5': 26, 'move_board': 3}
- Variações de ouro positivas/negativas: 77/98
- Probabilidade média selecionada: 0.615; abaixo de 0,05: 0
- Cabeças com máscara verificável: 1195; violações: 0
- Seleções diferentes da opção top-1: 0
- **Possível loop:** seed=20261022 round=6: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=9: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=9: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261022 round=10: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=10: movimento idêntico 5x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=10: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261022 round=15: movimento idêntico 4x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=15: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=15: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261022 round=16: movimento idêntico 4x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=16: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=16: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261022 round=18: movimento idêntico 3x: [3, 0, 1, 0, 0, 0]
- **Possível loop:** seed=20261022 round=18: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=20261022 round=18: padrão alternado em 4 movimentos: [(3, 0, 1, 0, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 0, 0, 0), (3, 0, 1, 17, 0, 0)]
- **Possível loop:** seed=20261022 round=19: movimento idêntico 3x: [3, 0, 1, 0, 0, 0]
- **Possível loop:** seed=20261022 round=19: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=20261022 round=19: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 0, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 0, 0, 0)]
- **Possível loop:** seed=20261022 round=20: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=20261022 round=21: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=21: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 21, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 21, 0, 0)]
- **Possível loop:** seed=20261022 round=22: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=20261022 round=22: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 21, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 21, 0, 0)]
- **Possível loop:** seed=20261022 round=23: movimento idêntico 5x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=20261022 round=23: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 25, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 25, 0, 0)]
- **Possível loop:** seed=20261023 round=7: movimento idêntico 5x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=7: movimento idêntico 3x: [3, 0, 0, 0, 0, 0]
- **Possível loop:** seed=20261023 round=7: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261023 round=14: movimento idêntico 4x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=14: movimento idêntico 3x: [3, 0, 0, 0, 0, 0]
- **Possível loop:** seed=20261023 round=14: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261023 round=15: movimento idêntico 5x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=15: movimento idêntico 3x: [3, 0, 0, 0, 0, 0]
- **Possível loop:** seed=20261023 round=15: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261023 round=16: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=16: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261023 round=17: movimento idêntico 5x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=17: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=17: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261023 round=18: movimento idêntico 5x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=18: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=18: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261023 round=19: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=19: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261023 round=20: movimento idêntico 5x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=20: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=20: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261023 round=21: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=21: movimento idêntico 5x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=21: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261023 round=22: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=22: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261023 round=23: movimento idêntico 4x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261023 round=23: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=23: padrão alternado em 4 movimentos: [(3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261023 round=24: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=24: movimento idêntico 4x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261023 round=24: padrão alternado em 4 movimentos: [(3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261023 round=25: movimento idêntico 5x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=25: movimento idêntico 4x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261023 round=25: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0)]
- **Possível loop:** seed=20261023 round=26: movimento idêntico 5x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261023 round=26: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=26: padrão alternado em 4 movimentos: [(3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261023 round=27: movimento idêntico 4x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261023 round=27: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=27: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0)]
- **Possível loop:** seed=20261023 round=28: movimento idêntico 5x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261023 round=28: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=28: padrão alternado em 4 movimentos: [(3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261023 round=29: movimento idêntico 5x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261023 round=29: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=29: padrão alternado em 4 movimentos: [(3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261023 round=31: movimento idêntico 3x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261023 round=31: padrão alternado em 4 movimentos: [(3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0)]

### Jogador 5
- Contagem de ações: {'move_bench': 89, 'pass': 119, 'buy': 184, 'other_5': 162, 'move_board': 102, 'reroll': 84}
- Variações de ouro positivas/negativas: 223/256
- Probabilidade média selecionada: 0.637; abaixo de 0,05: 0
- Cabeças com máscara verificável: 1468; violações: 0
- Seleções diferentes da opção top-1: 0
- **Possível loop:** seed=20261022 round=3: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=7: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=7: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261022 round=9: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=9: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261022 round=16: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=16: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261023 round=4: movimento idêntico 3x: [3, 0, 0, 5, 0, 0]
- **Possível loop:** seed=20261023 round=4: padrão alternado em 4 movimentos: [(3, 0, 0, 5, 0, 0), (3, 0, 0, 18, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 18, 0, 0)]
- **Possível loop:** seed=20261023 round=5: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=5: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 4, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 4, 0, 0)]

### Jogador 6
- Contagem de ações: {'move_bench': 91, 'pass': 56, 'buy': 111, 'move_board': 44, 'other_5': 92, 'reroll': 46}
- Variações de ouro positivas/negativas: 129/147
- Probabilidade média selecionada: 0.659; abaixo de 0,05: 0
- Cabeças com máscara verificável: 913; violações: 0
- Seleções diferentes da opção top-1: 0
- **Possível loop:** seed=20261022 round=17: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=17: movimento idêntico 3x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261022 round=17: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0)]
- **Possível loop:** seed=20261022 round=21: padrão alternado em 4 movimentos: [(3, 0, 0, 5, 0, 0), (3, 0, 0, 21, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 21, 0, 0)]
- **Possível loop:** seed=20261022 round=22: padrão alternado em 4 movimentos: [(3, 0, 0, 5, 0, 0), (3, 0, 0, 21, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 21, 0, 0)]
- **Possível loop:** seed=20261023 round=3: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261023 round=3: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261023 round=7: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=7: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0)]
- **Possível loop:** seed=20261023 round=10: movimento idêntico 3x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261023 round=11: movimento idêntico 4x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261023 round=11: padrão alternado em 4 movimentos: [(3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261023 round=16: padrão alternado em 4 movimentos: [(3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261023 round=17: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=17: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0)]
- **Possível loop:** seed=20261023 round=21: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=21: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 5, 0, 0)]

### Jogador 7
- Contagem de ações: {'other_5': 96, 'buy': 115, 'move_bench': 91, 'pass': 80, 'reroll': 45, 'move_board': 63}
- Variações de ouro positivas/negativas: 137/151
- Probabilidade média selecionada: 0.670; abaixo de 0,05: 0
- Cabeças com máscara verificável: 1009; violações: 0
- Seleções diferentes da opção top-1: 0
- **Possível loop:** seed=20261022 round=3: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=3: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 0, 0, 0)]
- **Possível loop:** seed=20261022 round=7: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=7: movimento idêntico 3x: [3, 0, 0, 25, 0, 0]
- **Possível loop:** seed=20261022 round=7: padrão alternado em 4 movimentos: [(3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261022 round=8: movimento idêntico 4x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261022 round=8: padrão alternado em 4 movimentos: [(3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261022 round=10: movimento idêntico 3x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261022 round=10: padrão alternado em 4 movimentos: [(3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 17, 0, 0)]
- **Possível loop:** seed=20261022 round=17: movimento idêntico 3x: [3, 0, 0, 26, 0, 0]
- **Possível loop:** seed=20261022 round=17: padrão alternado em 4 movimentos: [(3, 0, 0, 26, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 26, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop:** seed=20261022 round=19: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261022 round=19: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 5, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 5, 0, 0)]
- **Possível loop:** seed=20261023 round=15: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=20261023 round=15: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 25, 0, 0)]

## Limitações dos dados

- O JSONL registra ação, round, ouro antes/depois, recompensas, máscaras e diagnósticos.
- Não contém snapshot completo de tabuleiro/banco/loja por decisão; não confirma oportunidades reais de 2 estrelas, compras ignoradas ou ganho de posicionamento.
- Não contém comp_direction, comp_focus, traits ativos nem unidades core por registro; não prova que a composição guiou a ação.
- A máscara só pode ser validada quando diagnostics contém mask e selected. Ausência de diagnóstico não conta como violação.
- A variação líquida de ouro não é necessariamente o custo da ação.
- Os rótulos de ações 0–6 são hipóteses; confirme os enums atuais da engine antes de usar as contagens oficialmente.

## Erros de leitura

Nenhum.
