# Fine-tuning Econômico Independente — TFT AI

Este diretório mantém o treino normal isolado: não altera `trainer.py`, `policy.py`,
`ppo.py`, `rollout.py` nem `train_cycle.ps1`. A engine C++ recebeu duas correções
estratégicas necessárias aos cenários: persistência/histerese de foco e core,
e classificação de roles consistente entre observação e BoardEvaluation.

## Limitação importante do engine atual

A interface Python/C++ disponível expõe `reset(seed)`, `step()`,
observações, máscaras e snapshots somente de leitura. Ela **não expõe uma API
pública para injetar ouro, HP, nível, estágio, comp e estado do lobby**.

Como o requisito é não alterar o código atual, o gerador não falsifica estados.
Ele identifica os cenários-alvo quando aparecem naturalmente em partidas
simuladas pela engine C++. Cenários que não ocorrerem ficam como "não cobertos"
no relatório. Injeção real de estado exigiria uma API nova na engine e está
fora desta PR.

## Treinamento

Compile a engine C++ como já é necessário para o projeto:

```bash
# PowerShell: escolha exatamente um cenário por execução
.\economy_finetuning\run_finetune.ps1 -Scenario s4_fast8_lvl6_gold60_hp_ok

# Alternativa direta em Python
python economy_finetuning/finetune.py \
  --scenario s4_fast8_lvl6_gold60_hp_ok \
  --checkpoint tft_checkpoint.pt \
  --updates 100 \
  --rollout-steps 512
# O script imprime o caminho exclusivo do checkpoint e da execução.
```

O checkpoint de origem nunca é sobrescrito. Cada execução exige `--scenario`
e aplica shaping somente a esse cenário; os demais são registrados apenas
para monitoramento. As cabeças treináveis dependem do cenário: economia usa `type_head`/`value_head`; vendas usa `sell_head`; implantação usa `bench_head`/`bench_to_board_head`; posicionamento usa `board_source_head`/`board_move_target_head`. Encoder, fusão e cabeças não relacionadas permanecem congeladas. A cabeça de tipo
compartilhada é projetada de volta para uma pequena região L2 ao redor dos
pesos originais a cada update. O shaping é pequeno e condicionado ao
estado/estratégia; SLOWROLL recebe proteção explícita contra incentivo genérico
de XP. O limite de drift pode ser ajustado com `--max-type-head-drift`.

## Cadeia obrigatória e aprovação manual

A ordem dos dez cenários é fixa. O cenário 1 parte do checkpoint original;
cada cenário seguinte parte exclusivamente do checkpoint aprovado do anterior.
O runner bloqueia qualquer etapa cujo predecessor não esteja aprovado. Um
treino concluído é registrado como `trained`, nunca como aprovado.

Depois de revisar a auditoria e a avaliação pareada, crie um JSON de aprovação
com `approved: true` e o SHA-256 exato do checkpoint avaliado. Exemplo:

```json
{
  "approved": true,
  "checkpoint_sha256": "SHA256_DO_CHECKPOINT",
  "summary": {
    "paired_seeds": 20,
    "regression_review": "passed"
  }
}
```

Libere o próximo estágio somente após essa revisão:

```powershell
.\\economy_finetuning\\approve_scenario.ps1 -Scenario critical_hp_high_gold -Evaluation .\\evaluation.json
```

O estado local fica em `economy_finetuning/chain_state.json` (ignorado pelo
Git). A cadeia guarda o hash do checkpoint e da origem, e invalida etapas
posteriores se uma etapa anterior for refeita.

## Avaliação comparativa

O trace gerado durante o treino compara os dois modelos deterministicamente no
mesmo estado e com as mesmas máscaras. A ação estocástica do candidato usada
para coletar PPO é registrada separadamente.

Para avaliar consequências em partidas completas:

```bash
python economy_finetuning/paired_evaluator.py \
  --original tft_checkpoint.pt \
  --finetuned CAMINHO_DO_CHECKPOINT_GERADO.pt \
  --seeds 20261105,20261106,20261107,20261108 \
  --output CAMINHO_DA_EXECUCAO/logs/paired_match_results.jsonl
```

Cada seed executa duas lobbies mistas 4v4: uma com fine-tuned nos assentos pares
e outra com a distribuição espelhada. Isso evita a métrica sem sentido de
colocação média em self-play homogêneo (que tende sempre a 4,5) e permite
comparar original vs. fine-tuned por assento, Top 4 e vitórias. O avaliador
exige hashes iguais da observação e das máscaras iniciais nas duas lobbies.
Registra rewards nativos, contagens de ações, colocação terminal, Top 4, HP,
ouro, nível e métricas atuais do BoardEvaluation. Quatro seeds servem apenas
como smoke test; a aprovação final deve usar pelo menos 20 seeds inéditas,
não usadas no treino.

## Auditoria e visualizador

Instale as dependências opcionais:

```bash
pip install -r economy_finetuning/requirements-viewer.txt
```

Gere o relatório e abra o viewer:

```bash
python economy_finetuning/audit.py \
  --trace CAMINHO_DA_EXECUCAO/logs/decision_trace.jsonl \
  --paired CAMINHO_DA_EXECUCAO/logs/paired_match_results.jsonl \
  --metadata CAMINHO_DA_EXECUCAO/reports/experiment_config.json \
  --summary CAMINHO_DA_EXECUCAO/reports/training_summary.json \
  --output economy_finetuning/reports/ECONOMY_FINETUNING_AUDIT_critical_hp_high_gold.md
streamlit run economy_finetuning/viewer/app.py
```

O visualizador lê JSONL localmente, limita a leitura padrão a 200 mil linhas e
permite filtrar divergências e exportar o subconjunto investigado. Os JSONL,
checkpoints e execuções são dados locais e ficam ignorados pelo Git.

## Cenários implementados

Veja a lista integral em `SCENARIOS.md`. Os cenários são classificados como
treináveis ou monitor-only. O cenário de HP crítico é treinado com reward
nativo, sem bônus artificial para XP; a utilidade de cada oferta continua
sendo avaliada pelo reward/estado real da engine, sem rótulos inventados.

## O que a auditoria consegue provar

- Shadow comparison: original e fine-tuned recebem o mesmo estado observado.
- Divergência de ação completa: compara os seis componentes da ação.
- Divergência de distribuição: compara Jensen-Shannon da distribuição da
  cabeça de tipo (não de todas as cabeças condicionais).
- Preservação por estratégia e cenário: somente para estados realmente vistos.
- Partidas completas pareadas: comparam reward, colocação, Top 4, HP, ouro,
  nível e métricas estruturais/posicionais do snapshot terminal.
- Proveniência: checkpoint original/fine-tuned, commit do repositório, hashes
  do TftEngine/RewardModel/policy/PPO/config e parâmetros do experimento.
- A auditoria não classifica uma divergência como melhoria sem medir o efeito.

A validação de partidas completas pareadas ainda precisa ser executada antes de
promover o checkpoint. A auditoria shadow é necessária, mas não substitui esse
teste porque as trajetórias divergem após ações diferentes.

## Artefatos

- `runs/latest/logs/decision_trace.jsonl`: decisões originais e ajustadas no
  mesmo estado, incluindo probabilidades da cabeça de tipo.
- `runs/latest/logs/training_metrics.jsonl`: métricas PPO por update.
- `runs/latest/logs/scenario_results.jsonl`: resumos de episódios completos.
- `runs/latest/logs/paired_match_results.jsonl`: resultados de partidas
  completas pareadas.
- `runs/latest/reports/experiment_config.json`: configuração e hash do modelo.
- `runs/latest/reports/training_summary.json`: contagem de cenários encontrados.
- `reports/ECONOMY_FINETUNING_AUDIT.md`: auditoria gerada em Markdown,
  fora dos diretórios ignorados, pronta para revisão e commit.
