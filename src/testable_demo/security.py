"""Secure-by-default examples for hashing, subprocess, parsing, and SQL.

This module deliberately uses only safe APIs so that bandit and semgrep
do not flag any patterns. It is the showcase module for SAST aggregates.
"""

from __future__ import annotations

import ast
import hashlib
import secrets
import sqlite3
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Iterable


def hash_password(password: str, salt: bytes) -> str:
    """Hash ``password`` with a per-user ``salt`` using SHA-256.

    Returns the hex digest. Use a unique random ``salt`` per user.
    """
    if not password:
        raise ValueError("password must not be empty")
    if not salt:
        raise ValueError("salt must not be empty")
    digest = hashlib.sha256(salt + password.encode("utf-8")).hexdigest()
    return digest


def generate_token(num_bytes: int = 32) -> str:
    """Generate a cryptographically strong URL-safe token."""
    if num_bytes <= 0:
        raise ValueError("num_bytes must be positive")
    return secrets.token_urlsafe(num_bytes)


def run_command(args: Iterable[str], timeout: float = 10.0) -> str:
    """Run a subprocess safely with a list of arguments and ``shell=False``.

    Returns the captured stdout. Raises ``subprocess.CalledProcessError``
    when the command exits non-zero.
    """
    arg_list = list(args)
    if not arg_list:
        raise ValueError("args must not be empty")
    completed = subprocess.run(  # noqa: S603 - shell=False with explicit args
        arg_list,
        shell=False,
        check=True,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return completed.stdout


def parse_literal_config(source: str) -> Any:
    """Parse a Python literal expression safely (no ``eval``)."""
    if not source.strip():
        raise ValueError("source must not be empty")
    return ast.literal_eval(source)


def safe_load_yaml(source: str) -> Any:
    """Parse a tiny YAML-like ``key: value`` document without external deps.

    This intentionally avoids ``yaml.load``; values are parsed with
    ``ast.literal_eval`` when possible, otherwise treated as strings.
    """
    result: dict[str, Any] = {}
    for raw_line in source.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        key, separator, value = line.partition(":")
        if not separator:
            raise ValueError(f"invalid line: {raw_line!r}")
        result[key.strip()] = _coerce_value(value.strip())
    return result


def _coerce_value(value: str) -> Any:
    """Coerce a YAML-like scalar to a Python value."""
    if not value:
        return ""
    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return value


def select_user_by_id(database_path: str, user_id: int) -> tuple[int, str] | None:
    """Look up a user by id using a parameterized SQL query."""
    if user_id < 0:
        raise ValueError("user_id must be non-negative")
    with sqlite3.connect(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, name FROM users WHERE id = ?",
            (user_id,),
        )
        row = cursor.fetchone()
    if row is None:
        return None
    return int(row[0]), str(row[1])


def write_temp_file(content: str, suffix: str = ".txt") -> Path:
    """Write ``content`` to a securely created temporary file.

    Uses ``NamedTemporaryFile`` rather than ``tempfile.mktemp``.
    Returns the path of the created file.
    """
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=suffix,
        delete=False,
        encoding="utf-8",
    ) as handle:
        handle.write(content)
        return Path(handle.name)
