"""Pytest configuration."""

from pathlib import Path

import pytest

pytest_plugins = "sphinx.testing.fixtures"


@pytest.fixture(scope="session")
def rootdir():
    """Get the root directory for the whole test session."""
    return Path(__file__).parent.absolute() / "roots"
