"""Tests for the pyprote module."""
import subprocess  # noqa: S404 # acknowledge security warning
from pathlib import Path
from typing import List

from pyprote.cli_argument_defaults import format_dict_defaults, out_dir_default


def test_pyprote_cli(cleanup_dir):
    """Test the pyprote cli."""
    # arrange
    expected_file_creations = get_expected_file_creations()

    # act
    res = subprocess.run(["pyprote"], capture_output=True)  # noqa: S603,S607 - ignore security warning

    # assert
    res_std_out_decoded = res.stdout.decode("utf-8")
    for path in expected_file_creations:
        # assert logging messages about file creation
        assert path in res_std_out_decoded

        # assert file where actually created
        filepath = path.replace(" created.", "")
        assert Path(filepath).exists()


def get_expected_file_creations() -> List[str]:
    """Get the expected file creation messages."""
    package_name = format_dict_defaults["package_name"]
    package_files = {
        "root_dir_files": ["pyproject.toml", "README.md", "setup.cfg", "pytest.ini", ".gitignore", "Pipfile"],
        "test_dir_files": ["__init__.py", "conftest.py", f"test_{package_name}.py"],
        "package_dir_files": ["__main__.py", "__init__.py", f"{package_name}.py"],
        "logging_config_dir_files": ["logger_config.json", "logger_config.py"],
    }

    expected_file_creations = []
    expected_file_creations += fill_expected_file_creations(package_files["root_dir_files"], "root")
    expected_file_creations += fill_expected_file_creations(package_files["package_dir_files"], "package")
    expected_file_creations += fill_expected_file_creations(package_files["test_dir_files"], "tests")
    expected_file_creations += fill_expected_file_creations(package_files["logging_config_dir_files"], "logging_config")
    return expected_file_creations


def fill_expected_file_creations(
    dir_files: List[str],
    dir_name: str,
) -> List[str]:
    """Fill the expected file creation messages.

    Args:
        dir_files (List[str]): List of files that are expected to be created.
        dir_name (str): Name of the directory. Currently, supports ["root", "package", "tests", "logging_config"]


    Returns:
        List[str]: List of expected file creation messages.
    """
    res = []
    dir_path = get_dir_path(dir_name)
    for file_name in dir_files:
        res.append(paste_created(dir_path, file_name))
    return res


def get_dir_path(dir_name: str) -> Path:
    """Get the path to the directory where the files are expected to be created.

    Args:
        dir_name (str): Name of the directory. Currently, supports ["root", "package", "tests", "logging_config"]

    Returns:
        Path: Path to the directory.

    Raises:
        ValueError: If the directory name is not one of the expected ones.
    """
    base_dir = Path(out_dir_default)
    package_name = format_dict_defaults["package_name"]
    if dir_name == "root":
        return base_dir
    elif dir_name == "package":
        return base_dir / package_name
    elif dir_name == "tests":
        return base_dir / "tests"
    elif dir_name == "logging_config":
        return base_dir / package_name / "logging_config"
    raise ValueError(f"Invalid dir_name: {dir_name}")


def paste_created(dirpath: Path, filename: str) -> str:
    """Paste the created file name into the expected file creation message."""
    root_file_path = str(dirpath / filename)
    return f"{root_file_path} created."
