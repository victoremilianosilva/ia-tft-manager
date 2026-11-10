# Sessões, logs e replay

## Diretório de sessão

Ao iniciar uma partida com gravação habilitada, ViewerSession cria uma pasta match-YYYYMMDD-HHMMSS-id dentro do diretório escolhido, por padrão viewer/sessions/. Ela contém:

- metadata.json: versão do schema, match ID, caminho e SHA-256 do checkpoint, seed, modo determinístico, engine, horário, classe de policy, dimensões de observação/ação e nomes dos logs.
- player_1_log.json até player_8_log.json: linha do tempo independente por assento.

As entradas incluem IDs sequenciais, timestamp, rodada/estágio, tipo de evento, texto legível e payload estruturado. Snapshots podem incluir recursos, tabuleiro, banco, loja, traits contadas, ação, recompensa, diagnóstico de policy e eventos retornados pela engine.

## Persistência

PlayerJsonLogWriter atualiza os arquivos JSON periodicamente e em pontos importantes do ciclo; ao terminar ou fechar a sessão, faz flush e encerra o writer. O formato novo não gera events.jsonl. O leitor ainda aceita JSONL antigo para compatibilidade.

A linha legível de impacto usa cost × star × 2.0, identificada nos metadados como contribuição de board_power nativa. Não é métrica oficial de dano nem saída direta do modelo.

## Replay

O replay importa JSON com schema_version = 1 e log_format = tft_player_log, ou JSONL legado. Valida estrutura, versão e ordem/unicidade de sequence_id. Navegar no replay exibe entradas gravadas e não executa a policy nem avança a engine.

Ao abrir uma pasta de sessão, o leitor procura primeiro events.jsonl legado e, se não existir, tenta player_1_log.json.

## Integridade e limites

- match_id associa eventos à partida.
- checkpoint_sha256 identifica os pesos usados.
- seed e deterministic registram a configuração de inferência.
- Logs são dados de auditoria, não substituem os vetores de observação do PPO.
- Eventos não retornados pela API nativa não podem ser reconstruídos como se fossem observações reais.

Teste principal: tests/test_viewer_player_logs.py.
