# TFT Viewer desktop

## Implementação real

O viewer é uma aplicação PySide6 em viewer/main.py, com lógica de sessão em viewer/session.py e persistência por jogador em viewer/player_logs.py. O comando canônico é python -m viewer.main. A entrada antiga viwer/main.py foi consolidada em viewer/main.py para manter a interface e a lógica de sessão no mesmo pacote.

O viewer é ferramenta de avaliação e observação: carrega uma policy treinada, chama a engine C++ e mostra o estado retornado. Não cria PPOTrainer, não otimiza pesos e não continua o treinamento.

## Componentes

- ViewerWindow: janela principal, controles de checkpoint, seed, modo determinístico, diretório de saída, execução/pausa/passo e layout adaptável.
- PlayerCard e ChampionCell: visão dos oito jogadores e tabuleiros 4 × 7; o foco individual mostra tabuleiro, banco, loja, recursos e diagnóstico disponível.
- ChampionIconLoader: carrega ícones de forma assíncrona. A ausência de imagem não deve impedir a leitura textual.
- StepWorker: executa o passo da sessão numa thread de trabalho para não bloquear a interface durante uma chamada nativa.
- ViewerSession: checkpoint, policy, seed, engine, inferência, snapshots, eventos e replay.
- PlayerJsonLogWriter: grava oito arquivos independentes, um por assento.

## Checkpoint

A sessão verifica a existência do checkpoint e de units_gerado.json, calcula SHA-256 e carrega os pesos em CPU. Aceita dicionários com policy_state_dict, model_state_dict, state_dict, policy ou um state dict diretamente, além de metadados opcionais obs_dim, action_dims e hidden_size. Se obs_dim estiver ausente, tenta inferi-lo a partir de global_mlp.0.weight. Os pesos precisam corresponder à arquitetura atual de TFTPolicy; incompatibilidades são rejeitadas.

A policy entra em eval() e seus parâmetros ficam sem gradiente. O viewer não cria otimizador nem trainer.

## Passo e interface

A engine avança a lobby em um passo nativo com oito ações. A sessão monta uma ação por jogador vivo e envia PASS para vagas eliminadas. Não é possível pausar a engine no meio de uma chamada step; pausa e velocidade controlam os passos seguintes. Ao fechar, a janela aguarda a thread ativa antes de fechar a engine.

A interface apresenta a lobby, o jogador selecionado, recursos, formações, banco, loja, o último pareamento informado pelo estado público, eventos da engine e diagnóstico de policy. O painel de combate usa opponent_id real. Se a engine não fornece HP/mana por frame, o viewer não inventa animações.

Diagnósticos incluem probabilidades após máscara das cabeças visitadas, alternativas, log-probability, entropia e estimativa de valor. Isso é dado numérico da policy, não uma explicação em linguagem natural da intenção do modelo.

## Execução no Windows

Na raiz do repositório, com Python, CMake e toolchain C++ configurados:

~~~powershell
python -m pip install -r requirements.txt -r viewer/requirements.txt
python scripts/build_native.py
$env:PYTHONPATH = "$PWD\cpp\build\bin\Release;$PWD"
python -m viewer.main
~~~

Ajuste PYTHONPATH se a extensão nativa tiver sido gerada em outro diretório.

## Diagramas

- [Arquitetura](assets/viewer-architecture.svg)
- [Wireframe do dashboard](assets/viewer-dashboard-wireframe.svg)
- [Wireframe de combate](assets/viewer-combat-wireframe.svg)
- [Ciclo de eventos](assets/viewer-event-lifecycle.svg)

Wireframes são conceituais; não garantem que a engine entregue todos os campos desenhados. Veja também [logs e replay](sessions-logs-replay.md).

## Testes relevantes

- tests/test_viewer_player_logs.py
- tests/test_viewer_policy_diagnostics.py

Execute os testes no ambiente do projeto antes de considerar uma alteração validada.
