# Relatório de performance — treinamento PPO

## Diagnóstico confirmado no código

A revisão do fluxo de treino identificou um gargalo estrutural: `Trainer`
aceitava `use_subprocess`, mas sempre construía `LobbyVectorEnv` no processo
principal. O método `LobbyVectorEnv.step()` percorria as lobbies em sequência.
Assim, aumentar `num_lobbies` aumentava o trabalho serial de simulação.

O loop PPO, a policy compartilhada e o armazenamento do rollout permanecem no
processo principal. A engine C++ continua sendo responsável pelo estado e pelas
regras de cada partida.

## Alteração desta PR

- Um processo persistente por lobby, usando o contexto `spawn` (compatível com
  Windows) e uma engine C++ criada dentro do worker.
- Dispatch em lote: todos os workers recebem `step` antes de o processo principal
  aguardar os resultados, permitindo que lobbies distintas avancem em paralelo.
- Chamadas `reset` e `env_method` também são encaminhadas aos workers.
- `use_subprocess=False` mantém o modo serial para depuração, testes e comparação.
- Policy, PPO, rollout, observações, recompensas, dones e semântica de lobby
  continuam centralizados e com as mesmas dimensões.

## Como medir na máquina de treino

Após compilar a extensão C++:

```powershell
python scripts/benchmark_lobby_parallelism.py --lobbies 1,2,4 --steps 100 --warmup 10 --output reports/lobby_parallelism.json
```

O benchmark executa o mesmo workload de ações PASS em modo serial e subprocesso,
desconta o aquecimento e grava tempo total, tempo médio por passo, lobbies/s e
transições de agentes/s. Execute com a mesma versão do binário, número de lobbies,
configuração de CPU e carga de fundo para comparar.

## Limitações e interpretação

- Não há speedup numérico declarado nesta PR: o benchmark precisa ser executado
  no hardware que fará o treinamento.
- O paralelismo pode aumentar o uso de RAM e o custo de IPC; lobbies pequenas ou
  CPUs com poucos núcleos podem não ganhar desempenho.
- A policy continua em CPU nesta alteração. Não foi feita migração para GPU,
  alteração de arquitetura da rede, recompensa, estratégia ou engine de combate.
- Em scripts Python no Windows, a criação de processos deve ocorrer sob
  `if __name__ == "__main__":`. O `Trainer` mantém a opção
  `use_subprocess=False` para ambientes que não suportem spawn.


## Remoção de telemetria de anti-loop e máscaras

O caminho PPO deixa de consultar/exportar contadores de anti-loop e auditorias
de máscaras para o TensorBoard. Também foi removida a conversão desses
contadores no binding Python/C++ e o método público dedicado exclusivamente
a essa telemetria.

**Importante:** as máscaras de ação que a policy consome continuam sendo
geradas pela engine e consultadas pelo Trainer. Os validadores de ações,
bloqueios anti-loop, prevenção de ciclos e demais regras nativas continuam
ativos. Esta alteração remove somente diagnóstico/telemetria, não controles
que afetam decisões ou a legalidade das ações.

A expectativa é reduzir sincronizações, conversões, alocações e IPC por lobby
e por passo. O ganho exato será medido no benchmark; não é presumido.
