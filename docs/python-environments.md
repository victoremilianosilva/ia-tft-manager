# Ambientes Python e bindings nativos

## CppTFTLobbyWrapper

cpp_lobby_env.py cria a extensão nativa tft_engine, expõe reset/step, normaliza ações para seis inteiros, converte observações e recompensas para arrays NumPy e encaminha consultas de máscaras, estratégias, métricas anti-loop, estado público e snapshot de auditoria. A engine C++ é o backend usado pelo treinador e pelo viewer.

step(actions) espera oito ações. O retorno contém observações, recompensas, flag de conclusão da lobby e informação com jogadores, rodada/estágio, eventos e componentes de recompensa.

## LobbyVectorEnv

vector_lobby_env.py instancia um ambiente por lobby. O reset retorna observações com forma (num_lobbies, 8, obs_dim). O step retorna observações, rewards e dones com eixos lobby/jogador, além de um info por lobby.

Dones individuais são marcados quando um jogador é eliminado. Ao terminar uma lobby, o wrapper captura estado terminal/ranking antes do reset automático do ambiente.

O wrapper é serial no código atual; use_subprocess não transforma LobbyVectorEnv em execução multiprocessada.

## Binding

cpp/bindings/tft_engine_bindings.cpp e cpp/bindings/combat_engine_bindings.cpp expõem APIs nativas para Python. O módulo compilado precisa estar no caminho de importação. O contrato inclui IDs de ações, shapes, tipos numéricos e formatos de snapshots.

## Fechamento de recursos

Ambientes nativos têm close(). Ferramentas e testes devem chamá-lo em finally ou no encerramento da sessão. Não feche uma engine enquanto step estiver ativo em outra thread.

Consulte [build e testes](build-and-tests.md).
