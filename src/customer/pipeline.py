import logging
from customer.logging_config import configure_logging
from customer.csv_reader import read_customers_csv
from customer.processor import process_customers
from customer.parser import parse_customer
from customer.config import CUSTOMER_DATA_FILE

#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_customer_pipeline(path=CUSTOMER_DATA_FILE):
    logger.info("Customer pipeline started")

    customers = read_customers_csv(path)
    logger.info("Loaded %s customers",len(customers))

    parsed_customers =[]
    for customer in customers:
        parsed_customers.append(parse_customer(customer))
    result = process_customers(parsed_customers)
    logger.info("Customer pipeline completed")
    return result