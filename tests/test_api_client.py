from customer.api_client import get_url_status,get_url_data
def test_get_url_status(monkeypatch):
    class FakeResponse:
        status_code = 200

    def fake_get(url):
        return FakeResponse()
    monkeypatch.setattr("customer.api_client.requests.get",fake_get)
    result = get_url_status("https://example.com")
    assert result == 200

def test_get_url_data(monkeypatch):
    class FakeResponse:
        def json(self):
            return {
                "name" : "Alice",
                "age" : 25
            }
    def fake_get(url):
        return FakeResponse() #Creating an object from FakeResponse class
    
# For this test, don't use real requests.get. use fake_get instead
    monkeypatch.setattr(
        "customer.api_client.requests.get",
        fake_get
    )
    result = get_url_data('https://example.com')
    assert result['name'] == 'Alice'
    assert result['age'] == 25
    
#get_url_data()->requests.get(url) -> (monkeypatch redirects this) -> fake_get(url)
#                                                                             |       
#Python dictionary <- {"name": "Alice", "age": 25} <- response.json()<- FakeResponse()
     

