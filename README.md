# Astra Data Platform

Astra is a Python-based data platform project built to develop practical data engineering skills through a working application.

## Current capabilities

- CSV and JSON customer data ingestion
- Customer parsing and validation
- Data processing and rejection of invalid records
- Logging and error handling
- API data ingestion
- SQLite database integration
- Customer insertion, retrieval, updates and deletion
- Batch database operations
- Unit and integration testing

## Technology stack

- Python
- SQLite
- Pytest
- uv
- Git

## Project structure

```text
astra-platform/
├── data/
│   ├── customers.csv
│   ├── customers.json
│   └── customers.txt
├── src/
│   ├── customer/
│   └── validator/
├── tests/
├── main.py
├── pyproject.toml
└── README.md
```

## Setup

Install project dependencies:

```bash
uv sync
```

## Run Astra

From the project root:

```bash
uv run --no-sync python main.py
```

The current application entry point runs the customer database pipeline:

1. Reads customer records from the configured CSV file.
2. Parses and processes customer records.
3. Rejects invalid records.
4. Saves successfully processed customers to SQLite.
5. Reports the number of processed and rejected records.

The default input file is:

```text
data/customers.csv
```

The input file can be changed using the `CUSTOMER_DATA_FILE` environment variable.

The SQLite database is created at:

```text
data/astra.db
```

## Database behavior

Astra currently uses the following customer table:

| Column | Type |
|---|---|
| id | INTEGER PRIMARY KEY |
| name | TEXT |
| city | TEXT |
| age | INTEGER |

Each successful `save_customer()` operation commits independently.

**Important:** The current CSV-to-database pipeline is append-only. Running it repeatedly inserts the same valid input records again. Duplicate prevention and upsert behavior have not yet been implemented.

Batch database saving uses a separate all-or-nothing transaction.

## Run tests

Run the complete test suite:

```bash
uv run --no-sync pytest -q
```

## Development progress

### Completed

- Python fundamentals and project setup
- Input validation and parsing
- CSV and JSON ingestion
- Data processing and quality checks
- Logging and configuration
- API integration
- SQLite database creation and operations
- Pipeline integration
- Unit and integration tests
- Runnable application entry point

### Future development

- Advanced SQL and data modeling
- Apache Spark
- Streaming and Kafka
- Workflow orchestration with Airflow
- FastAPI
- Cloud infrastructure and AWS
- Observability and reliability engineering
- AI data platform capabilities

Future capabilities will be introduced in subsequent project versions.