
import allure

from clients.posts_client import PostsClient


@allure.epic("Enterprise QA Automation")
@allure.feature("Posts API")
@allure.story("Retrieve all posts")
@allure.severity(allure.severity_level.CRITICAL)
def test_should_get_all_posts(posts_client: PostsClient):
    with allure.step("Send GET request to retrieve all posts"):
        response = posts_client.get_all_posts()

    with allure.step("Validate HTTP response"):
        assert response.status_code == 200

    with allure.step("Validate response structure"):
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0


@allure.epic("Enterprise QA Automation")
@allure.feature("Posts API")
@allure.story("Retrieve post by ID")
@allure.severity(allure.severity_level.CRITICAL)
def test_should_get_post_by_id(posts_client: PostsClient):
    with allure.step("Send GET request for post ID 1"):
        response = posts_client.get_post(1)

    with allure.step("Validate HTTP response"):
        assert response.status_code == 200

    with allure.step("Validate returned post"):
        assert response.json()["id"] == 1


@allure.epic("Enterprise QA Automation")
@allure.feature("Posts API")
@allure.story("Create a post")
@allure.severity(allure.severity_level.NORMAL)
def test_should_create_post(posts_client: PostsClient):
    payload = {
        "title": "Enterprise QA Automation",
        "body": "Testing API with Python and Pytest",
        "userId": 1,
    }

    with allure.step("Send POST request to create a post"):
        response = posts_client.create_post(payload)

    with allure.step("Validate HTTP response"):
        assert response.status_code == 201

    with allure.step("Validate created post data"):
        assert response.json()["title"] == payload["title"]
        assert response.json()["userId"] == 1


@allure.epic("Enterprise QA Automation")
@allure.feature("Posts API")
@allure.story("Update a post")
@allure.severity(allure.severity_level.NORMAL)
def test_should_update_post(posts_client: PostsClient):
    payload = {
        "id": 1,
        "title": "Updated QA Automation",
        "body": "Updated test content",
        "userId": 1,
    }

    with allure.step("Send PUT request to update post ID 1"):
        response = posts_client.update_post(1, payload)

    with allure.step("Validate HTTP response"):
        assert response.status_code == 200

    with allure.step("Validate updated post data"):
        assert response.json()["title"] == payload["title"]


@allure.epic("Enterprise QA Automation")
@allure.feature("Posts API")
@allure.story("Delete a post")
@allure.severity(allure.severity_level.NORMAL)
def test_should_delete_post(posts_client: PostsClient):
    with allure.step("Send DELETE request for post ID 1"):
        response = posts_client.delete_post(1)

    with allure.step("Validate HTTP response"):
        assert response.status_code == 200
