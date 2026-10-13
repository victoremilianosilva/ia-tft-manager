# Contrato entre TFT Engine e Combat Engine

**Versão:** 1.0  
**Linguagem:** C++  
**Objetivo:** integrar o motor de combate ao motor de lobby, preservando o comportamento funcional do TFT original e reduzindo overhead de processamento e alocação.

## 1. Responsabilidades

### TFT Engine (`TFTEngine`)

Responsável por:
- Gerenciar os oito jogadores da lobby.
- Preparar as equipes a partir das unidades posicionadas no tabuleiro.
- Resolver confrontos entre jogadores.
- Aplicar o resultado do combate ao estado da partida.
- Calcular o dano ao jogador perdedor.
- Atualizar vitórias, derrotas, economia, recompensas, eliminações e classificação.
- Controlar o avanço de rounds e stages.

### Combat Engine (`CombatEngine`)

Responsável por:
- Receber os dados de duas equipes.
- Validar a entrada necessária para a simulação.
- Executar o combate.
- Determinar o vencedor, empate e sobreviventes.
- Retornar estatísticas por equipe e unidade.
- Registrar eventos detalhados somente quando solicitados.

O `CombatEngine` não deve modificar diretamente jogadores, economia, recompensas, classificação ou estado da lobby.

## 2. Interface pública

A interface principal deve continuar compatível com os tipos já definidos em `CombatInput.hpp` e `CombatResult.hpp`.

```cpp
namespace tft {

class CombatEngine {
public:
    CombatEngine() = default;

    [[nodiscard]]
    CombatResult simulate(const CombatInput& input) const;
};

}
```

O `TFTEngine` deve possuir uma instância reutilizável do `CombatEngine`, preferencialmente dentro de sua implementação privada (`Impl`).

```cpp
struct TFTEngine::Impl {
    CombatEngine combat_engine;

    // Estado da lobby e dos jogadores.
};
```

A instância não deve ser reconstruída a cada confronto. Como a interface atual de `CombatEngine` é `const` e não mantém estado de combate entre chamadas, ela pode ser reutilizada.

## 3. Contrato de entrada: `CombatInput`

O `TFTEngine` monta um `CombatInput` para cada confronto.

### Campos obrigatórios

- `player_a`: dados da primeira equipe.
- `player_b`: dados da segunda equipe.
- `context`: tipo de combate, como `PVP` ou `PVE`.
- `config`: dimensões do tabuleiro, limites da simulação e opções de registro.
- `seed`: semente determinística, conforme a política de RNG definida na configuração.

### Dados de cada equipe

Cada `CombatTeam` deve informar:
- Identificador da equipe (`PLAYER_A` ou `PLAYER_B`).
- Identificador do jogador.
- HP atual do jogador.
- Unidades vivas que participarão do confronto.

Cada `CombatUnit` deve transportar os atributos de combate disponíveis no modelo atual: ID, posição, estrelas, HP, ataque, velocidade, alcance, defesa, mana, habilidade, itens, traits e modificadores.

### Regras do contrato

1. Os IDs das unidades devem ser únicos dentro do combate inteiro, não apenas dentro de cada equipe.
2. A identificação de equipe de cada unidade deve corresponder à equipe que a contém.
3. A posição deve respeitar as dimensões definidas em `CombatConfig`.
4. Os atributos indispensáveis à simulação devem ser válidos e finitos.
5. Os dados de entrada pertencem ao `TFTEngine`; o `CombatEngine` não deve alterar o tabuleiro original.
6. A entrada deve conter somente unidades participantes do confronto.

O `TFTEngine` deve preencher os campos diretamente a partir do estado interno das unidades, sem criar representações intermediárias desnecessárias.

## 4. Contrato de saída: `CombatResult`

O `CombatEngine` retorna um resultado independente do estado da lobby.

### Resultado obrigatório

| Campo | Significado |
|---|---|
| `success` | Indica se a operação foi aceita e executada sem erro de entrada ou execução. |
| `completed` | Indica se a simulação chegou a um estado terminal válido. |
| `timeout` | Indica que um limite de duração ou de eventos foi atingido. |
| `winner` | `PLAYER_A`, `PLAYER_B` ou `DRAW`. |
| `player_a_survivors` | Quantidade de unidades sobreviventes da equipe A. |
| `player_b_survivors` | Quantidade de unidades sobreviventes da equipe B. |
| `player_a_deaths` | Quantidade de unidades da equipe A que morreram durante o combate. |
| `player_b_deaths` | Quantidade de unidades da equipe B que morreram durante o combate. |
| `duration` | Duração simulada do confronto. |
| `units` | Estatísticas finais das unidades, identificadas por ID. |

### Estatísticas das unidades

Cada `CombatUnitResult` deve identificar a unidade e sua equipe, informando sobrevivência, HP inicial e final, dano causado e recebido, eliminações, ataques, habilidades utilizadas e posição final.

Quando uma estatística não for suportada pela implementação atual, ela deve ter uma semântica documentada e consistente. Não se deve apresentar um valor padrão como se fosse uma estatística calculada.

### Semântica de erro

- Se `success == false`, o `TFTEngine` não aplica o resultado à partida.
- O erro deve incluir `error_code` e `error_message`.
- Se `timeout == true`, o resultado não deve ser tratado automaticamente como uma vitória normal.
- `completed == true` somente pode indicar um combate encerrado de acordo com a política de término definida.
- Um resultado incompleto ou inválido não pode alterar HP, economia, recompensas ou classificação dos jogadores.

## 5. Contrato de eventos

O registro de eventos deve ser opcional para reduzir alocações no treinamento da IA.

- `record_events`: eventos genéricos.
- `record_damage`: eventos detalhados de dano.
- `record_positions`: mudanças de posição.
- `record_abilities`: eventos de habilidades.
- Demais flags: devem preservar a semântica definida em `CombatConfig`.

Quando o registro estiver desativado, os vetores de eventos correspondentes devem permanecer vazios. O resultado principal — vencedor, sobreviventes e estatísticas necessárias — não pode depender de o registro estar habilitado.

Os eventos devem usar IDs de unidades estáveis, timestamps relativos ao combate e tipos documentados.

## 6. Fluxo de resolução

O fluxo esperado no `TFTEngine` é:

1. Selecionar os dois jogadores que se enfrentarão.
2. Obter as unidades vivas de seus tabuleiros.
3. Resolver equipes vazias sem executar uma simulação desnecessária:
   - Ambas vazias: empate, sem dano ou recompensa de vitória.
   - Apenas A vazia: vitória de B.
   - Apenas B vazia: vitória de A.
4. Se ambas tiverem unidades, construir `CombatInput`.
5. Executar `combat_engine.simulate(input)`.
6. Validar `success`, `completed` e `timeout`.
7. Interpretar `winner` e as quantidades de sobreviventes.
8. Converter o resultado para a representação interna do confronto da lobby.
9. Aplicar vitórias, derrotas, recompensas e dano ao jogador perdedor.
10. Atualizar eliminações e classificação no fluxo normal da lobby.

O `CombatEngine` não deve calcular novamente as regras de economia, recompensas ou eliminação que pertencem ao `TFTEngine`.

## 7. Regras de dano e empate

O comportamento de referência do Python deve ser preservado:

- O dano ao jogador perdedor é calculado pela lobby com base no dano do stage e na quantidade de unidades sobreviventes do vencedor.
- O vencedor não recebe dano de jogador nesse confronto.
- Empates não geram dano de jogador nem recompensa de vitória ou derrota.
- As recompensas são calculadas uma única vez por resultado.
- A eliminação acontece no fluxo da lobby após a aplicação do dano.
- Vitórias, derrotas, streaks e economia continuam sendo responsabilidade da lobby.

O campo `player_a_damage` ou `player_b_damage` do `CombatResult` não deve substituir essa regra enquanto o contrato não definir explicitamente que o motor de combate é responsável por esse cálculo.

## 8. Otimizações permitidas

As seguintes otimizações não devem alterar o comportamento observável:

- Reutilizar a instância de `CombatEngine`.
- Passar a entrada por referência constante.
- Evitar conversões Python/C++ no fluxo nativo.
- Desabilitar logs e eventos detalhados durante treinamento normal.
- Reservar capacidade de vetores quando o tamanho esperado for conhecido.
- Reutilizar buffers internos somente quando isso não introduzir estado compartilhado entre combates.
- Evitar percorrer repetidamente as mesmas unidades para obter estatísticas que podem ser acumuladas durante a simulação.

A otimização não pode mudar o vencedor, as quantidades de sobreviventes, as regras de dano da lobby ou a política de RNG determinística para uma mesma entrada.

## 9. Critérios de aceitação

A integração será considerada contratualmente válida quando:

1. `TFTEngine` chamar `CombatEngine::simulate()` diretamente em C++.
2. Os tipos e namespaces usados na chamada coincidirem com os headers públicos.
3. As equipes e unidades forem convertidas corretamente do estado interno da lobby.
4. O resultado representar corretamente o vencedor, o empate e os sobreviventes.
5. Erros e timeouts não forem confundidos com combates normais concluídos.
6. Os casos de equipes vazias preservarem o comportamento de referência.
7. O dano, as recompensas e as eliminações forem aplicados uma única vez.
8. O registro opcional de eventos não alterar o resultado principal.
9. Os testes de integração cobrirem vitória A, vitória B, empate, equipes vazias, erro de entrada e timeout.

**Princípio final:** `CombatEngine` resolve o confronto entre unidades; `TFTEngine` resolve as consequências desse confronto para a partida.
