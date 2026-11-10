# Baseline de regressão econômica — 2026-11-03

Este arquivo preserva os números da auditoria anterior à correção econômica. Deve ser usado como referência na próxima auditoria; não sobrescrever. Criar um novo relatório de comparação para cada execução posterior.

## Comparação agregada

| Indicador | Auditoria anterior | Auditoria atual (baseline) |
|---|---:|---:|
| PASS enquanto vivos | 229 | 224 |
| PASS com 50+ de ouro | 7 | 17 |
| Compras de XP | 176 | 110 |
| Rerolls | 53 | 99 |
| Compras de unidades | 313 | 520 |
| Vendas | 136 | 311 |
| Movimentos | 306 | 542 |

Interpretação registrada: o total bruto de PASS caiu ligeiramente (-5), mas PASS com 50+ de ouro aumentou de 7 para 17 (+142,9%) e compras de XP caíram de 176 para 110 (-37,5%). O padrão aponta para pior conversão do excedente em progressão, não para aumento absoluto de PASS.

## Casos individuais

| Jogador | Auditoria anterior | Auditoria atual (baseline) |
|---|---|---|
| P2 | 28 gold, nível 8, colocação #2 | 177 gold, nível 7, colocação #3; 11 PASS com 50+ gold |
| P3 | 0 gold, nível 8, colocação #6 | 79 gold, nível 6, colocação #7; 3 PASS com 50+ gold |
| P7 | — | 83 gold, nível 8, colocação #1 (não classificado automaticamente como falha) |

### P2 — sequência de referência

- Em 4-7, estratégia FAST8; loja oferecia Sett, Rubrivira, Kog'Maw, Azir e Rengar.
- Comprou Azir, executou reroll e passou com 57 gold.
- Em 5-3, registro indica nível 5 e 82 gold.
- Em 5-4, PASS com 93 gold; em 5-5, PASS com 105; em 5-6, PASS com 117.
- Saldo final reportado: 177 gold; nível final 7; colocação #3.

### P3 — sequência de referência

- Saldo final reportado: 79 gold; nível 6; colocação #7.
- Na auditoria anterior, terminou com 0 gold e nível 8, colocação #6.

### P7 — controle não conclusivo

- Terminou com 83 gold, nível 8 e colocação #1.
- Manter como caso de controle: ouro sobrando isoladamente não comprova falha quando o tabuleiro vence.

## Recompensas reportadas para P2

| Ação | Recompensa média |
|---|---:|
| BUY | +0.3303 |
| BUY_XP | -0.0131 |
| PASS | -0.0725 |
| REROLL | -0.1340 |
| MOVE_BENCH | -0.1383 |

A leitura original foi que a penalidade de PASS já era aplicada, mas o sinal de BUY_XP não ensinava suficientemente a progressão parcial. Esses valores são médias agregadas da auditoria e não substituem o replay por decisão.

## Metadados das execuções

| Metadado | Auditoria anterior | Auditoria atual (baseline) |
|---|---|---|
| Seed | 20261016 | 20261016 |
| Engine | C++ | C++ |
| Observation dim | 7237 | 7237 |
| Checkpoint SHA-256 (prefixo) | 7ca55b81… | 8e9656ef… |

Os checkpoints são diferentes. Portanto, a mesma seed não isola o efeito do código: as políticas aprendidas também mudaram. Não atribuir a regressão a uma PR de performance sem replay controlado.

## Limitações registradas

- O log .tft contém ações e contexto estratégico, mas não preserva todas as máscaras legais em cada decisão.
- Ainda não foi comprovado que BUY_XP estava legal em absolutamente todos os PASS suspeitos.
- O caso P2 em 5-3 (nível 5, 82 gold) é o principal cenário sintético de regressão para o teste unitário.
- O caso P3 (nível 6, 79 gold) é um segundo cenário de late game com excedente e progressão insuficiente.
- A sequência de movimentos improdutivos (Varus/Kha'Zix/Malphite) fica fora do escopo desta correção econômica inicial.
- A frequência de reroll (53 → 99) também fica registrada para acompanhamento, mas não deve ser alterada nesta PR.

## Critérios para a próxima comparação

Reexecutar com a mesma seed 20261016 e registrar, no mínimo:

1. PASS enquanto vivos e PASS com 50+ gold.
2. BUY_XP, reroll, compras, vendas e movimentos.
3. Ouro e nível finais por jogador, especialmente P2/P3/P7.
4. Estratégia ativa, loja útil, XP atual/necessário e máscara legal em cada PASS de late game.
5. Recompensa média e acumulada de BUY_XP versus PASS.
6. Hash do checkpoint e hash do commit da engine.

Comparar primeiro a engine com o mesmo checkpoint para isolar o efeito do código. Depois, comparar checkpoints treinados com o mesmo protocolo para medir o efeito de aprendizagem.

## Correção implementada nesta branch

- Removido o bloqueio que zerava o sinal de progresso parcial de XP quando havia 60+ gold e o gasto preservava 50.
- O sinal phase-aware passa a ser usado no late game quando há progresso rumo ao nível-alvo.
- O bônus genérico de excedente só é aplicado quando o sinal phase-aware não se aplica, evitando empilhar os dois incentivos.
- SLOWROLL continua sem incentivo genérico de XP; FAST8/STABILIZE só recebem sinal quando há progresso parcial válido e dentro da reserva da fase.
- Correção complementar: PASS com mais de 50 gold é penalizado mesmo sem compra útil na loja e sem XP disponível; a política deve converter o excedente em XP ou reroll conforme a estratégia. Até 50 gold, permanece o comportamento baseado em oportunidade concreta.
- Testes unitários adicionados para os cenários sintéticos P2/P3 e para garantir PASS legítimo sem penalidade.
