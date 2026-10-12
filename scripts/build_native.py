
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CPP_DIR = ROOT / "cpp"
BUILD_DIR = CPP_DIR / "build"


def run(command, *, env=None):
    print("\n>", " ".join(map(str, command)), flush=True)
    subprocess.run(
        list(map(str, command)),
        cwd=ROOT,
        env=env,
        check=True,
    )


def main():
    python = sys.executable

    # Confirma que o pybind11 pertence ao Python selecionado.
    pybind11_dir = subprocess.check_output(
        [python, "-m", "pybind11", "--cmakedir"],
        text=True,
    ).strip()

    run([
        "cmake",
        "-S", CPP_DIR,
        "-B", BUILD_DIR,
        f"-DPython_EXECUTABLE={python}",
        f"-Dpybind11_DIR={pybind11_dir}",
        "-DBUILD_TESTING=ON",
    ])

    run([
        "cmake",
        "--build", BUILD_DIR,
        "--config", "Release",
    ])

    # Executa os testes registrados no CTest.
    run([
        "ctest",
        "--test-dir", BUILD_DIR,
        "-C", "Release",
        "--output-on-failure",
    ])

    print("\nCompilação e testes concluídos.", flush=True)


if __name__ == "__main__":
    main()
