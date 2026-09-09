import logging
from validator.validator import validate_age
from customer.cleaner import clean_customer
logger = logging.getLogger(__name__)
def process_customer(customer):
    if validate_age(customer.get("age")):
        valid, reason = validate_age(customer.get("age"))
        if valid :
            logger.info(
                "Customer processed: %s",
                customer.get("name")
            )
            return clean_customer(customer)
        logger.warning("Customer rejected: %s - %s",
                                    customer.get("name"),
                                    reason)
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