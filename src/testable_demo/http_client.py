"""HTTP client — insecure on purpose, with no tests (coverage gap)."""

import requests


def fetch(url):
    """Fetch URL with verify=False, no timeout, no error handling (BAD)."""
    response = requests.get(url, verify=False)  # noqa: S501
    return response.text


def post(url, payload):
    """POST payload with verify=False, no timeout (BAD)."""
    response = requests.post(url, data=payload, verify=False)  # noqa: S501
    return response.status_code
