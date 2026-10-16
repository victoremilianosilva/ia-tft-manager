# Assets do TFT Viewer

Esta pasta armazena os diagramas e wireframes referenciados por [TFT_VIEWER_PLAN.md](../TFT_VIEWER_PLAN.md).

- architecture.svg — arquitetura proposta e fluxo entre PPO, controlador, engine, replay e interface.
- dashboard-wireframe.svg — visão geral com oito cartões, cada um contendo o tabuleiro completo 7×4 e posições individuais das peças.
- combat-view.svg — novo wireframe da batalha detalhada, com todas as unidades dos dois lados, barras de HP/mana, posições, roster, timeline e controles; os dados são ilustrativos e a atualização real depende dos eventos/snapshots da engine.
- event-lifecycle.svg — sequência de auditoria de uma decisão individual.

Os SVGs são ilustrações vetoriais versionáveis e editáveis. São diagramas de planejamento, não screenshots do aplicativo implementado. Sempre que uma decisão de arquitetura ou interface mudar, atualizar os SVGs e o documento principal na mesma alteração.