import logging

from customer.pipeline import run_customer_database_pipeline
from customer.config import CUSTOMER_DATA_FILE, DATABASE_FILE, LOG_LEVEL


def main():
    logging.basicConfig(
        level = getattr(logging,LOG_LEVEL.upper(), logging.INFO)
    )
    result = run_customer_database_pipeline(
        path=CUSTOMER_DATA_FILE,
        database_path=DATABASE_FILE
    )

    print("\nAstra pipeline completed")
    print(f"Processed: {len(result['processed'])}")
    print(f"Rejected: {len(result['rejected'])}")


if __name__ == "__main__":
    main()