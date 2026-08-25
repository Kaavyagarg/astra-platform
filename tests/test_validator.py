import pytest
from validator.validator import is_valid_email, validate_emails
from validator.validator import validate_age
def test_valid_email():
    assert is_valid_email('abc@gmail.com') is True
    """ To run the same test multiple times with different data."""
@pytest.mark.parametrize(
       "email",
        ['abc.com',
         'abc@gmail',
        '@gmail.com',
        'abc@.com'],
)
def test_invalid_emails(email):
    assert is_valid_email(email) is False
def test_empty_email():
    assert is_valid_email("") is False
def test_email_with_only_spaces():
    assert is_valid_email("   ") is False
def test_validate_emails():
    emails = [
        'abc@gmail.com',
        'abc@gmail',
        'hello@yahoo.com'
    ]
    assert validate_emails(emails)==[True,False,True]

def test_email_with_integer_input():
    assert is_valid_email(12345) is False
def test_email_with_none_input():
    assert is_valid_email(None) is False

def test_validate_age():
    assert validate_age(29) == (True,None)
    assert validate_age(None) == (False, "Age not mentioned")
    assert validate_age("29") == (False, "Incorrect data type")
    assert validate_age(-5) == (False, "Invalid age")