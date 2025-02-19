import pytest
from application import app  # Import your Flask app

@pytest.fixture
def client():
    """Creates a test client for the Flask application."""
    app.testing = True
    return app.test_client()

def test_welcome_route(client):
    """Test the root URL (/)"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the flask course" in response.data
    
def test_index_route(client):
    """Test the /index route"""
    response = client.get("/index")
    assert response.status_code == 200
    assert b"Welcome to My Flask App!" in response.data  # Check content, not filename

def test_about_route(client):
    """Test the /about route"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"This is the about page" in response.data  # Check content, not filename

def test_form_get(client):
    """Test the /form route with GET"""
    response = client.get("/form")
    assert response.status_code == 200
    assert b"<form" in response.data  # Check if form is present


def test_form_post(client):
    """Test the /form route with POST"""
    form_data = {
        'name': 'Krish',
        'email': 'krish@example.com',
        'sex': 'male',
        'phone': '1234567890'
    }
    response = client.post("/form", data=form_data)
    assert response.status_code == 200
    assert b"Hello Krish!" in response.data  # Check if response contains "Hello Krish!"

def test_submit_post(client):
    """Test the /submit route with POST"""
    form_data = {
        'name': 'Krish',
        'email': 'krish@example.com',
        'sex': 'male',
        'phone': '1234567890'
    }
    response = client.post("/submit", data=form_data)
    assert response.status_code == 200
    assert b"Hello Krish!" in response.data  # Check if response contains "Hello Krish!"

def test_404_not_found(client):
    """Test an invalid route"""
    response = client.get("/invalid_route")
    assert response.status_code == 404
