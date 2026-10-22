# Auditoria estratégica TFT

- Registros válidos: **3360**
- Jogadores listados: **8**
- Erros de leitura: **0**

> Alertas são indícios para revisão, não prova de que outra ação seria melhor.

## Resumo por jogador

| Jogador | Ativos | Seeds | Movimentos | Passes | Δ ouro médio | Recompensa ação média | Recompensas negativas | Suspeitas de loop | Violações de máscara |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 230 | 1 | 24 | 20 | 0.074 | 0.034 | 97 | 7 | 0 |
| 1 | 420 | 1 | 84 | 28 | 0.031 | 0.027 | 170 | 17 | 0 |
| 2 | 210 | 1 | 67 | 19 | 0.010 | 0.026 | 80 | 18 | 0 |
| 3 | 270 | 1 | 26 | 23 | 0.556 | 0.041 | 108 | 4 | 0 |
| 4 | 410 | 1 | 101 | 43 | 0.088 | 0.023 | 156 | 29 | 0 |
| 5 | 310 | 1 | 37 | 25 | 0.045 | 0.033 | 114 | 8 | 0 |
| 6 | 310 | 1 | 25 | 17 | 0.026 | 0.043 | 95 | 6 | 0 |
| 7 | 420 | 1 | 77 | 20 | 0.105 | 0.034 | 171 | 23 | 0 |

## Detalhes e alertas

### Jogador 0
- Contagem de ações: {'move_bench': 24, 'pass': 20, 'buy': 89, 'reroll': 20, 'other_5': 77}
- Variações de ouro positivas/negativas: 89/102
- Probabilidade média selecionada: 0.461; abaixo de 0,05: 0
- Cabeças com máscara verificável: 444; violações: 0
- Seleções diferentes da opção top-1: 0
- **Possível loop:** seed=11 round=3: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=11 round=3: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 24, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 24, 0, 0)]
- **Possível loop:** seed=11 round=4: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=4: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=5: movimento idêntico 3x: [3, 0, 1, 24, 0, 0]
- **Possível loop:** seed=11 round=5: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=5: padrão alternado em 4 movimentos: [(3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0)]

### Jogador 1
- Contagem de ações: {'move_bench': 84, 'pass': 28, 'buy': 142, 'other_5': 123, 'reroll': 43}
- Variações de ouro positivas/negativas: 147/174
- Probabilidade média selecionada: 0.408; abaixo de 0,05: 0
- Cabeças com máscara verificável: 853; violações: 0
- Seleções diferentes da opção top-1: 0
- **Possível loop:** seed=11 round=3: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=11 round=3: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 24, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 24, 0, 0)]
- **Possível loop:** seed=11 round=9: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=11 round=9: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 24, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 24, 0, 0)]
- **Possível loop:** seed=11 round=10: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=10: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=11: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=11: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=13: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=13: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=14: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=14: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=27: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=27: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=29: movimento idêntico 3x: [3, 0, 5, 17, 0, 0]
- **Possível loop:** seed=11 round=30: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=30: padrão alternado em 4 movimentos: [(3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0)]

### Jogador 2
- Contagem de ações: {'move_bench': 67, 'pass': 19, 'buy': 53, 'reroll': 27, 'other_5': 44}
- Variações de ouro positivas/negativas: 60/75
- Probabilidade média selecionada: 0.409; abaixo de 0,05: 0
- Cabeças com máscara verificável: 441; violações: 0
- Seleções diferentes da opção top-1: 0
- **Possível loop:** seed=11 round=3: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=11 round=3: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 24, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 24, 0, 0)]
- **Possível loop:** seed=11 round=4: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=4: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=5: movimento idêntico 4x: [3, 0, 1, 24, 0, 0]
- **Possível loop:** seed=11 round=5: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=5: padrão alternado em 4 movimentos: [(3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0)]
- **Possível loop:** seed=11 round=6: movimento idêntico 5x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=6: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=7: movimento idêntico 3x: [3, 0, 1, 24, 0, 0]
- **Possível loop:** seed=11 round=7: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=7: padrão alternado em 4 movimentos: [(3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0)]
- **Possível loop:** seed=11 round=8: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=9: movimento idêntico 3x: [3, 0, 1, 24, 0, 0]
- **Possível loop:** seed=11 round=9: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=9: padrão alternado em 4 movimentos: [(3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0)]
- **Possível loop:** seed=11 round=21: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=21: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]

### Jogador 3
- Contagem de ações: {'move_bench': 25, 'pass': 23, 'move_board': 1, 'buy': 113, 'reroll': 8, 'other_5': 100}
- Variações de ouro positivas/negativas: 110/116
- Probabilidade média selecionada: 0.433; abaixo de 0,05: 0
- Cabeças com máscara verificável: 535; violações: 0
- Seleções diferentes da opção top-1: 0
- **Possível loop:** seed=11 round=4: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=4: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=5: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=5: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]

### Jogador 4
- Contagem de ações: {'move_bench': 101, 'pass': 43, 'buy': 118, 'other_5': 104, 'reroll': 44}
- Variações de ouro positivas/negativas: 126/155
- Probabilidade média selecionada: 0.408; abaixo de 0,05: 0
- Cabeças com máscara verificável: 834; violações: 0
- Seleções diferentes da opção top-1: 0
- **Possível loop:** seed=11 round=3: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=3: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=8: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=8: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=9: movimento idêntico 3x: [3, 0, 1, 24, 0, 0]
- **Possível loop:** seed=11 round=9: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=9: padrão alternado em 4 movimentos: [(3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0)]
- **Possível loop:** seed=11 round=10: movimento idêntico 3x: [3, 0, 1, 24, 0, 0]
- **Possível loop:** seed=11 round=10: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=10: padrão alternado em 4 movimentos: [(3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0)]
- **Possível loop:** seed=11 round=13: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=13: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=14: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=14: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=15: movimento idêntico 3x: [3, 0, 1, 24, 0, 0]
- **Possível loop:** seed=11 round=15: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=15: padrão alternado em 4 movimentos: [(3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0)]
- **Possível loop:** seed=11 round=19: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=19: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=23: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=23: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=24: movimento idêntico 3x: [3, 0, 1, 24, 0, 0]
- **Possível loop:** seed=11 round=24: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=24: padrão alternado em 4 movimentos: [(3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0)]
- **Possível loop:** seed=11 round=25: movimento idêntico 3x: [3, 0, 1, 24, 0, 0]
- **Possível loop:** seed=11 round=25: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=25: padrão alternado em 4 movimentos: [(3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0)]
- **Possível loop:** seed=11 round=27: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=27: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]

### Jogador 5
- Contagem de ações: {'move_bench': 37, 'pass': 25, 'buy': 117, 'other_5': 105, 'reroll': 26}
- Variações de ouro positivas/negativas: 121/134
- Probabilidade média selecionada: 0.423; abaixo de 0,05: 0
- Cabeças com máscara verificável: 606; violações: 0
- Seleções diferentes da opção top-1: 0
- **Possível loop:** seed=11 round=3: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=11 round=3: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 24, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 24, 0, 0)]
- **Possível loop:** seed=11 round=9: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=11 round=9: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 24, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 24, 0, 0)]
- **Possível loop:** seed=11 round=18: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=18: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=19: movimento idêntico 5x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=19: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]

### Jogador 6
- Contagem de ações: {'move_bench': 24, 'move_board': 1, 'pass': 17, 'buy': 121, 'reroll': 38, 'other_5': 109}
- Variações de ouro positivas/negativas: 124/150
- Probabilidade média selecionada: 0.461; abaixo de 0,05: 0
- Cabeças com máscara verificável: 590; violações: 0
- Seleções diferentes da opção top-1: 0
- **Possível loop:** seed=11 round=3: movimento idêntico 4x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=11 round=3: movimento idêntico 3x: [3, 0, 0, 24, 0, 0]
- **Possível loop:** seed=11 round=3: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 24, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 24, 0, 0)]
- **Possível loop:** seed=11 round=4: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=4: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=5: padrão alternado em 4 movimentos: [(3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0)]

### Jogador 7
- Contagem de ações: {'move_bench': 77, 'pass': 20, 'buy': 145, 'other_5': 130, 'reroll': 48}
- Variações de ouro positivas/negativas: 146/189
- Probabilidade média selecionada: 0.409; abaixo de 0,05: 0
- Cabeças com máscara verificável: 849; violações: 0
- Seleções diferentes da opção top-1: 0
- **Possível loop:** seed=11 round=3: movimento idêntico 3x: [3, 0, 0, 17, 0, 0]
- **Possível loop:** seed=11 round=3: padrão alternado em 4 movimentos: [(3, 0, 0, 17, 0, 0), (3, 0, 0, 24, 0, 0), (3, 0, 0, 17, 0, 0), (3, 0, 0, 24, 0, 0)]
- **Possível loop:** seed=11 round=5: movimento idêntico 3x: [3, 0, 1, 24, 0, 0]
- **Possível loop:** seed=11 round=5: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=5: padrão alternado em 4 movimentos: [(3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0)]
- **Possível loop:** seed=11 round=6: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=6: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=7: movimento idêntico 3x: [3, 0, 1, 24, 0, 0]
- **Possível loop:** seed=11 round=7: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=7: padrão alternado em 4 movimentos: [(3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0)]
- **Possível loop:** seed=11 round=11: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=11: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]
- **Possível loop:** seed=11 round=12: movimento idêntico 3x: [3, 0, 1, 24, 0, 0]
- **Possível loop:** seed=11 round=12: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=12: padrão alternado em 4 movimentos: [(3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0)]
- **Possível loop:** seed=11 round=13: movimento idêntico 3x: [3, 0, 1, 24, 0, 0]
- **Possível loop:** seed=11 round=13: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=13: padrão alternado em 4 movimentos: [(3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0)]
- **Possível loop:** seed=11 round=14: movimento idêntico 3x: [3, 0, 1, 24, 0, 0]
- **Possível loop:** seed=11 round=14: movimento idêntico 4x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=14: padrão alternado em 4 movimentos: [(3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0)]
- **Possível loop:** seed=11 round=17: movimento idêntico 3x: [3, 0, 1, 17, 0, 0]
- **Possível loop:** seed=11 round=17: padrão alternado em 4 movimentos: [(3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0), (3, 0, 1, 17, 0, 0), (3, 0, 1, 24, 0, 0)]

## Limitações dos dados

- O JSONL registra ação, round, ouro antes/depois, recompensas, máscaras e diagnósticos.
- Não contém snapshot completo de tabuleiro/banco/loja por decisão; não confirma oportunidades reais de 2 estrelas, compras ignoradas ou ganho de posicionamento.
- Não contém comp_direction, comp_focus, traits ativos nem unidades core por registro; não prova que a composição guiou a ação.
- A máscara só pode ser validada quando diagnostics contém mask e selected. Ausência de diagnóstico não conta como violação.
- A variação líquida de ouro não é necessariamente o custo da ação.
- Os rótulos de ações 0–6 são hipóteses; confirme os enums atuais da engine antes de usar as contagens oficialmente.

## Erros de leitura

Nenhum.
