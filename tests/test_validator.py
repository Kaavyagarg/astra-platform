from src.validator.validator import is_valid_email
def test_valid_email():
    assert is_valid_email('abc@gmail.com') is True
def test_invalid_email_without_at():
    assert is_valid_email("abc.com") is False
def test_invalid_email_without_dot():
    assert is_valid_email("abc@gmail") is False
def test_invalid_email_starting_with_at():
    assert is_valid_email("@gmail.com") is False
def test_invalid_email_with_at_dot():
    assert is_valid_email("abc@.com") is False
def test_empty_email():
    assert is_valid_email("") is False
def test_email_with_only_spaces():
    assert is_valid_email("   ") is False