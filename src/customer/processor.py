from validator.validator import validate_age
from customer.cleaner import clean_customer
def process_customer(customer):
    if validate_age(customer.get("age")):
        valid, reason = validate_age(customer.get("age"))
        if valid :
            return clean_customer(customer)
        return {
            "customer":customer,
            "reason":reason
        }

def process_customers(customers):
    processed = []
    rejected = []
    for customer in customers:
        result =process_customer(customer)
        if "reason" in result:
            rejected.append(result)
        else:
            processed.append(result)
    return {
        "processed" :processed,
        "rejected" : rejected
    }