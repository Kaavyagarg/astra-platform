import logging
logger = logging.getLogger(__name__)
def is_positive(num: int) -> bool:
    "check whether a number is positive or negative"
    return num > 0

import re
def is_valid_email (email:str)-> bool:
    """
    Check whether email follows basic validation rules
    """
    if not isinstance(email,str):
        logger.warning("Invalid email type received")
        return False
    #pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    #return bool(re.match(pattern, email))
    email = email.strip().lower()
    if not email:
        return False
    if "@" not in email:
        return False
    if "." not in email:
        return False
    if email.startswith("@") or "@." in email:
        return False
    return True

def validate_emails(emails:list[str])-> list[bool]:
    """Validate a list of email addresses"""
    return [is_valid_email(email) for email in emails]
