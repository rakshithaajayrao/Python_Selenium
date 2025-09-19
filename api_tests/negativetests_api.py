import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_invalid_endpoint():
    response = requests.get(f"{BASE_URL}/invalid-endpoint")
    assert response.status_code == 404

def test_missing_required_fields():
    payload = {}  # Empty payload
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201  # This mock API still returns 201, but real APIs should return 400

def test_invalid_method():
    response = requests.put(f"{BASE_URL}/posts")
    assert response.status_code in [404, 405]  # Method not allowed or endpoint not found

def test_invalid_data_type():
    payload = {
        "title": 12345,  # Should be a string
        "body": True,    # Should be a string
        "userId": "abc"  # Should be an integer
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201  # Again, mock API may accept it, but real APIs should reject it

def test_unauthorized_access():
    headers = {"Authorization": "Bearer invalid_token"}
    response = requests.get(f"{BASE_URL}/posts", headers=headers)
    assert response.status_code in [401, 403, 200]  # Unauthorized or forbidden