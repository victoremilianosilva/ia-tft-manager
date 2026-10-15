
#pragma once

// Entrada e resultado padronizados do motor de combate.
#include "CombatInput.hpp"
#include "CombatResult.hpp"

namespace tft {

/**
 * @brief Executa uma simulação determinística de combate em C++.
 *
 * Recebe equipes, posições, atributos e configuração através de CombatInput,
 * e devolve o resultado e os eventos através de CombatResult. O lobby Python
 * e a lobby nativa usam este mesmo motor. A simulação atual resolve movimento
 * e ataques básicos; os campos de habilidade, itens e traits ainda não são
 * consumidos pelo loop de combate e não devem ser considerados mecânicas ativas.
 */
class CombatEngine {
public:
    // Construtor padrão: o motor ainda não precisa manter estado
    // entre diferentes chamadas de simulação.
    CombatEngine() = default;

    /**
     * @brief Valida a entrada e simula o confronto.
     * @param input Dados das equipes, unidades e configurações.
     * @return Resultado com vencedor, sobreviventes, dano, eventos e status.
     */
    CombatResult simulate(const CombatInput& input) const;
};

} // namespace tft