$ErrorActionPreference = "Stop"

# Teste comparável de aproximadamente 10 minutos.
# A duração real depende do hardware, do checkpoint e das partidas.
$env:TFT_ENGINE_BACKEND = "cpp"
python -c "from trainer import Trainer; t=Trainer(num_envs=4, use_subprocess=False); t.train(total_updates=300, rollout_steps=128)"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
