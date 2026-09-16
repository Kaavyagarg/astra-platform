from customer.parser import convert_age
from customer.parser import parse_customer, parse_api_customer

def test_convert_valid_age():
    assert convert_age("25") == 25
def test_convert_invalid_age():
    assert convert_age("hello") is None
def test_parse_customer_converts_age():
    customer = {
        "name":"Alice",
        "age":"25",
        "phone":"9876543210"
    }
    result = parse_customer(customer)
    assert result["age"] == 25

def test_convert_none_age():
    assert convert_age(None) is None 

def test_parse_customer_missing_age():
    customer = {
        "name":"David",
        "age" : "",
        "phone":"9876543210"
    }
    result = parse_customer(customer)
    assert result["age"] is None 

def test_parse_api_customer():
    data = {
        "name":"Alice",
        "age": 25,
        "phone": "9876543210"
    }
    result = parse_api_customer(data)
    assert result['name'] == 'Alice'
    assert result['age'] == 25
    assert result['phone'] == "9876543210"