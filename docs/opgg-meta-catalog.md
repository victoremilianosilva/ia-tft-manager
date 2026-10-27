# Catálogo competitivo OP.GG para TFT

## Fluxo

O coletor `scripts/update_opgg_meta_catalog.py` chama exclusivamente `tft_list_meta_decks`. Ele salva:

- `data/opgg_tft_meta_raw.json`: resposta original para auditoria;
- `data/opgg_tft_meta.json`: catálogo normalizado consumido pelo planejador C++.

O coletor valida a resposta antes de substituir arquivos e escreve os arquivos de forma atômica. Se a chamada falhar e já existir um catálogo válido, preserva o último snapshot válido.

## Treinamento

`python trainer.py` tenta atualizar o catálogo antes de criar o Trainer. Por padrão, snapshots com menos de 12 horas são reutilizados; portanto, o treino não faz chamadas de rede por decisão ou por episódio.

Variáveis úteis:

- `TFT_OPGG_DISABLE_REFRESH=1`: não chama o MCP.
- `TFT_OPGG_META_CATALOG=C:/caminho/catalogo.json`: caminho explícito para o JSON consumido pelo C++.
- `python scripts/update_opgg_meta_catalog.py --if-stale`: atualiza somente se o snapshot estiver vencido.
- `python scripts/update_opgg_meta_catalog.py`: força nova coleta.
- `python scripts/update_opgg_meta_catalog.py --offline`: exige um catálogo existente e não usa rede.

O catálogo gerado não deve ser editado manualmente nem ser a única cópia dos dados brutos.

## Viewer

Ao carregar um checkpoint, o Viewer executa o mesmo coletor em modo `--if-stale`. Se a rede estiver indisponível, a sessão continua e o planejador nativo permanece como fallback. Não há chamadas ao MCP durante os passos da partida.

## Como o planejador usa os dados

O `CompositionPlanner` mantém seu plano nativo e compara com as composições do catálogo:

- nível até 5: o snapshot `early_game` informa as peças de transição a procurar;
- nível 6–7: o snapshot `mid_game` informa a transição intermediária;
- nível 8+: as unidades finais definem o alvo;
- unidades já possuídas, unidades na loja, traits já representadas, custo, dificuldade estimada de aquisição e papéis carry/frontline afetam o score;
- as estatísticas de Top 4 só dão um bônus pequeno e apenas quando há uma amostra mínima;
- a candidata externa só substitui o plano nativo quando obtém vantagem contextual. O catálogo não restringe máscaras nem torna compras obrigatórias.

O catálogo deve conter IDs compatíveis com `units_gerado.json`. Unidades sem correspondência são ignoradas. Um catálogo ausente, inválido ou incompatível não pode interromper a partida.

## Limitações intencionais da primeira versão

A integração usa somente `tft_list_meta_decks`. Os campos `deck` e `label` são preservados separadamente, sem presumir que sejam estatísticas intercambiáveis. O coletor não infere o patch: guarda a metadata recebida e o horário da coleta. O score é uma heurística inicial e precisa ser avaliado por ablação antes de ser tratado como ganho comprovado de win rate.
