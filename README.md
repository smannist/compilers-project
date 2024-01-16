
## Setup

Requirements:

    - [Pyenv](https://github.com/pyenv/pyenv) for installing Python 3.11+
    - [Poetry](https://python-poetry.org/) for installing dependencies

Easy Pyenv setup:

    # Install curl
    sudo apt install curl

    # Install Pyenv
    bash <(curl -sSL https://raw.githubusercontent.com/zaemiel/ubuntu-pyenv-installer/master/ubuntu-pyenv-installer.sh)

Install dependencies:

    # Install Python specified in `.python-version`
    pyenv install

    # Install dependencies specified in `pyproject.toml`
    poetry install

If `pyenv install` gives an error about `_tkinter`, you can ignore it.
If you see other errors, you may have to investigate.

If you have trouble with Poetry not picking up pyenv's python installation,
try `poetry env remove --all` and then `poetry install` again.

Typecheck and run tests:

    ./check.sh

    # or individually:
    poetry run mypy .
    poetry run pytest -vv

Run the compiler on a source code file:

    ./compiler.sh COMMAND path/to/source/code

where `COMMAND` may be one of these:

    interpret
    TODO(student): add more

## IDE setup

Recommended VSCode extensions:

- Python
- Pylance
- autopep8
