from customer.api_client import get_url_status,get_url_data
import pytest
import requests
def test_get_url_status(monkeypatch):
    class FakeResponse:
        status_code = 200

    def fake_get(url,timeout=5):
        return FakeResponse()
    monkeypatch.setattr("customer.api_client.requests.get",fake_get)
    result = get_url_status("https://example.com")
    assert result == 200

def test_get_url_data(monkeypatch):
    class FakeResponse:
        def raise_for_status(self):
            pass 
        def json(self):
            return {
                "name" : "Alice",
                "age" : 25
            }
    def fake_get(url, timeout=5):
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
     
def test_get_url_data_http_error(monkeypatch):
    class FakeResponse:
        def raise_for_status(self):
            raise requests.HTTPError("404 Client Error")
        def json(self):
            return {}
    def fake_get(url,timeout= 5):
        return FakeResponse()
    monkeypatch.setattr(
        "customer.api_client.requests.get",
        fake_get
    )
# Expect this code to raise an HTTPError. If it doesn't, the test fails.
    with pytest.raises(requests.HTTPError):
        get_url_data("https://example.com")

def test_get_url_data_network_error(monkeypatch):
    def fake_get(url, timeout=5):
        raise requests.RequestException("Connection failed")
    monkeypatch.setattr(
        "customer.api_client.requests.get",
        fake_get
    )
    with pytest.raises(requests.RequestException):
        get_url_data("https://example.com")

def test_get_url_data_uses_timeout(monkeypatch):
    class FakeResponse:
        def raise_for_status(self):
            pass
        def json(self):
            return {"name":"Alice"}
    def fake_get(url,timeout):
        assert timeout == 5
        return FakeResponse()
    monkeypatch.setattr(
        "customer.api_client.requests.get",
        fake_get
    )
    result = get_url_data("https://example.com")
    assert result['name'] == 'Alice'
def test_get_url_timeout(monkeypatch):
    def fake_get(url, timeout):
        raise requests.Timeout("Request timed out")
    monkeypatch.setattr(
        "customer.api_client.requests.get",
        fake_get
    )
    with pytest.raises(requests.Timeout):
        get_url_data("https://example.com")