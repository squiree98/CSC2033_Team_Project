def test_quizzes(client):
    response = client.get('/quizzes', follow_redirects=True)
    assert response.status_code == 200
    #assert b'Filter ' in response.data


def test_create_quiz(client):
    response = client.post('/create_quiz',
                          data=dict(name='Climate Action', age_group="5-12"), follow_redirects=True)
    assert response.status_code == 200
    assert b"bbba" in response.data


def test_create_question(client):
    response = client.get('/create_question', follow_redirects=True)
    assert response.status_code == 200
    assert b'Please enter' in response.data