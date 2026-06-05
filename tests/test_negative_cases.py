import pytest


@pytest.mark.smoke
def test_non_existing_post_returns_404(api_client):
    response = api_client.get("/posts/999999")
    assert response.status_code == 404


def test_invalid_route_returns_404(api_client):
    response = api_client.get("/invalid-route")
    assert response.status_code == 404

