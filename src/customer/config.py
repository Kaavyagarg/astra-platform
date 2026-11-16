import os

def get_customer_data_file():
    #Ask the environment for CUSTOMER_DATA_FILE. If nobody provided it, use data/customers.csv.
    return os.getenv(
    "CUSTOMER_DATA_FILE",
    'data/customers.csv'
)
CUSTOMER_DATA_FILE = get_customer_data_file()

APP_ENV = os.getenv(
    "APP_ENV",
    "development"
)

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)

def get_database_file():
    return os.getenv(
        "DATABSE_FILE",
        "data/astra.db"
    )
DATABASE_FILE = get_database_file()