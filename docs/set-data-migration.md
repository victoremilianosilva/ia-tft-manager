# Migração de dados do TFT por set

O catálogo do jogo deve vir dos dados publicados pelo CommunityDragon, não de listas montadas manualmente. O script scripts/migrate_set_data.py baixa a exportação atual e gera os arquivos normalizados consumidos pelo projeto.

## Atualizar para o Set 18

Na raiz do repositório:

```bash
python scripts/migrate_set_data.py --set 18
```

Para reproduzir a migração a partir de um JSON já baixado:

```bash
python scripts/migrate_set_data.py --set 18 --input path/to/en_us.json
```

Saídas:
- data/units_gerado.json: campeões compráveis de custo 1–5, estatísticas, habilidades e traits.
- data/traits.json: traits do set, breakpoints publicados e associação de campeões.
- data/item_catalog_set18.json: catálogo normalizado de componentes e itens craftáveis.
- data/set18_manifest.json: nome do set e contagens para auditoria.

O script seleciona o set explicitamente por número, mescla variantes de setData, remove duplicatas por apiName e filtra unidades que não são campeões compráveis. Nomes, descrições, ícones e efeitos de origem são preservados sempre que disponíveis.

## Limitações que precisam ser respeitadas

- O endpoint latest é mutável. Para reprodução bit-a-bit, arquive também o JSON de origem e seu SHA-256.
- O normalizador de itens reutiliza scripts/generate_item_catalog.py. Passivas e efeitos que a engine de combate ainda não implementa continuam sendo metadados; importar JSON não implementa automaticamente esses efeitos.
- As funções/roles dos campeões começam neutras e são recalculadas pelo classificador da engine, evitando reutilizar classificações antigas do Set 17.
- O gerador não roda durante o treino: os arquivos de dados gerados devem ser revisados e versionados.

Testes:

```bash
python -m pytest tests/test_migrate_set_data.py tests/test_generate_item_catalog.py -q
```
