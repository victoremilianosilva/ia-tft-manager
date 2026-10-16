# TFT Viewer

Aplicativo desktop de observação e avaliação de partidas TFT-like, baseado exclusivamente na especificação de `TFT_VIEWER_PLAN.md`.

## Executar no Windows

Na raiz do repositório, com o ambiente virtual ativo:

```powershell
python -m pip install -r viewer/requirements.txt
cmake --build cpp/build --config Release --parallel 2
$env:PYTHONPATH = "$PWD\cpp\build\bin\Release;$PWD"
python -m viwer.main
```

O motor nativo `tft_engine` e o catálogo `units_gerado.json` precisam estar disponíveis. Se a build estiver incompleta, compile todos os módulos nativos conforme os passos acima.

## Checkpoint

A primeira versão aceita checkpoints cujo arquivo contém o `state_dict` da `TFTPolicy` ou um dicionário com `policy_state_dict`, `model_state_dict` ou `state_dict`, e metadados opcionais `obs_dim`, `action_dims` e `hidden_size`. O modelo é carregado em CPU, colocado em `eval()`, com gradientes desativados. Nenhum `PPOTrainer` nem otimizador é criado.

## Sessões e replay

As sessões são gravadas em `viewer/sessions/` com `metadata.json` e `events.jsonl`. Os eventos têm `schema_version` e `sequence_id` monotônico. Abrir replay lê os eventos existentes e não executa a política.

## Limitações explícitas da primeira versão

- A engine avança o lobby em passos conjuntos de oito ações; não há pausa no meio de uma chamada nativa.
- A visualização de combate mostra eventos e snapshots efetivamente disponíveis. Se posições/HP intermediários não chegarem ao binding, a interface indica a ausência, sem fabricar animações.
- A inferência diagnóstica registra distribuições após máscara para as cabeças visitadas, sem executar uma segunda amostragem.
- O formato de checkpoint precisa corresponder à arquitetura atual de `TFTPolicy`; formatos incompatíveis são rejeitados.
