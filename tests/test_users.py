"""
This file (test_users.py) contains unit tests for the 'users' blueprint.

These tests use GETs and POSTS to different URLs to check for the proper behaviour of the 'users' blueprint
"""


def test_register_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check the response is 200

    author Kiara
    date 18/01/2022
    """
    response = client.get('/register')
    assert response.status_code == 200
    assert b'Sign up' in response.data
    assert b'Email' in response.data
    assert b'Password' in response.data
    assert b'Repeat Password' in response.data


def test_valid_registration(client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted (POST)
    THEN check the response is valid and the registered user is directed to log in page

    author Kiara
    date 18/01/2022
    """

    response = client.post('/register',
                                data=dict(email='test@email.com',
                                          password='password123',
                                          confirm_password='password123',
                                          q1="TRUE", q2="FALSE", q3="TRUE", q4="FALSE", q5="TRUE"),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Log in' in response.data
    assert b'Email' in response.data
    assert b'Password' in response.data
    assert b'Repeat Password' not in response.data


def test_invalid_registration_passwords_do_not_match(client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to with invalid credentials (POST)
    THEN check that user is redirected to register page

    author Kiara
    date 18/01/2022
    """
    response = client.post('/register',
                           data=dict(email='test@email.com',
                                     password='password123',
                                     confirm_password='passwood123',
                                     q1="TRUE", q2="FALSE", q3="TRUE", q4="FALSE", q5="TRUE"),
                           follow_redirects=True)
    assert response.status_code == 200
    assert b'Sign up' in response.data
    assert b'Email' in response.data
    assert b'Password' in response.data
    assert b'Repeat Password' in response.data


def test_invalid_registration_questions_answered_incorrectly(client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to with invalid credentials (POST)
    THEN check that user is redirected to register page

    author Kiara
    date 18/01/2022
    """
    response = client.post('/register',
                           data=dict(email='test@email.com',
                                     password='password123',
                                     confirm_password='password123',
                                     q1="TRUE", q2="TRUE", q3="TRUE", q4="FALSE", q5="TRUE"),
                           follow_redirects=True)
    assert response.status_code == 200
    assert b'Sign up' in response.data
    assert b'Email' in response.data
    assert b'Password' in response.data
    assert b'Repeat Password' in response.data


def test_login_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is requested (GET)
    THEN check the response is 200

    author Kiara
    date 18/01/2022
    """

    response = client.get('/login')
    assert response.status_code == 200
    assert b'Log in' in response.data
    assert b'Email' in response.data
    assert b'Password' in response.data


def test_valid_login(client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted (POST)
    THEN check the response is valid and logged-in user is directed to profile page

    author Kiara
    date 18/01/2022
    """

    response = client.post('/login', data=dict(email='User@email.com', password='password123'), follow_redirects=True)
    assert response.status_code == 200
    assert b'Sign up' not in response.data
    assert b'Log in' not in response.data
    assert b'Password' not in response.data
    assert b'My Profile' in response.data
    assert b'Email Address: User@email.com' in response.data
    assert b'Username: User' in response.data
    assert b'Total Quiz Score: 0' in response.data


def test_invalid_login(client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user

    author Kiara
    data 18/01/2022
    """
    response = client.post('/login',
                                data=dict(email='User@email.com@gmail.com', password='passwood123'),
                                follow_redirects=True)

    assert response.status_code == 200
    assert b'Log in' in response.data
    assert b'Log out' not in response.data


def test_profile_page(client, init_database, login_default_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/profile' page is requested (GET)
    THEN check the response is 200

    author Kiara
    date 18/01/2022
    """

    response = client.get('/profile')
    assert response.status_code == 200
    assert b'My Profile' in response.data
    assert b'Email Address: User@email.com' in response.data
    assert b'Username: User' in response.data
    assert b'Total Quiz Score: 0' in response.data
