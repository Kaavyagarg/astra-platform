import logging
from customer.logging_config import configure_logging
from customer.csv_reader import read_customers_csv
from customer.processor import process_customers
from customer.processor import process_customer
from customer.parser import parse_customer
from customer.config import CUSTOMER_DATA_FILE
from customer.api_client import get_url_data
from customer.parser import parse_api_customer
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

def run_api_customer_pipeline(url):
    data = get_url_data(url)
    customer = parse_api_customer(data)
    return process_customer(customer)

def run_api_customers_pipeline(url):
    data = get_url_data(url)
    customers = []
    for item in data:
        customers.append(parse_api_customer(item))
    return process_customers(customers)