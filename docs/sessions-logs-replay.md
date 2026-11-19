# Sessões, logs e replay

> Este documento descreve o formato de sessão/replay do Viewer atualmente implementado. Ele é distinto do [Strategic Shadow Integrated Replay Contract v1](strategic-shadow-integrated-replay-contract.v1.draft.md), que define a futura prova determinística integrada entre produtores/consumidores Shadow, PPO e outcomes. Um replay de logs do Viewer não comprova a cadeia integrada nem substitui fixtures/artefatos exigidos pelo contrato.

## Diretório de sessão

Ao iniciar uma partida com gravação habilitada, ViewerSession cria uma pasta match-YYYYMMDD-HHMMSS-id dentro do diretório escolhido, por padrão viewer/sessions/. Ela contém:

- metadata.json: versão do schema, match ID, caminho e SHA-256 do checkpoint, seed, modo determinístico, engine, horário, classe de policy, dimensões de observação/ação e nomes dos logs.
- player_1_log.json até player_8_log.json: linha do tempo independente por assento.

As entradas incluem IDs sequenciais, timestamp, rodada/estágio, tipo de evento, texto legível e payload estruturado. Snapshots podem incluir recursos, tabuleiro, banco, loja, traits contadas, ação, recompensa, diagnóstico de policy e eventos retornados pela engine.

## Correlação com a identidade nativa

O `match_id` dos eventos do Viewer é um UUID gerado por `ViewerSession`; ele não é o ID numérico do episódio do TFTEngine. Ao persistir diagnósticos de Composition Intelligence, o Viewer acrescenta um envelope que contém os dois IDs, jogador, rodada, timestamp e sequência do diagnóstico. O Unified strategic sidecar permanece com o Engine match ID e sequência própria; a correlação depende desse envelope de Composition Intelligence.

A validação atual de `identity_complete` verifica player_id, round e sequence, mas não exige engine_match_id. Portanto, esse booleano não é prova suficiente de correlação Engine↔sessão. Consulte [Current Replay, Correlation and Evaluation Gap Audit](current-replay-correlation-evaluation-gap-audit.v1.draft.md).

O PPO RolloutBuffer guarda observações e máscaras em tensores separados e mantém metadata por linha com Engine instance, episode, decision sequence, player sequence, player ID, round, hash da observação float32 e hash da máscara pós-ablation. Os hashes são metadados de correlação, não features neurais. O replay do Viewer continua sendo navegação de logs; não reexecuta Engine ou policy.

## Persistência

PlayerJsonLogWriter atualiza os arquivos JSON periodicamente e em pontos importantes do ciclo; ao terminar ou fechar a sessão, faz flush e encerra o writer. O formato novo não gera events.jsonl. O leitor ainda aceita JSONL antigo para compatibilidade.

A linha legível de impacto usa cost × star × 2.0, identificada nos metadados como contribuição de board_power nativa. Não é métrica oficial de dano nem saída direta do modelo.

## Replay

O replay importa JSON com schema_version = 1 e log_format = tft_player_log, ou JSONL legado. Valida estrutura, versão e ordem/unicidade de sequence_id. Navegar no replay exibe entradas gravadas e não executa a policy nem avança a engine.

Ao abrir uma pasta de sessão, o leitor procura primeiro events.jsonl legado, depois player_1_log.json e, por último, player_1_log.tft. O formato .tft histórico é exibido como timeline textual somente leitura, preservando linhas e ordem; o leitor não inventa ações, snapshots, recompensas ou identidade de Engine a partir do texto.

## Integridade e limites

- ViewerSession.match_id associa eventos à sessão do Viewer; a correlação com o Engine episode ID é um envelope separado nos diagnósticos de Composition Intelligence.
- checkpoint_sha256 identifica os pesos usados.
- seed e deterministic registram a configuração de inferência.
- Logs são dados de auditoria, não substituem os vetores de observação do PPO.
- Eventos não retornados pela API nativa não podem ser reconstruídos como se fossem observações reais.

Testes principais: tests/test_viewer_player_logs.py e tests/test_viewer_legacy_log_compatibility.py.
