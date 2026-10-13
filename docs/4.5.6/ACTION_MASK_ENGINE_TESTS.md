# Testes do ActionMaskEngine

## Objetivo

Validar o comportamento básico da geração de máscaras nativas antes de integrar o motor C++ aos managers Python e à política PPO.

## Cobertura

* Disponibilidade de `PASS`.
* Fallbacks técnicos sem habilitar ações reais.
* Compra condicionada a ouro, custo e disponibilidade.
* Venda condicionada à existência de unidades no banco.
* Movimentos do tabuleiro com origem e destino condicionados.
* Movimentos do banco para posições vazias do tabuleiro.
* Jogador eliminado com somente `PASS` disponível.
* Rejeição de estado econômico inválido.

## Compilar e executar no Windows

Na raiz do repositório, configure o projeto:

```powershell
cmake -S cpp -B cpp/build -DCMAKE_BUILD_TYPE=Release
```

Compile o novo teste:

```powershell
cmake --build cpp/build --config Release --target test_action_mask_engine
```

Execute somente o teste de máscaras:

```powershell
ctest --test-dir cpp/build -C Release -R action_mask_engine --output-on-failure
```

Execute todos os testes nativos:

```powershell
ctest --test-dir cpp/build -C Release --output-on-failure
```

## Critérios de aceitação

1. O projeto compila sem erros.
2. O teste `action_mask_engine` passa.
3. Os testes nativos já existentes continuam passando.
4. Fallbacks das máscaras não habilitam ações reais.
5. As dimensões e os índices permanecem compatíveis com o contrato da política PPO.

## Limitação

Esses testes validam regras isoladas do motor C++. A equivalência completa com `ActionMaskManager.py`, incluindo o histórico anti-loop real, ainda precisa ser validada antes de ativar o backend C++ no fluxo da partida.
