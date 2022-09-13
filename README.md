# pyprote: A Python package for creating Templates for python projects


[![PyPI version](https://badge.fury.io/py/pyprote.svg)](https://badge.fury.io/py/pyprote)
[![PyPI - Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![tests](https://github.com/Cattes/pyprote/actions/workflows/ci-cd-pipeline.yml/badge.svg)](https://github.com/Cattes/pyprote/actions/workflows/ci-cd-pipeline.yml)

## Installation from PyPi

```shell
pip install pyprote
```

# Usage

You can create a project template by changing into the directory you want the template to be
created in. Existing files will **not** be overwritten.

## Create a new project

### Use default template:

You will have to replace all instances of `PY_PRO_TE_FILL_ME_IN` with your own project name, email etc..

```shell
pyprote
```


### Fill the template cli arguments:
```shell
pyprote --package_name my_cool_package_name \
        --package_version 0.1.0 \
        --package_description 'My cool package description' \
        --package_author_name 'John Doe' \
        --package_author_email john@doe \
        --package_link https://cool.package \
        --out_dir pyprote_output_dir
```

### CLI app

```shell
pyprote --help
```

# Installation - local development

Create a virtual environment.

## Poetry:
```shell
poetry install
```

# Testing

Running the tests requires to run the following command in the root folder (of course in the virtual environment):

```shell
poetry run pytest
```

# Formatting

```shell
poetry run black . && \
poetry run isort . && \
poetry run flake8 . && \
poetry run mypy .
```

## Versioning

Update (calendar) version with [bumpver](https://github.com/mbarkhau/bumpver):

```shell
poetry run bumpver update --dry --patch
```
`--dry` just shows how the version WOULD change.
```shell
poetry run bumpver update --patch
```


## How to build a Python package?

To build the package, you need to go to the root folder of the package and run the following command:

```shell
poetry build
```

The built package is now located in the dist/ folder.


## Publishing your package in PyPi

Publishing is done automatically using GitHub actions.

Commit to master creates test-pypi release.

Tagged Commit creates real pypi release.
