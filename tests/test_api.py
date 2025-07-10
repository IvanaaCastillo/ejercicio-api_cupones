from app.api_cupones import app

def test_success():
    client = app.test_client()
    res = client.post('/price', json={'price': 990, 'coupon': 'SALES10'})
    assert res.status_code == 200

#def test_failure():
    #client = app.test_client()
    #res = client.post('/price', json={'price': 990, 'coupon': 'SALES10'})
    #assert res.status_code == 500
