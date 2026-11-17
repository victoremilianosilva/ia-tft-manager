# Auditoria de Fine-tuning Econômico

> Documento-base versionável. A auditoria preenchida é gerada após executar
> treinamento, shadow comparison e partidas pareadas. Não preencher resultados
> com valores ilustrativos.

## 1. Identificação do experimento

- Checkpoint original:
- SHA-256:
- Checkpoint fine-tuned:
- SHA-256:
- Seed(s):
- Versão/commit da engine:
- Dimensão de observação:
- Dimensões do action space:
- Atualizações PPO:
- Transições econômicas elegíveis:
- Cenários efetivamente encontrados:

## 2. Resumo executivo

- Resultado econômico:
- Preservação comportamental:
- Generalização:
- Decisão: APROVADO / REPROVADO / INCONCLUSIVO

## 3. Cenários econômicos

| Cenário | Ocorrências | BUY_XP | BUY | ROLL | PASS | Resultado |
|---|---:|---:|---:|---:|---:|---|
| FAST8 estágio 4, nível 6, 60+ ouro | | | | | | |
| FAST8 estágio 4, nível 6, 80+ ouro | | | | | | |
| FAST8 estágio 4, nível 7, 60+ ouro | | | | | | |
| Meio/fim de jogo abaixo do nível-alvo, 60+ ouro | | | | | | |
| HP crítico e 50+ ouro | | | | | | |
| FAST8 com HP baixo e 50+ ouro | | | | | | |
| SLOWROLL com reserva de ouro | | | | | | |
| ALL_IN com 50+ ouro | | | | | | |
| Qualquer estratégia com ouro acima de 50 | | | | | | |
| Oportunidade de compra útil com 50+ ouro | | | | | | |

## 4. Comparação de política no mesmo estado

- Estados shadow comparados:
- Taxa de divergência de ação:
- Jensen-Shannon média da cabeça de tipo:
- Distribuições condicionais disponíveis:
- Estados sem suporte/amostra:

## 5. Preservação das decisões não treinadas

| Família | Original | Fine-tuned | Divergência | Consequência | Classificação |
|---|---:|---:|---:|---|---|
| Compras | | | | | |
| Roll | | | | | |
| Venda | | | | | |
| Banco/tabuleiro | | | | | |
| Itens | | | | | |
| Composição | | | | | |
| Estratégia SLOWROLL | | | | | |
| Estratégia FAST8 | | | | | |
| Outras estratégias | | | | | |

## 6. Partidas completas pareadas

| Seed | Reward original | Reward fine-tuned | Diferença | Ambas concluídas |
|---:|---:|---:|---:|:---:|
| | | | | |

## 7. Regressões e casos para investigação

Para cada caso, anexar seed, jogador, estado, máscaras válidas, ação original,
ação fine-tuned, consequência e evidência bruta.

## 8. Limitações

- Cenários são detectados em estados naturais da engine; não há injeção de
  estado no C++ atual.
- Divergência de tipo não equivale a divergência de todas as distribuições
  condicionais.
- Reward não equivale a colocação. Interpretar ranking apenas quando o schema
  terminal da engine fornecer esse campo.
- Ausência de ocorrência é falta de cobertura, não evidência de preservação.

## 9. Decisão final

- [ ] Ganho econômico comprovado.
- [ ] Preservação das decisões fora do escopo comprovada.
- [ ] Nenhuma regressão grave sem mitigação.
- [ ] Partidas completas pareadas concluídas.
- [ ] Generalização em seeds não usadas no treino.
- [ ] Checkpoint aprovado para uso experimental.

Responsável pela revisão:
Data:
