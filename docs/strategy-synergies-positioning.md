# Estratégia, sinergias e posicionamento

## Posicionamento

`PositioningEngine` avalia a formação no tabuleiro 4 × 7 usando perfis/roles e posições. A linha 0 é tratada como frontline e a linha 3 como backline. A avaliação considera proteção de carries: tanques oferecem a proteção mais forte; fighters à frente contam como proteção parcial. O classificador de papéis usa fighter como desempate quando faltam sinais, evitando que um perfil sem dados vire tank por ordem do enum. O resultado alimenta observações e recompensas; não é o motor que simula ataques e movimentação durante o combate.

## Sinergias

`SynergyCounter` conta traits das unidades e `SynergyEngine` acompanha contagens ativas/parciais, marcos e nível de trait. `CompositionPlanner` usa os marcos do set carregado para pontuar o ganho marginal de completar cada breakpoint: composições com sinergias fechadas (por exemplo, 2/4/6 quando esses forem os marcos reais) devem vencer uma distribuição que só espalha traits sem ativá-las. Os marcos nunca devem ser presumidos universais: a lista vem dos dados do set atual.

## Contexto estratégico

`StrategyInfo` é um snapshot de estratégia para observação e diagnóstico: estratégia atual/anterior, confiança, idade, motivo, scores, poder do tabuleiro, força do banco, contagem de traits ativas e informações de foco/composição. A interface de treino pode registrar contagens de estratégia sem manter uma policy separada por jogador: a policy PPO é compartilhada pelos assentos.

## Integração

A estratégia não substitui as regras legais da engine. Ela informa estado/heurísticas; as ações continuam sujeitas às máscaras e à validação. Mudanças em traits, foco ou posicionamento precisam ser avaliadas com o catálogo e as recompensas atuais.

Testes relacionados: `cpp/tests/test_synergy_counter.cpp`, `tests/test_action_mask_validation.py` e testes de paridade de sinergia, quando aplicáveis.
