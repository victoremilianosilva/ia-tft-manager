# Decision Engine — Compilação, Importação e Testes

## Objetivo

Documentar como compilar os módulos C++ com o ambiente Python do projeto, executar os testes automatizados e importar o `decision_engine`.

## Pré-requisitos

- Python utilizado pelo projeto, com o ambiente virtual ativado.
- CMake 3.20 ou superior.
- Compilador C++ compatível com C++20.
- `pybind11` instalado no ambiente Python selecionado.

Instale as dependências Python a partir da raiz do projeto:

```powershell
python -m pip install -r requirements.txt
```

Confirme as ferramentas:

```powershell
python --version
python -m pybind11 --cmakedir
cmake --version
```

## Compilação

Na raiz do repositório, execute:

```powershell
python scripts/build_native.py
```

O script configura o CMake com o interpretador Python atual, compila os alvos e executa os testes registrados no CTest.

O diretório de build é `cpp/build`.

## Execução dos testes isoladamente

Depois de configurar e compilar:

```powershell
ctest --test-dir cpp/build -C Release --output-on-failure
```

O teste `decision_error_contract` valida o contrato de erros nativo.

O teste `decision_engine_import` verifica se o módulo pode ser importado pelo interpretador selecionado na compilação.

## Importação manual

O módulo é gerado no diretório de saída configurado pelo alvo CMake. Para importá-lo, esse diretório precisa estar no `PYTHONPATH`.

Exemplo em PowerShell, caso o módulo esteja em `cpp/build/bin`:

```powershell
$env:PYTHONPATH = "$PWD\cpp\build\bin"
python -c "import decision_engine; print(decision_engine.__doc__)"
```

O caminho real deve corresponder ao diretório de saída configurado no CMake. Em builds com configurações específicas, como Visual Studio, confira também o subdiretório `Release`.

## Critérios de aceitação

- O CMake utiliza o Python do ambiente virtual selecionado.
- Os módulos nativos compilam sem depender de caminhos pessoais fixos.
- O CTest executa os testes nativos.
- O teste de importação usa o mesmo interpretador Python da compilação.
- A compilação e os testes não exigem inicializar o ambiente PPO ou executar treinamento.

## Limites

A aprovação desses testes não comprova a equivalência funcional entre as implementações Python e C++. Essa validação pertence aos testes de integração e comparação de resultados.