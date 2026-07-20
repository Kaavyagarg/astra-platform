from src.validator.validator import is_positive,is_valid_email
print(is_positive(10))
print(is_positive(-5))
print(is_valid_email('john@email.com'))
print(is_valid_email('wrong-email'))
