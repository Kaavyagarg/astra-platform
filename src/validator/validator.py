def is_positive(num: int) -> bool:
    "check whether a number is positive or negative"
    return num > 0

import re
def is_valid_email (email:str)-> bool:
    "Check whether email is valid"
    #pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    #return bool(re.match(pattern, email))
    email = email.strip().lower()
    if not email:
        return False
    if "@" not in email:
        return False
    if "." not in email:
        return False
    if email.startswith("@"):
        return False
    if "@." in email:
        return False
    return True