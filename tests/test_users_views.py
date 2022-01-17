def test_login(client):
    response = client.post('/login',
                                data=dict(username='user1@gmail.com', password='user1'),
                                follow_redirects=True)
    assert response.status_code == 200