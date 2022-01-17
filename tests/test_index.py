def test_index(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """

    response = client.get('/')
    assert response.status_code == 200
    assert b'Climate Action' in response.data
    assert b'About us' in response.data
    #TODO add more statements
