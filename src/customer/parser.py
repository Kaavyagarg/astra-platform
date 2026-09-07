def convert_age(age):
    try:
        return int(age)
    except ValueError:
        return None

def parse_customer(customer):
    parsed_customer = customer.copy()
    age = convert_age(customer.get("age"))
    if age is not None:
        parsed_customer['age'] = age
    return parsed_customer