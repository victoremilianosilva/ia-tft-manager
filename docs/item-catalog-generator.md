# Gerar catálogo de itens por set

O arquivo **itens.json** é a cópia de origem do CommunityDragon. Ele contém vários sets e pode conter mais de uma entrada **setData** para o mesmo set. O gerador mescla as entradas com o mesmo número/nome, filtra as receitas pertencentes ao set selecionado e escreve o contrato **schema_version: 1** consumido por **cpp/include/items/ItemCatalog.hpp**.

## Uso

Na raiz do repositório:

```bash
python scripts/generate_item_catalog.py --set 16
```

O comando acima lê **itens.json** (fonte bruta do CommunityDragon) e gera **data/item_catalog_16.json**. Para o Set 18, o arquivo de saída ativo é **data/itens.json**, consumido por padrão pela engine. Os metadados especiais do Set 18 ficam em **data/item_effects.json**. Para outros sets, use o número ou nome correspondente:

```bash
python scripts/generate_item_catalog.py --set 18
python scripts/generate_item_catalog.py --set Set17 --output data/item_catalog_set17.json
python scripts/generate_item_catalog.py --set 16 --input path/to/itens.json --output /tmp/catalog.json
```

O script não baixa dados da internet. Isso torna o resultado reprodutível a partir da cópia de origem versionada no repositório.

## O que entra no catálogo

- Componentes referenciados pelas receitas do set.
- Itens cuja definição de origem contém exatamente dois componentes.
- IDs e nomes originais, receita, descrição, ícone e **effects** da origem.
- Campos numéricos normalizados que o contrato atual da engine reconhece.
- Pesos heurísticos iniciais para carry/tank/support/utility, derivados de chaves conhecidas em **effects**.

Itens augment (**isAugment**) e registros sem uma receita de dois componentes não são tratados como receitas craftáveis. Receitas duplicadas são rejeitadas explicitamente porque o contrato atual da engine não consegue representar duas saídas para o mesmo par de componentes. O limite atual de dez tipos de componentes também é validado.

## Limitações importantes

- **AD** no CommunityDragon é um modificador relativo ao dano de ataque base da unidade; por isso é preservado em **source_effects** e **não** convertido em **stats.attack_damage**, que representa um valor plano no contrato atual.
- Passivas e efeitos condicionais ficam preservados em **source_effects**, mas não são inventados como atributos permanentes. O catálogo, por si só, não implementa esses efeitos no **CombatEngine**.
- Os pesos de função são heurísticas, não rótulos oficiais da Riot nem uma estratégia treinada. Devem ser auditados e calibrados com testes/partidas.
- O script exige **--set** explicitamente. O Set 18 grava **data/itens.json** por padrão; os demais sets mantêm nomes específicos. A fonte bruta continua sendo o **itens.json** da raiz, distinto do catálogo em **data/itens.json**.
- O arquivo resultante inclui campos extras **source_*** para auditoria; o loader C++ atual ignora esses campos e lê os campos do contrato principal.

## Testes

```bash
python -m pytest tests/test_generate_item_catalog.py -q
```
