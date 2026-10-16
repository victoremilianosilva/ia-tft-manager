# TFT Viewer

Aplicativo desktop de observação e avaliação de partidas TFT-like, baseado exclusivamente na especificação de `viewer/docs/TFT_VIEWER_PLAN.md`.

## Estrutura

- `viwer/main.py`: entrada da interface desktop.
- `viewer/session.py`: controlador, inferência, eventos e replay.
- `viewer/docs/`: especificação integral e wireframes.

## Executar no Windows

Na raiz do repositório, com o ambiente virtual ativo:

```powershell
python -m pip install -r requirements.txt -r viewer/requirements.txt
cmake --build cpp/build --config Release --parallel 2
$env:PYTHONPATH = "$PWD\cpp\build\bin\Release;$PWD"
python -m viwer.main
```

O motor nativo `tft_engine` e o catálogo `units_gerado.json` precisam estar disponíveis. Se a build estiver incompleta, compile todos os módulos nativos conforme os passos acima.

## Checkpoint

A primeira versão aceita checkpoints cujo arquivo contém o `state_dict` da `TFTPolicy` ou um dicionário com `policy`, `policy_state_dict`, `model_state_dict` ou `state_dict`, e metadados opcionais `obs_dim`, `action_dims` e `hidden_size`. O modelo é carregado em CPU, colocado em `eval()`, com gradientes desativados. Nenhum `PPOTrainer` nem otimizador é criado.

## Sessões e replay

As novas sessões são gravadas em `viewer/sessions/` com `metadata.json` e oito arquivos independentes: `player_1_log.json` até `player_8_log.json`. Cada arquivo é o histórico legível daquele jogador (`text`) junto dos dados estruturados de ação, recompensa, snapshots do tabuleiro/banco/loja, evolução, mudanças de sinergia e análise de posicionamento. O JSON é atualizado atomicamente durante a partida, no fim de rodada e ao finalizar. Novas sessões não criam `events.jsonl`; o botão de replay ainda pode importar arquivos JSONL legados, apenas para compatibilidade. Abrir replay nunca executa a política.

## Limitações explícitas da primeira versão

- A engine avança o lobby em passos conjuntos de oito ações; não há pausa no meio de uma chamada nativa.
- A visualização de combate mostra eventos e snapshots efetivamente disponíveis. Se posições/HP intermediários não chegarem ao binding, a interface indica a ausência, sem fabricar animações.
- A inferência diagnóstica registra distribuições após máscara para as cabeças visitadas, sem executar uma segunda amostragem.
- O formato de checkpoint precisa corresponder à arquitetura atual de `TFTPolicy`; formatos incompatíveis são rejeitados.
