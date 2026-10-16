# Engine TFT: C++ como fonte única

A engine de jogo agora é exclusivamente nativa C++. O estado da partida, regras
da lobby, economia, loja, pool compartilhado, combate, recompensas, observações
e máscaras são responsabilidade dos módulos em `cpp/`. O arquivo
`cpp_lobby_env.py` é somente um adaptador para o PPO e não implementa regras
de jogo.

O seletor `TFT_ENGINE_BACKEND`, a factory `engine_backend.py` e a implementação
da lobby Python foram removidos. O PPO, a policy, o rollout, os relatórios e o
visualizador continuam em Python porque são infraestrutura/aplicação, não uma
segunda implementação da engine.

## Build e testes

```bash
python -m pip install numpy torch tensorboard pybind11 pytest
cmake -S cpp -B cpp/build -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=ON
cmake --build cpp/build --parallel 2
ctest --test-dir cpp/build --output-on-failure
PYTHONPATH="cpp/build/bin:." python -m pytest -q tests/test_tft_engine_api.py tests/test_lobby_end_to_end.py
```

## Nota sobre paridade histórica

A remoção da referência Python não é, por si só, uma prova matemática de
equivalência com todos os comportamentos históricos. Os documentos de auditoria
em `docs/` e seus registros de lacunas continuam como histórico técnico. A
validação daqui em diante deve exercitar invariantes e cenários reproduzíveis
diretamente na engine C++, sem manter uma segunda engine de jogo Python.
