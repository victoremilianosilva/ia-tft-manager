# Catálogo, cópias e estoque de unidades

## Definição estática vs instância

A engine distingue `ChampionDefinition` de `UnitInstance`:

- **ChampionDefinition** contém dados do catálogo: IDs, nome, custo, traits, stats, perfil de combate, habilidade e ícones.
- **UnitInstance** representa uma cópia possuída: referência ao campeão, `champion_id`, UUID e estrelas.

Uma definição é compartilhada; cada cópia deve ter identidade própria. O nível de estrela pertence à instância, não à definição estática.

## Componentes

- `ChampionCatalog` carrega e valida o JSON e indexa por ID interno e `api_name`.
- `UnitInstanceFactory` cria instâncias a partir de IDs do catálogo e gera UUIDs.
- `UnitPool` mantém estoque inicial e disponível por campeão, impede retirada de estoque vazio e limita devoluções ao estoque original.
- `TftEngine.hpp` define estruturas compartilhadas usadas pelo lobby, pelos bindings e pela auditoria.

## Fonte de dados

O catálogo consumido pela engine é `data/units_gerado.json`. O arquivo `data/traits.json` fica ao lado dele e fornece os marcos de sinergia; o catálogo de itens fica em `data/item_catalog_set17.json`. A pasta `tests/diagnostico/` contém dados e ferramentas de inspeção separados, que não são os catálogos carregados pelo runtime. O catálogo precisa incluir os campos que a engine desserializa. O viewer também lê esse catálogo para associar IDs das unidades a nomes, traits, roles e ícones.

Não trate traits.json como substituto de units_gerado.json: são catálogos com formatos e finalidades diferentes.

## Invariantes

- IDs internos precisam ser estáveis dentro do catálogo carregado.
- `apiName` deve identificar unicamente a definição.
- A quantidade disponível não pode ficar negativa nem exceder a quantidade inicial.
- Comprar, vender e reiniciar a lobby devem atualizar o pool e a posse de cópias de forma consistente.
- UUIDs identificam instâncias, enquanto o ID de campeão identifica a definição.

Testes relacionados: `cpp/tests/test_unit_instance_factory.cpp`, `cpp/tests/test_unit_pool.cpp`, `cpp/tests/test_tft_engine_pool.cpp` e `tests/test_lobby_end_to_end.py`.
