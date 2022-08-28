"""Code that should run for all tests."""
import shutil
from pathlib import Path
from typing import Generator

import pytest

from pyprote.cli_argument_defaults import out_dir_default


@pytest.fixture
def sample_fixture() -> str:
    """Sample fixture."""
    return "Hello World!"


@pytest.fixture(autouse=True)
def cleanup_dir() -> Generator:
    """Fixture to clean up the results of the cli run."""
    yield

    # Teardown :
    if Path.cwd().joinpath(out_dir_default).exists():
        shutil.rmtree(Path.cwd().joinpath(out_dir_default))
