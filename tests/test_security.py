"""Tests for ``testable_demo.security``."""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from testable_demo.security import (
    generate_token,
    hash_password,
    parse_literal_config,
    run_command,
    safe_load_yaml,
    select_user_by_id,
    write_temp_file,
)


def test_hash_password_is_deterministic() -> None:
    digest_one = hash_password("hunter2", b"salt-123")
    digest_two = hash_password("hunter2", b"salt-123")
    assert digest_one == digest_two
    assert len(digest_one) == 64


def test_hash_password_changes_with_salt() -> None:
    first = hash_password("hunter2", b"salt-a")
    second = hash_password("hunter2", b"salt-b")
    assert first != second


def test_hash_password_empty_password_raises() -> None:
    with pytest.raises(ValueError, match="password"):
        hash_password("", b"salt")


def test_hash_password_empty_salt_raises() -> None:
    with pytest.raises(ValueError, match="salt"):
        hash_password("pw", b"")


def test_generate_token_default_length_is_url_safe() -> None:
    token = generate_token()
    assert isinstance(token, str)
    assert len(token) >= 32
    assert all(ch.isalnum() or ch in "-_" for ch in token)


def test_generate_token_invalid_size_raises() -> None:
    with pytest.raises(ValueError, match="positive"):
        generate_token(0)


def test_run_command_returns_stdout() -> None:
    output = run_command(["python3", "-c", "print('hello')"])
    assert output.strip() == "hello"


def test_run_command_empty_args_raises() -> None:
    with pytest.raises(ValueError, match="empty"):
        run_command([])


def test_parse_literal_config_dict() -> None:
    parsed = parse_literal_config("{'host': 'localhost', 'port': 8080}")
    assert parsed == {"host": "localhost", "port": 8080}


def test_parse_literal_config_list() -> None:
    assert parse_literal_config("[1, 2, 3]") == [1, 2, 3]


def test_parse_literal_config_empty_raises() -> None:
    with pytest.raises(ValueError, match="empty"):
        parse_literal_config("   ")


def test_safe_load_yaml_basic() -> None:
    parsed = safe_load_yaml("name: 'demo'\nport: 8080\n")
    assert parsed == {"name": "demo", "port": 8080}


def test_safe_load_yaml_skips_comments_and_blanks() -> None:
    parsed = safe_load_yaml("# comment\n\nfoo: 1\n")
    assert parsed == {"foo": 1}


def test_safe_load_yaml_string_fallback() -> None:
    parsed = safe_load_yaml("greeting: hello world\n")
    assert parsed == {"greeting": "hello world"}


def test_safe_load_yaml_invalid_line_raises() -> None:
    with pytest.raises(ValueError, match="invalid line"):
        safe_load_yaml("not-a-key-value\n")


def test_select_user_by_id_returns_row(tmp_path: Path) -> None:
    db_path = tmp_path / "users.db"
    with sqlite3.connect(db_path) as conn:
        conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        conn.execute("INSERT INTO users (id, name) VALUES (1, 'alice')")
        conn.commit()
    result = select_user_by_id(str(db_path), 1)
    assert result == (1, "alice")


def test_select_user_by_id_missing_returns_none(tmp_path: Path) -> None:
    db_path = tmp_path / "users.db"
    with sqlite3.connect(db_path) as conn:
        conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        conn.commit()
    result = select_user_by_id(str(db_path), 42)
    assert result is None


def test_select_user_by_id_negative_raises(tmp_path: Path) -> None:
    db_path = tmp_path / "users.db"
    with sqlite3.connect(db_path) as conn:
        conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        conn.commit()
    with pytest.raises(ValueError, match="non-negative"):
        select_user_by_id(str(db_path), -1)


def test_write_temp_file_creates_readable_file() -> None:
    path = write_temp_file("contents", suffix=".txt")
    try:
        assert path.exists()
        assert path.suffix == ".txt"
        assert path.read_text(encoding="utf-8") == "contents"
    finally:
        path.unlink()
