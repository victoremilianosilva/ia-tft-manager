# PPO Reference Protection

Esta camada é ativada automaticamente quando o checkpoint de entrada contém o metadado fine_tuning (ou quando já contém reference_protection). Ela não altera o processo dos dez fine-tunings; só protege a retomada do PPO geral.

## O que protege

1. **Âncora imutável:** o checkpoint final aprovado é a referência de pesos. Seu SHA-256 é validado em cada retomada.
2. **Trust region:** depois de cada update PPO, a policy inteira é projetada para permanecer dentro de um limite L2 relativo à âncora (padrão 2%). O limite é global, não por cabeça.
3. **Replay balanceado:** uma loss de imitação de baixa intensidade (padrão 0,01) usa ações determinísticas da policy aprovada em estados reais dos dez cenários treináveis. O replay exige cobertura mínima para todos os cenários e valida o hash da origem.
4. **Saída separada:** o PPO protegido não pode sobrescrever o checkpoint de entrada. Use TFT_CHECKPOINT_OUTPUT_PATH.
5. **Retomada conservadora:** por padrão, a primeira volta ao PPO reduz LR para no máximo 5e-5, min LR para no máximo 1e-5, clip para no máximo 0,10 e target KL para no máximo 0,01. Variáveis de ambiente explícitas continuam podendo sobrescrever esses valores.
6. **Regression gate:** compara partidas pareadas 4v4 espelhadas, exige seeds completas e estados iniciais iguais, mede ICs por seed (não trata oito assentos da mesma partida como oito observações independentes), verifica cobertura dos dez cenários e mede retenção das ações de referência. Nunca promove automaticamente.

## Fluxo após aprovar os dez fine-tunings

### 1. Coletar replay real do checkpoint final

Execute na raiz do repositório, usando o caminho do checkpoint final da cadeia:

~~~powershell
python -m ppo_protection.collect_reference_replay --checkpoint "CAMINHO_DO_CHECKPOINT_FINAL.pt" --output "ppo_protection/reference_replay.pt" --steps 500000 --min-per-scenario 32 --seed 20270101
~~~

O coletor só usa estados reais alcançados pela engine C++. Ele grava reference_replay.pt e reference_replay.coverage.json. Se algum cenário não atingir 32 exemplos, não use o replay: aumente --steps e execute novamente com um caminho de saída novo. Use apenas um arquivo cuja cobertura esteja completa; não há mesclagem automática de arquivos de replay.

### 2. Configurar o PPO geral

~~~powershell
$env:TFT_CHECKPOINT_PATH = "CAMINHO_DO_CHECKPOINT_FINAL.pt"
$env:TFT_CHECKPOINT_OUTPUT_PATH = "checkpoints/tft_ppo_continued_001.pt"
$env:TFT_REFERENCE_REPLAY_PATH = "ppo_protection/reference_replay.pt"
~~~

Depois execute o comando normal do projeto para instanciar Trainer e chamar train(). O trainer detecta o checkpoint fine-tuned, ativa as proteções e recusa iniciar se o replay estiver ausente/incompleto, tiver hash de origem diferente ou se o caminho de saída for igual ao checkpoint de entrada.

Em uma retomada posterior, use o último checkpoint PPO protegido como TFT_CHECKPOINT_PATH, um novo TFT_CHECKPOINT_OUTPUT_PATH, e mantenha o replay/âncora originais. Os metadados do checkpoint preservam a referência original, o hash e o replay.

### 3. Avaliar antes de promover

~~~powershell
.\ppo_protection\evaluate_ppo_candidate.ps1 -ReferenceCheckpoint "CAMINHO_DO_CHECKPOINT_FINAL.pt" -CandidateCheckpoint "checkpoints\tft_ppo_continued_001.pt" -Replay "ppo_protection\reference_replay.pt" -Coverage "ppo_protection\reference_replay.coverage.json" -SeedStart 20270101 -SeedCount 50 -MinSeeds 50
~~~

O resultado JSON tem promotion_allowed e checks; approved permanece sempre false. Um resultado bloqueado exige investigação/novo treino. Mesmo quando elegível, a revisão humana continua obrigatória.

## Limitações deliberadas

- Os traces dos fine-tunings anteriores não armazenam a observação bruta nem todas as máscaras; por isso, o replay é coletado novamente depois da cadeia, não reconstruído artificialmente dos JSONL antigos.
- A engine não oferece injeção pública de estados. O coletor minera cenários naturalmente; não encontrar um cenário significa falta de cobertura, não aprovação.
- A projeção de pesos limita drift, mas não é uma prova matemática de equivalência comportamental. Por isso existem replay, avaliação pareada e portão de regressão.
- A avaliação de partidas mede desempenho agregado. A retenção por cenário é medida separadamente no conjunto de replay, com concordância de tipo de ação. Concordância não prova que a ação é ótima; o relatório continua sujeito a revisão humana.
