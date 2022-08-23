# `pyprote`: A Python package for creating Templates for python projects

# Installation - development

Create a virtual environment.

## `Poetry`:
```shell
poetry install
```

# Testing

Running the tests requires to run the following command in the root folder (of course in the virtual environment):

```shell
poetry run pytest
```


# CLI app

```shell
pyprote --help
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

```
bumpver update --dry --patch
```
`--dry` just shows how the version WOULD change.
```
bumpver update --patch
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

## Installation from PyPi

```shell
pip install pyprote
```
