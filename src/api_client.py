from __future__ import annotations

from typing import Any

import requests


class APIClient:
    """Simple wrapper over requests.Session for readable test calls."""

    def __init__(self, base_url: str, session: requests.Session, timeout: int = 10) -> None:
        self.base_url = base_url.rstrip("/")
        self.session = session
        self.timeout = timeout

    def get(self, endpoint: str, **kwargs: Any) -> requests.Response:
        endpoint = endpoint.lstrip("/")
        return self.session.get(
            f"{self.base_url}/{endpoint}",
            timeout=kwargs.pop("timeout", self.timeout),
            **kwargs,
        )
