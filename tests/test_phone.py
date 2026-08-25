from validator.phone import is_valid_phone

def test_valid_phone_without_country_code():
    assert is_valid_phone("9876543210") is True


def test_valid_phone_with_country_code():
    assert is_valid_phone("+919876543210") is True


def test_valid_phone_with_space():
    assert is_valid_phone("91 9876543210") is False


def test_valid_phone_with_space_in_middle():
    assert is_valid_phone("98765 43210") is False


def test_valid_phone_with_letters():
    assert is_valid_phone("IN 9876543210") is False


def test_valid_phone_with_wrong_digit_count():
    assert is_valid_phone("987654321") is False 


def test_valid_phone_with_hypen():
    assert is_valid_phone("98765-43210") is False


def test_valid_phone_with_country_code_and_hypen():
    assert is_valid_phone("+91-9876543210") is False