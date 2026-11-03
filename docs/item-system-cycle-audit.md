# Auditoria do ciclo de itens — PR #149

**Escopo:** rastrear componente, receita, item, inventário, unidade, equipamento e combate.  
**Branch auditada:** `fix/purchase-sale-classification`.  
**Status:** diagnóstico estático; nenhuma partida ou treinamento foi executado para esta auditoria.

## Resumo

A infraestrutura principal e o resolvedor de recompensas PvE já existem. O catálogo Set18 está versionado em `data/itens.json`; o lobby concede componentes e escolhas de bigorna ao longo das etapas. As lacunas mais importantes estavam na avaliação dos efeitos especiais, na validação de operações que o simulador não implementa e na telemetria que não distinguia aquisição de equipamento aplicado. Esta PR fecha essas lacunas de integração, mas não declara todas as passivas CommunityDragon como simuladas.

## Evidências por etapa

| Etapa | Estado observado | Lacuna / risco |
|---|---|---|
| Componente | 10 IDs no catálogo Set18; `ItemEngine::add_component` valida IDs e conta cópias; etapas PvE 2 e 3 concedem componente aleatório por jogador vivo | A tabela de recompensas simulada é uma simplificação explícita; não deve ser confundida com probabilidades oficiais de loot |
| Receita | 39 receitas de dois componentes no catálogo; receitas simétricas e componentes duplicados são suportados | A cobertura depende do catálogo selecionado e da normalização correta do set |
| Item | 55 registros no catálogo: 39 itens com receita e 16 itens de emblema | Dados de origem e efeitos normalizados não são equivalentes; passivas precisam de cobertura explícita |
| Inventário | Estado por jogador separado em componentes, itens completos e equipamentos por UUID | É necessário provar aquisição real e persistência em uma partida completa |
| Compatibilidade | `item_fit` considera atributos numéricos, pesos de função, traits, composição e agora passivas suportadas, com condições/função | Efeitos que não têm handler no simulador não recebem score como se fossem funcionais |
| Craft/equip | Ações PPO 7/8, máscaras e validação C++ existem; craft+equip tem rollback | Testes de fixture não demonstram que a policy escolhe essas ações com loot real |
| Combate | `CombatItemAdapter` projeta atributos e efeitos para `CombatInput`; o simulador interpreta operações genéricas e mantém handlers legados por ID | Cobertura das passivas específicas ainda precisa ser validada item a item; loader agora rejeita operação/trigger sem handler |

## Catálogo e efeitos

O arquivo `data/itens.json` declara `Set18`, 10 componentes, 55 itens, 39 receitas e 16 emblemas. Os emblemas usam IDs `DA_18_*`, e esses IDs também aparecem em `data/item_effects.json`; portanto, a diferença entre a família `TFT_Item_*` dos itens comuns e `DA_18_*` dos emblemas não é, isoladamente, uma falha de correspondência.

O gerador `scripts/generate_item_catalog.py` preserva `source_effects`, mas sua normalização genérica de combate atualmente mapeia diretamente apenas bônus de AD e regeneração de mana. O catálogo contém muitas outras chaves de origem (por exemplo, efeitos condicionais de vida, escudos, dano por ataque, cura, redução de resistências e efeitos por acúmulo). A cobertura por item em `data/itens.json` agora identifica 118 ocorrências de chaves de origem ainda não normalizadas genericamente, distribuídas por 38 itens. **Esse número não significa 117 efeitos definitivamente ausentes do combate:** parte deles pode ser tratada por compatibilidade específica de item em `CombatEngine.cpp`. É necessário comparar item a item para distinguir efeito aplicado, efeito aproximado e efeito sem implementação.

O simulador interpreta atualmente estas operações genéricas: `add_stat`, `bonus_damage`, `grant_charges`, `heal_max_hp_pct` e `mana_regen`. O loader C++ agora rejeita operações não implementadas e combinações incompatíveis entre operação e trigger, evitando que um catálogo aceite passivas silenciosamente inertes. O gerador e `data/itens.json` agora expõem `effect_coverage` por item: chaves de origem, atributos normalizados, efeitos genéricos e chaves que ainda exigem revisão específica. A lista de chaves não normalizadas não é automaticamente uma lista de bugs, pois parte pode ter handler legado ou ser parâmetro de uma passiva. Os testes de combate existentes cobrem, entre outros, AD genérico, dano bônus, efeitos condicionais e auras.

## Aquisição e decisão

O resolvedor PvE interno do lobby está conectado ao estado de cada jogador:
- etapas 2 e 3: um componente aleatório do catálogo vai diretamente à bolsa;
- 4-7: uma bigorna oferece até três componentes, e a policy escolhe um;
- 5-7 e 6-7: uma bigorna oferece até quatro itens completos, e a policy escolhe um.

As escolhas usam o RNG individual do jogador, registram eventos de concessão e atualizam as máscaras. As APIs públicas `TFTEngine::grant_item_component` e `grant_completed_item` também existem para integrações externas/testes. A auditoria anterior estava incorreta ao afirmar que o resolvedor PvE não existia; a implementação já estava no lobby.

A decisão continua sendo da policy unificada: ação 7 equipa do inventário; ação 8 faz craft e equipa. Não foi criado seletor heurístico paralelo. A recompensa da ação agora combina o valor numérico com a força dos efeitos especiais que o simulador realmente suporta, sem somar os dois valores diretamente e duplicar os mesmos atributos.

## Alterações implementadas nesta etapa

1. **Compatibilidade:** `ItemEngine::item_effect_strength` pontua efeitos suportados por operação, alvo, função e condições; `item_fit` inclui esse valor na compatibilidade usada pelas observações.
2. **Recompensa:** a qualidade imediata de equip/craft combina força numérica e força de passivas suportadas por composição multiplicativa, evitando dupla contagem aditiva.
3. **Contrato catálogo/combate:** o loader C++ aceita somente operações e pares trigger/operação com handlers existentes no `CombatEngine`. Operações como `grant_shield` sem handler não são mais aceitas como se fossem funcionais.
4. **Telemetria:** o lobby emite `ITEM_ANVIL_CHOSEN` e `ITEM_ACTION_APPLIED`, incluindo jogador, tipo, item, unidade-alvo, fit, recompensa e etapa.
5. **Auditoria:** `audit_item_system_e2e.py` agrega eventos de loot, bigorna e transições aplicadas, além de contagens por tipo de ação.

## Limite conhecido de cobertura

O catálogo preserva `source_effects` da CommunityDragon, mas isso não significa que toda chave de origem seja aplicada pelo simulador. Parte das passivas é coberta por handlers específicos existentes em `CombatEngine.cpp`; outras ainda não têm implementação genérica ou específica. Não se deve converter uma chave desconhecida em atributo permanente nem premiá-la como efeito ativo. A cobertura completa exige mapeamento/teste por item e só deve ser marcada como suportada quando houver efeito observável no combate.

## Critérios de aceite

- Uma partida real produz componentes/itens por eventos de aquisição identificáveis.
- Pelo menos um componente coletado pode completar uma receita válida, gerar um item no inventário e ser equipado em uma unidade identificada por UUID.
- A policy recebe observações e máscaras coerentes e executa a transição sem rejeições.
- O item aparece no `CombatInput` da unidade correta e seu efeito suportado altera uma métrica/evento verificável do combate.
- A auditoria registra tentativas, transições bem-sucedidas, itens não utilizados, crafts, equips, efeitos aplicados e motivos de falha.
- A validação cobre os oito jogadores e não considera uma partida truncada como aprovada.

**Não executar treino ou partida de comparação até fechar as correções e os testes determinísticos acima.**
