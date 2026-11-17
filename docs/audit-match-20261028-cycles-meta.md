# Auditoria de loops e composição meta — sessão 2026-10-28 21:39

Sessão: `viewer/sessions/match-20261028-213933-26547a5c`  
Seed: `20261016` · checkpoint SHA-256: `524c4e4aaccabb07f23cff06ff949b7f6472c6b10326a208aaad2233db18b72b`

## Evidência do log

Dos oito arquivos, os logs dos jogadores 2 e 4 estão vazios. Os outros seis contêm 551 movimentos no total (P1 137, P3 74, P5 84, P6 51, P7 120, P8 85). Os testes não tratam nomes de unidades como UUIDs: os padrões de reversão do texto são candidatos que precisam ser reproduzidos com snapshots nativos.

Padrões prioritários para reproduzir:

- **P1:** Akali ↔ Ornn e Akali ↔ Kog'Maw/Ezreal; várias ações consecutivas com recompensa negativa, incluindo movimentos para a mesma unidade/slot visual.
- **P3:** Rek'Sai ↔ Grompe e, mais tarde, Fiddlesticks/Rammus/Aronguejo. A mesma sequência de três unidades reaparece com poucos passos de intervalo.
- **P5:** Cassiopeia ↔ Tristana aparece repetidamente, assim como Ahri ↔ Cassiopeia. Há reversões com recompensa combinada negativa; esse é um caso forte para replay.
- **P6:** Hecarim ↔ Akali e sequências envolvendo Teemo, Soraka, Ahri e Lillia. Há reversões com recompensa negativa e algumas ações isoladas que podem ser reposicionamento legítimo.
- **P7:** Fiddlesticks ↔ Cassiopeia/Diana e repetições Fiddlesticks ↔ Fiddlesticks; também há alternância de Rakan e Fiddlesticks. O mesmo nome dos dois lados pode representar cópias distintas, então não prova identidade.
- **P8:** Leona ↔ Rakan, Kha'Zix ↔ Teemo e sequências Kha'Zix/Cassiopeia/Leona. Recompensas negativas repetidas indicam que vale montar um replay exato.

## Composição meta

O log agora permite distinguir eventos diferentes:
- **candidate:** composição avaliada pelo scorer;
- **selected:** auditoria nativa emitiu `status=selected`;
- **executed_source_observed:** uma estratégia posterior registra `FONTE COMP: OP.GG — nome`;
- **outcome:** compras observadas, unidades no último quadro do tabuleiro, eventos de sinergia, strength final e colocação, quando presentes no log.

A fonte OP.GG é evidência de seleção/adoção pela estratégia, não prova de que toda a composição planejada foi montada. A lista de compras não é tratada como prova de implantação. O relatório mantém esses campos separados para comparação posterior.

## Limitações e próximo passo

O formato legado `.tft` não registra UUIDs nem snapshots completos antes/depois de cada ação. Por isso o teste da sessão confirma que os padrões de reversão estão presentes no log, mas **não** os chama de ciclos exatos. O teste complementar da assinatura nativa verifica identidade da unidade, tabuleiro, banco, itens, economia e contexto estratégico. Para reproduzir o ciclo real, execute o audit nativo com o seed/checkpoint da sessão e compare as assinaturas completas antes de mudar qualquer penalidade ou máscara.

Comando para inspeção do log:

```powershell
python scripts/audit_viewer_loops_and_meta.py viewer/sessions/match-20261028-213933-26547a5c --json reports/match-20261028-loops-meta.json
```

Testes novos:

```powershell
pytest tests/test_viewer_loops_meta_reproduction.py tests/test_native_cycle_signature_context.py -q
```
