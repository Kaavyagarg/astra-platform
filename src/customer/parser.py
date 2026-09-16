
def convert_age(age):
    try:
        return int(age)
    except (ValueError, TypeError):
        return None

def parse_customer(customer):
    parsed_customer = customer.copy()
    age = convert_age(customer.get("age"))
    if age == "":
        parsed_customer['age'] = None
    else:
        parsed_customer['age'] = convert_age(age)
    return parsed_customer

def parse_api_customer(data):
    return {
        "name": data.get("name"),
        "age": data.get("age"),
        "phone": data.get("phone")
    }