import os
from collections.abc import Generator

import pytest
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from src.api_client import APIClient


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")


@pytest.fixture(scope="session")
def api_session() -> Generator[requests.Session, None, None]:
    session = requests.Session()
    retry = Retry(
        total=3,
        read=3,
        connect=3,
        backoff_factor=0.3,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET",),
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.headers.update({"Accept": "application/json"})
    yield session
    session.close()


@pytest.fixture()
def api_client(base_url: str, api_session: requests.Session) -> APIClient:
    return APIClient(base_url=base_url, session=api_session, timeout=10)

