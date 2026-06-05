import pytest
from jsonschema import validate

from tests.schemas import POST_SCHEMA


@pytest.mark.smoke
def test_get_all_posts_returns_200_and_list(api_client):
    response = api_client.get("/posts")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0


@pytest.mark.contract
def test_get_single_post_contract_and_content(api_client):
    response = api_client.get("/posts/1")
    assert response.status_code == 200
    data = response.json()
    validate(instance=data, schema=POST_SCHEMA)
    assert data["id"] == 1
    assert data["userId"] >= 1
    assert data["title"].strip() != ""
    assert data["body"].strip() != ""


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_filter_posts_by_user(api_client, user_id):
    response = api_client.get("/posts", params={"userId": user_id})
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0
    assert all(item["userId"] == user_id for item in posts)
