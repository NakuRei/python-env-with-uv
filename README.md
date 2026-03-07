# Python Environment with UV

This project is a template for setting up a Python environment with UV.

## Overview

This template includes the following features:

- A sample Python module (`sample.py`) with a simple function.
- A `pyproject.toml` file configured for linting with Ruff.

The project includes following tools:

- [Ruff](https://github.com/astral-sh/ruff): A fast Python linter and formatter.
- [Mypy](https://github.com/python/mypy): A static type checker for Python.
- [pytest](https://docs.pytest.org/): A testing framework for Python.
- [pre-commit](https://pre-commit.com/): A tool for managing and maintaining multi-language pre-commit hooks.
- [VS Code](https://code.visualstudio.com/) settings: A configuration for Python development in Visual Studio Code.

## Prerequisites

This project requires [uv](https://docs.astral.sh/uv/) and [Git](https://git-scm.com/) to be installed on your system.

## Getting Started

1. Clone the repository:

   ```bash
    git clone git@github.com:NakuRei/python-env-with-uv.git
    cd python-env-with-uv
    ```

2. Install the dependencies using UV:
    ```bash
    uv sync --dev
    ```

3. Initialize the pre-commit hooks:
    ```bash
    uv run pre-commit install
    ```

## Usage

```bash
# Run the example script
uv run python examples/example.py

# Run the tests
uv run pytest

# Lint the code
uv run ruff check --fix .

# Format the code
uv run ruff format .

# Type check
uv run mypy .
```

## License

© 2026 Nakurei. All rights reserved.
