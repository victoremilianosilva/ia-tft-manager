# Contrato AntiLoop

## Objetivo

Documentar as regras que impedem movimentos repetitivos durante a geração de Action Masks, sem confundir consulta de candidatos com execução real de uma ação.

A implementação Python é a referência inicial. A versão C++ deve reproduzir o comportamento atual antes de qualquer alteração deliberada de regra.

## Responsabilidades

- Detectar bloqueios explícitos, reversões, oscilações, ciclos entre banco e tabuleiro e ciclos gerais.
- Construir identidades de unidade, chaves de movimento e assinaturas espaciais consistentes.
- Manter histórico, visitas, bloqueios e métricas conforme o ciclo de vida atual.
- Explicar o motivo do bloqueio sem registrar uma execução que não ocorreu.

## Precedência dos bloqueios

A ordem identificada na documentação de análise é:

1. Bloqueio explícito.
2. Movimento reverso.
3. Oscilação.
4. Ciclo entre banco e tabuleiro.
5. Ciclo geral.
6. Sem bloqueio, caso nenhuma regra anterior se aplique.

Essa precedência afeta o motivo retornado quando mais de uma regra reconhece o mesmo candidato. Deve ser confirmada contra o código Python atual antes de ser tratada como contrato congelado.

## Identidade e assinaturas

A identidade da unidade, a chave do movimento e a assinatura do tabuleiro precisam usar os mesmos campos, valores padrão, ordenação e tratamento de valores ausentes nas duas implementações.

As seguintes distinções são importantes e precisam ser testadas:

- Unidade com UUID versus unidade sem UUID.
- Unidade sem UUID identificada por `id + star`, conforme a implementação Python atual.
- Valor padrão de estrela quando o campo não existe.
- Posições vazias versus ocupadas.
- Assinatura espacial igual com economia diferente.

Não se deve acrescentar ouro, XP ou loja à assinatura espacial se a implementação atual não os inclui.

## Consultas e mutações

Consultas como `should_block_move`, `get_block_reason`, detecção de reversão, oscilação e ciclo não devem atualizar o histórico oficial nem contabilizar uma execução, salvo se o comportamento atual documentar explicitamente algum efeito colateral de diagnóstico.

A atualização do histórico deve ocorrer no ponto correto do fluxo real:

- Tentativa de execução;
- Bloqueio durante execução;
- Movimento concluído com sucesso;
- Falha ou rollback.

Um candidato aceito pela máscara não equivale a um movimento executado. Não registrar sucesso durante a geração de máscaras.

## Histórico, limites e reset

A migração deve preservar:

- A ordem dos registros, pois ela influencia as regras de detecção.
- Os limites de capacidade e a remoção dos registros mais antigos.
- A associação entre bloqueios e assinaturas de estado.
- A contagem de visitas e o limiar de repetição.
- Os contadores que são limpos no reset e os que permanecem acumulados.

Esses comportamentos devem ser verificados no código e nos testes atuais, sem inferir a semântica apenas pelos nomes dos métodos.

## Falhas e fallback

A análise atual registra que uma exceção em uma consulta AntiLoop pode ser capturada pelo gerador de máscaras e permitir que o candidato continue naquela camada. Esse comportamento é relevante para equivalência, mas precisa ser confirmado no código atual.

A integração C++ deve ter uma política explícita para erros. Não deve transformar silenciosamente qualquer falha em “movimento válido”, nem ocultar falhas nativas com fallback indiscriminado.

## Testes mínimos

- Histórico vazio.
- Reversão de movimento e reversão de troca.
- Oscilação dentro e fora da janela de histórico.
- Ciclo banco ↔ tabuleiro.
- Ciclo geral.
- Bloqueio explícito no mesmo estado e após mudança de estado.
- Candidato que corresponde a mais de uma regra, para verificar precedência.
- Identidades com e sem UUID.
- Histórico no limite de capacidade.
- Consultas repetidas sem mutação.
- Tentativa bloqueada, movimento bem-sucedido, falha, rollback e reset.
- Exceção controlada durante a geração de máscaras.

## Referências

- `contrato_atual.md`: comportamento atual observado.
- `casos_referencia.md`: cenários detalhados de comparação.
- `criterios_objetivos.md`: critérios de equivalência.
- `estrategia_faallback.md`: comportamento de fallback e rollback.
- `4.5.2/`: contratos nativos, convenções e build do módulo C++.
