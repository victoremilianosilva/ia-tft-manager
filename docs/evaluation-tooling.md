# Avaliação de checkpoints e ferramentas

## Head-to-head

scripts/evaluate_checkpoints.py compara dois checkpoints sem treinar nenhum deles. Em cada partida, quatro vagas usam a policy candidata e quatro a baseline; as vagas candidatas rotacionam entre partidas para reduzir viés de assento. A avaliação é determinística e usa seeds diferentes por partida.

A saída CSV registra seed, jogador, versão (baseline/candidate), colocação, vitória, rodada e assentos candidatos. O script exige colocação para os oito jogadores; não inventa ranking ausente.

Exemplo PowerShell:

~~~powershell
python scripts/evaluate_checkpoints.py --baseline checkpoints/baseline.pt --candidate tft_checkpoint.pt --matches 40 --output reports/head_to_head.csv
~~~

Ajuste os caminhos aos checkpoints disponíveis no ambiente local.

## Outras ferramentas

- scripts/build_native.py: configura CMake com o Python/pybind11 selecionado, compila Release e executa CTest.
- benchmark_real_throughput.py: mede throughput real do caminho de execução.
- profile_mask_bottlenecks.py: perfila custo relacionado às máscaras.
- export_tensorboard.py: exporta métricas TensorBoard.
- tests/diagnostico/: inspeção da API nativa e geração/validação de catálogos.

Arquivos de profiling e relatórios existentes são artefatos de execuções específicas; não são benchmarks atuais sem repetir a medição.
