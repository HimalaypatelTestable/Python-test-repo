"""Tests for ``testable_demo.http_client``."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
import requests

from testable_demo.http_client import fetch_json, fetch_text


def _make_response(
    status_code: int = 200,
    json_data: object | None = None,
    text_data: str = "",
) -> MagicMock:
    """Build a mock ``requests.Response`` for tests."""
    response = MagicMock(spec=requests.Response)
    response.status_code = status_code
    response.json = MagicMock(return_value=json_data)
    response.text = text_data
    if status_code >= 400:
        response.raise_for_status = MagicMock(
            side_effect=requests.HTTPError(f"{status_code} error"),
        )
    else:
        response.raise_for_status = MagicMock(return_value=None)
    return response


@patch("testable_demo.http_client.requests.get")
def test_fetch_json_returns_parsed_body(mock_get: MagicMock) -> None:
    mock_get.return_value = _make_response(json_data={"ok": True, "value": 42})
    result = fetch_json("https://example.com/api")
    assert result == {"ok": True, "value": 42}
    mock_get.assert_called_once_with("https://example.com/api", timeout=10.0)


@patch("testable_demo.http_client.requests.get")
def test_fetch_json_passes_timeout(mock_get: MagicMock) -> None:
    mock_get.return_value = _make_response(json_data=[])
    fetch_json("https://example.com/api", timeout=5)
    mock_get.assert_called_once_with("https://example.com/api", timeout=5)


@patch("testable_demo.http_client.requests.get")
def test_fetch_json_raises_on_http_error(mock_get: MagicMock) -> None:
    mock_get.return_value = _make_response(status_code=500)
    with pytest.raises(requests.HTTPError):
        fetch_json("https://example.com/api")


def test_fetch_json_empty_url_raises() -> None:
    with pytest.raises(ValueError, match="url"):
        fetch_json("")


def test_fetch_json_invalid_timeout_raises() -> None:
    with pytest.raises(ValueError, match="timeout"):
        fetch_json("https://example.com", timeout=0)


@patch("testable_demo.http_client.requests.get")
def test_fetch_text_returns_body(mock_get: MagicMock) -> None:
    mock_get.return_value = _make_response(text_data="hello")
    assert fetch_text("https://example.com") == "hello"


@patch("testable_demo.http_client.requests.get")
def test_fetch_text_raises_on_http_error(mock_get: MagicMock) -> None:
    mock_get.return_value = _make_response(status_code=404)
    with pytest.raises(requests.HTTPError):
        fetch_text("https://example.com/missing")


def test_fetch_text_empty_url_raises() -> None:
    with pytest.raises(ValueError, match="url"):
        fetch_text("")


def test_fetch_text_invalid_timeout_raises() -> None:
    with pytest.raises(ValueError, match="timeout"):
        fetch_text("https://example.com", timeout=-1)
