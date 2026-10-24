# Auditoria ponta a ponta do sistema de itens — Fase 7

A Fase 7 verifica compatibilidade do checkpoint, contrato de máscaras, passagem das seis posições de ação, execução na engine C++ nativa e encerramento de uma partida real. Os relatórios não substituem uma comparação estratégica antes/depois do treinamento.

## Executar com a engine e o checkpoint reais

Na raiz do repositório, depois de compilar o módulo nativo:

\`\`\`bash
python scripts/audit_item_system_e2e.py \
  --checkpoint tft_checkpoint.pt \
  --seed 20261024 \
  --max-steps 5000 \
  --out-dir reports/item_system_phase7
\`\`\`

A saída gera:

- \`audit.json\`: hash SHA-256 do checkpoint, dimensão da observação, migração de compatibilidade, contrato das máscaras, contagem de ações, ações de item, quantidade de eventos nativos, status de partida completa e colocação dos oito jogadores.
- \`trace.jsonl\`: ações enviadas à engine, recompensas, round, eventos retornados e estado \`done\` em cada step.

O comando retorna código diferente de zero se o checkpoint não puder ser carregado, as máscaras não corresponderem ao contrato, uma ação selecionada violar a máscara, as observações ficarem inválidas, a partida exceder o limite de steps ou a engine não expuser colocação para os oito jogadores.

## O que significa compatibilidade

- Checkpoints atuais são carregados com as cabeças de itens presentes.
- Se \`TFTPolicy.load_compatible_state_dict\` precisar migrar um checkpoint antigo, o relatório registra isso. Uma migração bem-sucedida prova compatibilidade de inferência, não que as novas cabeças de item tenham sido treinadas.
- O hash identifica exatamente o arquivo avaliado; guarde também o commit da engine, o catálogo de itens, seed e configuração de treinamento.
- O avaliador exige o conjunto nativo completo de máscaras, inclusive inventário, receitas e alvos de itens. Ausência ou shape diferente falha em vez de ser silenciosamente ignorada.

## Critério de conclusão

Só considerar a execução ponta a ponta aprovada quando \`status=passed\`, \`complete_match=true\`, as oito colocações estiverem presentes e o trace for gerado. Confira \`item_action_counts\`: zero ações de item não prova falha de execução, mas também não prova que equipar/combinar foi exercitado naquela partida. Para provar uso e efeitos estratégicos, use uma seed/cenário em que itens estejam disponíveis e compare checkpoints compatíveis em partidas pareadas.

A auditoria registra as ações de item escolhidas/enviadas e eventos devolvidos pela engine; não declara automaticamente que cada tentativa de item alterou o estado corretamente caso a engine não exponha um evento de sucesso específico. Essa confirmação exige verificar o estado nativo do inventário/equipamento ou adicionar um evento de resultado explícito.
