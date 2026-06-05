import pytest
from jsonschema import validate

from tests.schemas import POST_SCHEMA, USER_SCHEMA


@pytest.mark.parametrize(
    ("endpoint", "schema"),
    [
        ("/posts/1", POST_SCHEMA),
        ("/users/1", USER_SCHEMA),
    ],
)
@pytest.mark.contract
def test_core_endpoints_have_valid_contracts(api_client, endpoint, schema):
    response = api_client.get(endpoint)
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


@pytest.mark.parametrize("endpoint", ["/posts", "/users", "/comments", "/albums", "/todos"])
@pytest.mark.smoke
def test_common_resources_are_available(api_client, endpoint):
    response = api_client.get(endpoint)
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) > 0

