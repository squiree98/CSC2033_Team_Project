"""
This file (test_quiz.py) contains unit tests for the 'quiz' blueprint.

These tests use GETs to different URLs to check for the proper behaviour of the 'quiz' blueprint
"""


def test_quizzes_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/quizzes' page is requested (GET)
    THEN check the response is 200 (success)

    author Kiara
    date 18/01/2022
    """

    response = client.get('/quizzes', follow_redirects=True)
    assert response.status_code == 200


def test_create_quiz_page(client):
    """
       GIVEN a Flask application configured for testing
       WHEN the '/create_quiz' page is requested (GET)
       THEN check the response is 200 (success)

       author Kiara
       date 18/01/2022
       """

    response = client.get('/create_quiz', follow_redirects=True)
    assert response.status_code == 200


def test_create_question_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/create_question' page is requested (GET)
    THEN check the response is 200 (success)

    author Kiara
    date 18/01/2022
    """
    response = client.get('/create_question', follow_redirects=True)
    assert response.status_code == 200


def test_my_quizzes(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/my_quizzes' page is requested (GET)
    THEN check the response is 200 (success)

    author Kiara
    date 18/01/2022
    """
    response = client.get('/my_quizzes', follow_redirects=True)
    assert response.status_code == 200
