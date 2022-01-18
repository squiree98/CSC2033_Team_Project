"""

This file (test_app.py) contains the unit tests for the app.py file.
"""


def test_index(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid

    author Kiara
    date 17/01/2022
    """

    response = client.get('/')
    assert response.status_code == 200
    assert b'Climate Action' in response.data
    assert b'What is Climate Change?' in response.data
    assert b'What are the causes?' in response.data
    assert b'What are the effects?' in response.data
    assert b'What are the causes?' in response.data
    assert b'Where can I learn more?' in response.data
    assert b'About us' in response.data


def test_page_not_found(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/test' page is requested (GET)
    THEN check that the response is 404

    author Kiara
    date 18/01/2022
    """

    response = client.get('/test')
    assert response.status_code == 404
    assert b'Ooops! Page not found... Maybe look elsewhere?' in response.data

