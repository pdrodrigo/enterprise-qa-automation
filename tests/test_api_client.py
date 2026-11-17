
import requests

from core.api_client import APIClient


def test_api_client_should_initialize(api_client):
    assert api_client.base_url == (
        "https://jsonplaceholder.typicode.com"
    )
    assert isinstance(api_client.session, requests.Session)


def test_api_client_should_configure_headers(api_client):
    assert api_client.session.headers["Accept"] == "application/json"
    assert api_client.session.headers["Content-Type"] == "application/json"


def test_api_client_should_execute_get_request(api_client):
    response = api_client.get("/posts/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_api_client_should_execute_post_request(api_client):
    payload = {
        "title": "QA Automation",
        "body": "API Testing Framework",
        "userId": 1,
    }

    response = api_client.post("/posts", json=payload)

    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]


def test_api_client_should_close_session():
    client = APIClient()

    client.close()

    assert client.session is not None
