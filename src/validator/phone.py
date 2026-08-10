def is_valid_phone(phone: str) -> bool:
    """Check whether a phone number is valid"""
    if phone.isdigit():
        return len(phone) == 10
    elif phone.startswith("+91") and phone[3:].isdigit():
        return len(phone[3:]) == 10
    else:
        return False