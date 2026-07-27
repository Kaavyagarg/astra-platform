import pytest
from src.validator.validator import is_valid_email
def test_valid_email():
    assert is_valid_email('abc@gmail.com') is True
    """ To run the same test multiple times with different data."""
@pytest.mark.parametrize(
       "email",
        ['abc.com',
         'abc@gmail',
        '@gmail.com',
        'abc@.com']
)
def test_invalid_emails(email):
    assert is_valid_email(email) is False
def test_empty_email():
    assert is_valid_email("") is False
def test_email_with_only_spaces():
    assert is_valid_email("   ") is False