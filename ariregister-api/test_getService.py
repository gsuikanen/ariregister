from app_main import app

def test_home_page():
    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"OK" in response.data

def test_lists_ok():
    with app.test_client() as test_client:
        response = test_client.get('/api/v1/list/ownerRole')
        assert response.status_code == 200
        assert len(response.json) > 0
        response = test_client.get('/api/v1/list/ownerType')
        assert response.status_code == 200
        assert len(response.json) > 0

def test_lists_error():
    with app.test_client() as test_client:
        #Missing list name
        response = test_client.get('/api/v1/list/')
        assert response.status_code == 404
        #Non existing list name
        response = test_client.get('/api/v1/list/FakeList')
        assert response.status_code == 200
        assert b"ERROR" in response.data

def test_company_error():
    with app.test_client() as test_client:
        #No id provided
        response = test_client.get('/api/v1/company')
        assert response.status_code == 200
        assert b"ERROR" in response.data
        #Fake id provided
        response = test_client.get('/api/v1/company?id=-999')
        assert response.status_code == 200
        assert b"ERROR" in response.data
        assert b"not found" in response.data

def test_company_search_error():
    with app.test_client() as test_client:
        #No searchstring provided
        response = test_client.get('/api/v1/searchCompany')
        assert response.status_code == 200
        assert b"ERROR" in response.data
        #Too short searchstring provided
        response = test_client.get('/api/v1/searchCompany?searchstring=abc')
        assert response.status_code == 200
        assert b"ERROR" in response.data
        assert b"at least 4 symbols" in response.data

