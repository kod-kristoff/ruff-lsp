"""Utility functions for use with tests."""
from __future__ import annotations

import pathlib
import platform
from typing import TypeVar


def normalizecase(path: str) -> str:
    """Fixes 'file' uri or path case for easier testing in windows."""
    return path.lower() if platform.system() == "Windows" else path


def as_uri(path: str) -> str:
    """Return 'file' uri as string."""
    return normalizecase(pathlib.Path(path).as_uri())


T = TypeVar("T")


def unwrap(option: T | None) -> T:
    if option is None:
        raise ValueError("Option is None")
    return option
