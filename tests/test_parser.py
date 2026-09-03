from customer.parser import convert_age
def test_convert_valid_age():
    assert convert_age("25") == 25
def test_convert_invalid_age():
    assert convert_age("hello") is None