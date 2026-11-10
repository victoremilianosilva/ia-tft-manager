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
- scripts/benchmark_runtime.py: mede o loop nativo completo de inferência + máscaras + execução de ambiente, com aquecimento, média/mediana/P95, IC bootstrap da média, throughput por agente, metadados de máquina e revisão Git.
- scripts/compare_runtime_benchmarks.py: compara vários JSONs independentes por revisão e exige configuração compatível; gera redução de latência e speedup de throughput.
- scripts/profile_mask_bottlenecks.py: perfila custo relacionado às máscaras; é complementar, não substitui throughput ponta a ponta.
- export_tensorboard.py: exporta métricas TensorBoard.
- tests/diagnostico/: inspeção da API nativa e geração/validação de catálogos.

Arquivos de profiling e relatórios existentes são artefatos de execuções específicas; não são benchmarks atuais sem repetir a medição.

## Benchmark de velocidade antes/depois

Compile a engine nativa em Release e execute os comandos na mesma máquina, com o mesmo Python/venv, configuração, carga do sistema e seed. Faça pelo menos três processos independentes por revisão; não execute ambos simultaneamente.

~~~powershell
# Em main (baseline), repetir 3 vezes e preservar cada resultado:
python scripts/benchmark_runtime.py --num-envs 4 --warmup 50 --iterations 300 --seed 20261027 --output reports/main-1.json
python scripts/benchmark_runtime.py --num-envs 4 --warmup 50 --iterations 300 --seed 20261027 --output reports/main-2.json
python scripts/benchmark_runtime.py --num-envs 4 --warmup 50 --iterations 300 --seed 20261027 --output reports/main-3.json

# Troque para a revisão candidata e repita com os mesmos argumentos:
python scripts/benchmark_runtime.py --num-envs 4 --warmup 50 --iterations 300 --seed 20261027 --output reports/candidate-1.json
python scripts/benchmark_runtime.py --num-envs 4 --warmup 50 --iterations 300 --seed 20261027 --output reports/candidate-2.json
python scripts/benchmark_runtime.py --num-envs 4 --warmup 50 --iterations 300 --seed 20261027 --output reports/candidate-3.json

python scripts/compare_runtime_benchmarks.py --baseline reports/main-1.json reports/main-2.json reports/main-3.json --candidate reports/candidate-1.json reports/candidate-2.json reports/candidate-3.json --output reports/runtime_comparison.json
~~~

O benchmark de runtime mede o loop de inferência e passo do ambiente, não o backpropagation/otimizador PPO nem o tempo total de treinamento. O script registra a revisão local reportada pelo Git; se estiver executando uma cópia exportada sem .git, o campo será nulo. O comparador rejeita configurações divergentes e resume a mediana das medianas/P95 de execuções independentes. A avaliação head-to-head continua sendo a ferramenta separada para qualidade da policy.
