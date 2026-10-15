import pytest

from engine_backend import resolve_engine_backend


def test_python_is_the_default_backend(monkeypatch):
    monkeypatch.delenv("TFT_ENGINE_BACKEND", raising=False)
    assert resolve_engine_backend() == "python"


def test_environment_variable_selects_cpp(monkeypatch):
    monkeypatch.setenv("TFT_ENGINE_BACKEND", "cpp")
    assert resolve_engine_backend() == "cpp"


def test_explicit_argument_overrides_environment(monkeypatch):
    monkeypatch.setenv("TFT_ENGINE_BACKEND", "cpp")
    assert resolve_engine_backend("python") == "python"


@pytest.mark.parametrize("backend", ["PYTHON", " Cpp "])
def test_backend_selection_is_case_and_whitespace_tolerant(backend):
    expected = backend.strip().lower()
    assert resolve_engine_backend(backend) == expected


@pytest.mark.parametrize("backend", ["", "rust", "native", "true"])
def test_unknown_backend_is_rejected(backend):
    with pytest.raises(ValueError, match="engine_backend"):
        resolve_engine_backend(backend)
