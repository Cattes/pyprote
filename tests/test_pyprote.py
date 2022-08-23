"""Tests for the pyprote module."""

import pytest

from pyprote.pyprote import funone


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (2, 4),
        (3, 9),
        (100, 10000),
        (1.2, 1.44),
        (-1, 1),
        (-2, 4),
        (-50, 2500),
    ],
)
def test_funone(test_input, expected):
    """Test the funone function."""
    assert funone(test_input) == expected
