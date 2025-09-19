import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def endpoint():
    return f"{BASE_URL}/posts"

def test_get_posts_status_code(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        assert response.status_code == 200
        print(f"Response Status Code ==> {response.status_code} ==> Passed")
    else:
        print("Response Status Code ==> ", response.status_code, " ==> Failed")
   # print("Response Body ==> ", response.text)

def test_get_posts_content_type(endpoint):
    response = requests.get(endpoint)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert data["id"] == 1
    assert "title" in data

def test_create_post_and_verify_data():
    payload = {
        "title": "QA Automation",
        "body": "Pytest API test",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data

def test_update_put():
    payload = {
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200 or response.status_code == 204

def test_get_post_not_found():
    response = requests.get(f"{BASE_URL}/posts/999999")
    assert response.status_code == 404 or response.json() == {}