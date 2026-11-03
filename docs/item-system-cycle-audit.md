# Auditoria do ciclo de itens — PR #149

**Escopo:** rastrear componente, receita, item, inventário, unidade, equipamento e combate.  
**Branch auditada:** `fix/purchase-sale-classification`.  
**Status:** diagnóstico estático; nenhuma partida ou treinamento foi executado para esta auditoria.

## Resumo

A infraestrutura principal existe, mas o ciclo real ainda não está comprovado. O catálogo Set18 está versionado em `data/itens.json`; o loader C++ valida estrutura, receitas e cobertura mínima de efeitos. O maior bloqueio funcional conhecido está na aquisição: as APIs de concessão existem, mas não foi encontrada uma chamada originada no fluxo normal de recompensas/loot do lobby. Assim, uma partida pode nunca produzir componentes ou itens para a policy usar.

## Evidências por etapa

| Etapa | Estado observado | Lacuna / risco |
|---|---|---|
| Componente | 10 IDs no catálogo Set18; `ItemEngine::add_component` valida IDs e conta cópias | API de concessão existe, mas não está conectada a um resolvedor de loot de partida |
| Receita | 39 receitas de dois componentes no catálogo; receitas simétricas e componentes duplicados são suportados | A cobertura depende do catálogo selecionado e da normalização correta do set |
| Item | 55 registros no catálogo: 39 itens com receita e 16 itens de emblema | Dados de origem e efeitos normalizados não são equivalentes; passivas precisam de cobertura explícita |
| Inventário | Estado por jogador separado em componentes, itens completos e equipamentos por UUID | É necessário provar aquisição real e persistência em uma partida completa |
| Compatibilidade | `item_fit` considera atributos numéricos, pesos de função, traits e composição | Não pontua diretamente `combat_effects`; passivas podem ser subavaliadas na observação e na decisão |
| Craft/equip | Ações PPO 7/8, máscaras e validação C++ existem; craft+equip tem rollback | Testes de fixture não demonstram que a policy escolhe essas ações com loot real |
| Combate | `CombatItemAdapter` projeta atributos e efeitos para `CombatInput`; o simulador interpreta operações genéricas e também mantém compatibilidade por IDs | Nem todo efeito CommunityDragon é normalizado ou interpretado; passagem do objeto não prova aplicação correta da passiva |

## Catálogo e efeitos

O arquivo `data/itens.json` declara `Set18`, 10 componentes, 55 itens, 39 receitas e 16 emblemas. Os emblemas usam IDs `DA_18_*`, e esses IDs também aparecem em `data/item_effects.json`; portanto, a diferença entre a família `TFT_Item_*` dos itens comuns e `DA_18_*` dos emblemas não é, isoladamente, uma falha de correspondência.

O gerador `scripts/generate_item_catalog.py` preserva `source_effects`, mas sua normalização genérica de combate atualmente mapeia diretamente apenas bônus de AD e regeneração de mana. O catálogo contém muitas outras chaves de origem (por exemplo, efeitos condicionais de vida, escudos, dano por ataque, cura, redução de resistências e efeitos por acúmulo). Uma inspeção estática encontrou 117 ocorrências de chaves de efeito de origem que não pertencem ao conjunto de atributos/efeitos normalizados diretamente pelo gerador. **Esse número não significa 117 efeitos definitivamente ausentes do combate:** parte deles pode ser tratada por compatibilidade específica de item em `CombatEngine.cpp`. É necessário comparar item a item para distinguir efeito aplicado, efeito aproximado e efeito sem implementação.

O simulador interpreta atualmente estas operações genéricas: `add_stat`, `bonus_damage`, `grant_charges`, `heal_max_hp_pct` e `mana_regen`. O contrato de dados comenta outras operações, mas não basta que uma operação esteja documentada: ela precisa ter implementação e teste de combate.

## Aquisição

`TFTEngine::grant_item_component` e `TFTEngine::grant_completed_item` concedem itens e atualizam máscaras. Os aliases `*_for_testing` também existem. A documentação de integração já registra que o lobby não possui um resolvedor de drops PvE conectado a essas APIs. Até que a origem real de recompensas chame essas funções, a aquisição de itens não está integrada ao fluxo normal da partida.

Não devemos inventar drops, taxas ou recompensas para mascarar essa lacuna. A integração precisa usar os eventos e regras do ambiente que o simulador pretende representar.

## Correções necessárias, em ordem

1. **Aquisição:** localizar o ponto real de resolução de recompensas PvE/armory e conectar a concessão de componentes/itens. Registrar origem, jogador, round e quantidade.
2. **Catálogo:** adicionar validação por item que compare cada chave `source_effects` com atributos normalizados, operações genéricas suportadas e handlers legados explicitamente testados. Itens parcialmente modelados devem ser reportados como tais, não como totalmente funcionais.
3. **Compatibilidade:** incluir efeitos especiais suportados na avaliação marginal do item por unidade, respeitando função, traits, composição, condições e valor já acumulado. Evitar duplicar peso de atributos que já estão nos stats.
4. **Decisão de craft/equip:** registrar candidatos legais, score por item/unidade, ação escolhida, resultado e motivo de rejeição. Separar craft de equip na telemetria, mesmo quando a ação atômica executa ambos.
5. **Execução no combate:** para cada item, testar entrada de combate e efeito observável (atributo inicial, dano, cura, escudo, mana ou aura). Itens com mecânica não suportada devem falhar na validação de cobertura ou ser marcados explicitamente como aproximados.

## Critérios de aceite

- Uma partida real produz componentes/itens por eventos de aquisição identificáveis.
- Pelo menos um componente coletado pode completar uma receita válida, gerar um item no inventário e ser equipado em uma unidade identificada por UUID.
- A policy recebe observações e máscaras coerentes e executa a transição sem rejeições.
- O item aparece no `CombatInput` da unidade correta e seu efeito suportado altera uma métrica/evento verificável do combate.
- A auditoria registra tentativas, transições bem-sucedidas, itens não utilizados, crafts, equips, efeitos aplicados e motivos de falha.
- A validação cobre os oito jogadores e não considera uma partida truncada como aprovada.

**Não executar treino ou partida de comparação até fechar as correções e os testes determinísticos acima.**
