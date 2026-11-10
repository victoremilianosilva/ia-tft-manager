# Currículo de fine-tuning por estratégia

O currículo mantém os dois fine-tunings já executados e remove os cenários antigos ainda não executados. Os novos treinos são focados por comportamento e usam estados naturalmente alcançados pela engine C++; nenhum estado artificial é inventado.

## Ordem obrigatória

| Ordem | ID | Estratégia | Objetivo |
|---:|---|---|---|
| 1 | `critical_hp_high_gold` | Histórico | Preservar o primeiro fine-tuning já executado |
| 2 | `late_game_high_gold_underleveled` | Histórico | Preservar o segundo fine-tuning já executado |
| 3 | `econ_gold_reserve` | ECON | Guardar até 50, comprando pares, upgrades e peças úteis |
| 4 | `econ_surplus_strong_board` | ECON | Com board forte e ouro acima de 50, converter excedente em XP sem quebrar a reserva |
| 5 | `stabilize_weak_board` | STABILIZE | Com board fraco sob pressão, gastar seletivamente em compras, roll melhorado, XP e implantação |
| 6 | `fast8_strong_board` | FAST8 | Combinar economia, board forte e XP; não ativar FAST8 com board fraco |
| 7 | `all_in_emergency` | ALL_IN | Converter recursos em força imediata quando HP estiver crítico |
| 8 | `slowroll_winstreak` | SLOWROLL | Padrão Kha'Zix: buscar cópias/3 estrelas e gastar controladamente para prolongar a winstreak |

## Regras estratégicas

- **ECON:** preservar breakpoints de juros até 50; comprar quando a oferta completar par, upgrade ou tiver fit real. Acima de 50, se o board estiver forte, usar o excedente para XP mantendo pelo menos 50.
- **STABILIZE:** board fraco sob pressão não deve continuar acumulando ouro. Compras úteis e rolls que melhorem as opções podem fortalecer o board; XP é válido quando ajuda a estabilizar, sem virar gasto automático.
- **FAST8:** só é elegível com board forte e plano de composição que peça nível 8. Economia e força do board precisam acompanhar o XP.
- **ALL_IN:** HP crítico autoriza gastar a reserva; compras úteis, roll com melhora real e XP que aumente a capacidade de sobreviver são opções aprendidas, não ações obrigatórias.
- **SLOWROLL:** manter a janela da composição e procurar cópias que completem upgrades. Com winstreak, gastar de forma controlada em XP, compras e implantação para continuar vencendo; não transformar SLOWROLL em fast leveling.
- **LOSS_STREAK:** removida como estratégia ativa. O slot numérico legado permanece reservado para não deslocar IDs usados por checkpoints antigos; a engine não seleciona mais essa estratégia.

## Cobertura e aprovação

Os cenários são encontrados em observações reais. Zero transições significa **não coberto**, nunca aprovação. O treinamento concentra PPO nas transições do cenário selecionado; o reward nativo continua sendo a fonte principal para avaliar compras, força, XP, roll e combate.

Cada cenário exige avaliação pareada e revisão humana. A avaliação automática sempre grava `approved: false`. O próximo cenário só é liberado quando o arquivo de avaliação tiver `approved: true`, o hash SHA-256 corresponder ao checkpoint treinado e `approve_scenario.ps1` registrar a aprovação.

A nova execução de um cenário invalida os cenários posteriores, pois eles dependem da linhagem aprovada anterior. Os dois cenários históricos permanecem no começo da cadeia para preservar seus checkpoints e avaliações.
