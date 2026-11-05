# Fine-tuning Econômico Independente — TFT AI

Este diretório é um pipeline isolado. Não altera `trainer.py`, `policy.py`,
`ppo.py`, `rollout.py`, wrappers existentes, engine C++ ou auditoria de
partidas reais. Os módulos existentes são importados apenas para reutilizar
contratos, arquitetura, buffer PPO e engine nativa.

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
  --rollout-steps 128
# O script imprime o caminho exclusivo do checkpoint e da execução.
```

O checkpoint de origem nunca é sobrescrito. Cada execução exige `--scenario`
e aplica shaping somente a esse cenário; os demais são registrados apenas
para monitoramento. Por padrão, somente `type_head` e `value_head` são treináveis; encoder espacial/global, fusão, cabeças de
loja, venda, banco, tabuleiro e itens permanecem congeladas. A cabeça de tipo
compartilhada é projetada de volta para uma pequena região L2 ao redor dos
pesos originais a cada update. O shaping é pequeno e condicionado ao
estado/estratégia; SLOWROLL recebe proteção explícita contra incentivo genérico
de XP. O limite de drift pode ser ajustado com `--max-type-head-drift`.

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

Cada modelo joga sua própria lobby com a mesma seed. As trajetórias podem
divergir depois das primeiras ações; isso é intencional e permite comparar
consequências. O avaliador registra rewards nativos, contagens de ações e
snapshot terminal. Reward não é tratado automaticamente como colocação.

## Auditoria e visualizador

Instale as dependências opcionais:

```bash
pip install -r economy_finetuning/requirements-viewer.txt
```

Gere o relatório e abra o viewer:

```bash
python economy_finetuning/audit.py \
  --trace CAMINHO_DA_EXECUCAO/logs/decision_trace.jsonl \
  --paired CAMINHO_DA_EXECUCAO/logs/paired_match_results.jsonl
streamlit run economy_finetuning/viewer/app.py
```

O visualizador lê JSONL localmente, limita a leitura padrão a 200 mil linhas e
permite filtrar divergências e exportar o subconjunto investigado. Os JSONL,
checkpoints e execuções são dados locais e ficam ignorados pelo Git.

## Cenários implementados

Veja a lista integral em `SCENARIOS.md`. Os cenários são classificados como
treináveis ou monitor-only. Casos de utilidade de loja e estabilização com HP
crítico ficam monitor-only quando a observação disponível não permite provar
que uma compra específica é útil; não criamos rótulos artificiais.

## O que a auditoria consegue provar

- Shadow comparison: original e fine-tuned recebem o mesmo estado observado.
- Divergência de ação completa: compara os seis componentes da ação.
- Divergência de distribuição: compara Jensen-Shannon da distribuição da
  cabeça de tipo (não de todas as cabeças condicionais).
- Preservação por estratégia e cenário: somente para estados realmente vistos.
- Partidas completas pareadas: medem reward e guardam estado terminal bruto.
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
