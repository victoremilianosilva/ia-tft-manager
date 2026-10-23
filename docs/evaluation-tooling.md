# Avaliação de checkpoints e ferramentas

## Head-to-head

scripts/evaluate_checkpoints.py compara dois checkpoints sem treinar nenhum deles. Em cada partida, quatro vagas usam a policy candidata e quatro a baseline; as vagas candidatas rotacionam entre partidas para reduzir viés de assento. A avaliação é determinística e usa seeds diferentes por partida.

A saída CSV registra seed, jogador, versão (baseline/candidate), colocação, vitória, rodada e assentos candidatos. O script exige colocação para os oito jogadores; não inventa ranking ausente.

Exemplo PowerShell:

~~~powershell
python scripts/evaluate_checkpoints.py --baseline checkpoints/baseline.pt --candidate tft_checkpoint.pt --matches 40 --seed 20261015 --output reports/head_to_head.csv --json-output reports/head_to_head_summary.json
~~~

Ajuste os caminhos aos checkpoints disponíveis no ambiente local.

O CSV mantém os resultados por jogador. O JSON adicional agrega baseline e candidata, calcula deltas pareados por seed para colocação média, taxa de vitória e top 4, e inclui intervalos de confiança de 95% por bootstrap das seeds. Uma diferença negativa em colocação média favorece a candidata; diferenças positivas em vitória/top 4 favorecem a candidata. Esses intervalos descrevem a variação observada entre seeds e não provam causalidade.

Para comparações futuras, mantenha o mesmo --seed inicial, a mesma quantidade de partidas, a mesma versão da engine e a mesma configuração de avaliação. Use checkpoints compatíveis com a dimensão atual da observação e com a arquitetura de TFTPolicy; o script falha em vez de migrar silenciosamente pesos incompatíveis.

## Outras ferramentas

- scripts/build_native.py: configura CMake com o Python/pybind11 selecionado, compila Release e executa CTest.
- benchmark_real_throughput.py: mede throughput real do caminho de execução.
- profile_mask_bottlenecks.py: perfila custo relacionado às máscaras.
- export_tensorboard.py: exporta métricas TensorBoard.
- tests/diagnostico/: inspeção da API nativa e geração/validação de catálogos.

Arquivos de profiling e relatórios existentes são artefatos de execuções específicas; não são benchmarks atuais sem repetir a medição.
