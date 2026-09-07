from customer.csv_reader import read_customers_csv
from customer.processor import process_customers
from customer.parser import parse_customer
def run_customer_pipeline(path):
    customers = read_customers_csv(path)
    parsed_customers =[]
    for customer in customers:
        parsed_customers.append(parse_customer(customer))
    result = process_customers(parsed_customers)
    return result