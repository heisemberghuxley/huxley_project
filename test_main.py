from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

<<<<<<< HEAD
def test_route_movie():
=======
def test_route_product():
>>>>>>> heisenberg
    response = client.get("/product")
    assert response.status_code ==200
    