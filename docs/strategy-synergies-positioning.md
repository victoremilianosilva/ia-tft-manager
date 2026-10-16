# Estratégia, sinergias e posicionamento

## Posicionamento

`PositioningEngine` avalia a formação no tabuleiro 4 × 7 usando perfis/roles e posições. O resultado é uma métrica de posicionamento usada pela engine de lobby e pelos sinais de recompensa. Essa avaliação não deve ser confundida com o motor que simula ataques e movimentação durante o combate.

## Sinergias

`SynergyCounter` conta traits das unidades e `SynergyEngine` acompanha contagens ativas/parciais, marcos e nível de trait. A engine pode calcular multiplicadores/bonificações por nível e bônus de unidade conforme as traits presentes. A lista de traits e marcos deve corresponder ao set do catálogo carregado; não presumir que nomes ou limites são universais entre sets.

## Contexto estratégico

`StrategyInfo` é um snapshot de estratégia para observação e diagnóstico: estratégia atual/anterior, confiança, idade, motivo, scores, poder do tabuleiro, força do banco, contagem de traits ativas e informações de foco/composição. A interface de treino pode registrar contagens de estratégia sem manter uma policy separada por jogador: a policy PPO é compartilhada pelos assentos.

## Integração

A estratégia não substitui as regras legais da engine. Ela informa estado/heurísticas; as ações continuam sujeitas às máscaras e à validação. Mudanças em traits, foco ou posicionamento precisam ser avaliadas com o catálogo e as recompensas atuais.

Testes relacionados: `cpp/tests/test_synergy_counter.cpp`, `tests/test_action_mask_validation.py` e testes de paridade de sinergia, quando aplicáveis.
