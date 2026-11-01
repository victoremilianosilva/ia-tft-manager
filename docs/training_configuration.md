# Configuração do treinamento PPO

A configuração efetiva é centralizada em `TrainingConfig` (`training_config.py`).
Ela pode ser fornecida diretamente ao construtor:

```python
from trainer import Trainer
from training_config import TrainingConfig

config = TrainingConfig(
    learning_rate=2e-4,
    min_learning_rate=2e-5,
    lr_schedule_updates=800,
    entropy_coef_initial=0.02,
    entropy_coef_final=0.004,
    entropy_schedule_updates=800,
    batch_size=128,
    ppo_epochs=4,
    target_kl=0.025,
    rollout_steps=128,
)
trainer = Trainer(num_envs=4, config=config)
trainer.train(total_updates=800)
```

Também é possível sobrescrever parâmetros por variáveis de ambiente:

| Variável | Campo |
|---|---|
| `TFT_PPO_LR` | `learning_rate` |
| `TFT_PPO_MIN_LR` | `min_learning_rate` |
| `TFT_PPO_LR_SCHEDULE_UPDATES` | `lr_schedule_updates` |
| `TFT_PPO_ADAM_EPS` | `adam_eps` |
| `TFT_PPO_ADAM_BETA1` | `adam_beta1` |
| `TFT_PPO_ADAM_BETA2` | `adam_beta2` |
| `TFT_PPO_WEIGHT_DECAY` | `weight_decay` |
| `TFT_PPO_CLIP_COEF` | `clip_coef` |
| `TFT_PPO_ENT_COEF` | `entropy_coef_initial` |
| `TFT_PPO_ENT_COEF_FINAL` | `entropy_coef_final` |
| `TFT_PPO_ENT_DECAY_RATE` | `entropy_decay_rate` |
| `TFT_PPO_ENT_SCHEDULE_UPDATES` | `entropy_schedule_updates` |
| `TFT_PPO_VF_COEF` | `vf_coef` |
| `TFT_PPO_MAX_GRAD_NORM` | `max_grad_norm` |
| `TFT_PPO_TARGET_KL` | `target_kl` (`off` desabilita early stop) |
| `TFT_PPO_BATCH_SIZE` | `batch_size` |
| `TFT_PPO_EPOCHS` | `ppo_epochs` |
| `TFT_ROLLOUT_STEPS` | `rollout_steps` |
| `TFT_PPO_GAMMA` | `gamma` |
| `TFT_PPO_GAE_LAMBDA` | `gae_lambda` |
| `TFT_CHECKPOINT_PATH` | `checkpoint_path` |

Exemplo PowerShell:

```powershell
$env:TFT_PPO_LR = "0.0002"
$env:TFT_PPO_MIN_LR = "0.00002"
$env:TFT_PPO_BATCH_SIZE = "128"
$env:TFT_PPO_EPOCHS = "4"
$env:TFT_PPO_TARGET_KL = "0.025"
$env:TFT_PPO_ENT_COEF = "0.02"
$env:TFT_PPO_ENT_COEF_FINAL = "0.004"
$env:TFT_PPO_LR_SCHEDULE_UPDATES = "800"
$env:TFT_PPO_ENT_SCHEDULE_UPDATES = "800"
python trainer.py
```

## Retomada de checkpoint

Os pesos e os momentos do Adam são restaurados. O LR solicitado pela configuração atual
sempre prevalece sobre o LR armazenado no optimizer. O scheduler só é restaurado quando
LR, LR mínimo e horizonte coincidem com a configuração gravada no checkpoint; caso
contrário, começa uma nova curva com os parâmetros atuais. O progresso global do
scheduler e da entropia é mantido nos checkpoints compatíveis.

O checkpoint passa a armazenar também `training_config`. Um checkpoint antigo, sem
essa informação, mantém os pesos e pode restaurar os momentos do Adam, mas reinicia o
scheduler para evitar herdar silenciosamente uma curva desconhecida.

A configuração efetiva é registrada em `training/config` no TensorBoard e impressa no
início. Os diagnósticos PPO incluem minibatches tentados/processados, passos reais do
optimizer, early stop/KL e norma do gradiente antes do clipping.
