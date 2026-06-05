import pytest
from jsonschema import validate

from tests.schemas import USER_SCHEMA


@pytest.mark.smoke
def test_get_all_users_returns_non_empty_list(api_client):
    response = api_client.get("/users")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0


@pytest.mark.contract
def test_get_single_user_schema(api_client):
    response = api_client.get("/users/1")
    assert response.status_code == 200
    user = response.json()
    validate(instance=user, schema=USER_SCHEMA)
    assert user["id"] == 1


def test_user_email_has_expected_format(api_client):
    response = api_client.get("/users/1")
    assert response.status_code == 200
    email = response.json()["email"]
    assert "@" in email
    assert "." in email.split("@")[1]
