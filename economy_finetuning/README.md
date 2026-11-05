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

Compile a engine C++ como já é necessário para o projeto e instale as
dependências opcionais:

```bash
pip install -r economy_finetuning/requirements-viewer.txt
python economy_finetuning/finetune.py \
  --checkpoint tft_checkpoint.pt \
  --updates 100 \
  --rollout-steps 128 \
  --output economy_finetuning/checkpoints/economy_ft.pt
```

O checkpoint de origem nunca é sobrescrito. Por padrão, somente `type_head`
e `value_head` são treináveis; encoder espacial/global, fusão, cabeças de
loja, venda, banco, tabuleiro e itens permanecem congeladas. O shaping é
pequeno e condicionado ao estado/estratégia; SLOWROLL recebe proteção explícita
contra incentivo genérico de XP.

## Auditoria e visualizador

```bash
python economy_finetuning/audit.py
streamlit run economy_finetuning/viewer/app.py
```

O visualizador lê JSONL localmente, limita a leitura padrão a 200 mil linhas e
permite filtrar divergências e exportar o subconjunto investigado. Os JSONL,
checkpoints e execuções são dados locais e ficam ignorados pelo Git.

## O que a auditoria consegue provar

- Shadow comparison: original e fine-tuned recebem o mesmo estado observado.
- Divergência de ação completa: compara os seis componentes da ação.
- Divergência de distribuição: compara Jensen-Shannon da distribuição da
  cabeça de tipo (não de todas as cabeças condicionais).
- Preservação por estratégia e cenário: somente para estados realmente vistos.
- A auditoria não classifica uma divergência como melhoria sem medir o efeito.

A validação de partidas completas pareadas ainda precisa ser executada antes de
promover o checkpoint. A auditoria shadow é necessária, mas não substitui esse
teste porque as trajetórias divergem após ações diferentes.

## Artefatos

- `runs/latest/logs/decision_trace.jsonl`: decisões originais e ajustadas no
  mesmo estado, incluindo probabilidades da cabeça de tipo.
- `runs/latest/logs/training_metrics.jsonl`: métricas PPO por update.
- `runs/latest/logs/scenario_results.jsonl`: resumos de episódios completos.
- `runs/latest/reports/experiment_config.json`: configuração e hash do modelo.
- `runs/latest/reports/training_summary.json`: contagem de cenários encontrados.
- `runs/latest/reports/ECONOMY_FINETUNING_AUDIT.md`: auditoria gerada.
