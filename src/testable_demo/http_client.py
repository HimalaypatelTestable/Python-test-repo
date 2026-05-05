"""Safe HTTP client wrappers around ``requests``.

Calls always set an explicit timeout and use TLS verification (the default
``verify=True``). Errors are surfaced via ``raise_for_status``.
"""

from __future__ import annotations

from typing import Any

import requests


def fetch_json(url: str, timeout: float = 10.0) -> Any:
    """GET ``url`` and decode the JSON response body.

    ``timeout`` is forwarded to ``requests.get``. Raises
    ``requests.HTTPError`` for non-2xx responses.
    """
    if not url:
        raise ValueError("url must not be empty")
    if timeout <= 0:
        raise ValueError("timeout must be positive")
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()


def fetch_text(url: str, timeout: float = 10.0) -> str:
    """GET ``url`` and return the response body as text."""
    if not url:
        raise ValueError("url must not be empty")
    if timeout <= 0:
        raise ValueError("timeout must be positive")
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.text
