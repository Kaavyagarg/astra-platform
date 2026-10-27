from customer.pipeline import run_customer_pipeline
import pytest
import logging
import customer.pipeline as pipeline_module
from customer.parser import convert_age
from customer.csv_reader import read_customers_csv
from customer.pipeline import run_api_customer_pipeline
from customer.pipeline import run_api_customers_pipeline, run_customer_database_pipeline
from customer.database import (create_connection, get_customers, create_customers_table)
def test_run_customer_pipeline():
    result = run_customer_pipeline("data/customers.csv")
    assert "processed" in result
    assert "rejected" in result

def test_run_customer_pipeline_separates_rejected_customers():
    result = run_customer_pipeline("data/customers.csv")
    print(result)
    assert len(result['processed']) == 2
    assert len(result['rejected']) == 1

def test_run_customer_pipeline_missing_file():
    with pytest.raises(FileNotFoundError):
        run_customer_pipeline("data/does_not_exist.csv")

def test_pipeline_rejects_negative_age(tmp_path):
    path = tmp_path/"customers.csv"
    path.write_text(
        "name,age,phone\n"
        "David,-5,9876543210\n"
    )
    result = run_customer_pipeline(path)
    assert len(result['processed']) == 0
    assert len(result['rejected']) == 1
    assert result['rejected'][0]['reason'] == 'Invalid age'

def test_pipeline_rejects_missing_age(tmp_path):
    path = tmp_path/'customers.csv'
    path.write_text(
        "name,age,phone\n"
        'David,,987654321\n'
    )
    print(read_customers_csv(path))
    result = run_customer_pipeline(path)
    assert len(result['processed']) == 0
    assert len(result['rejected']) == 1
    assert result['rejected'][0]['reason'] == 'Age not mentioned'

def test_run_api_customer_pipeline(monkeypatch):
    def fake_get_url_data(url):
        return {
            "name":"Alice",
            "age":25,
            "phone":"9876543210"
        }
    monkeypatch.setattr(
        "customer.pipeline.get_url_data",
        fake_get_url_data
    )
    result = run_api_customer_pipeline("https://example.com")
    assert result["name"] == "Alice"
    assert result["age"] == 25

def test_run_api_customer_pipeline_rejects_invalid_age(monkeypatch):
    def fake_get_url_data(url):
        return {
            "name": "Bob",
            "age": -5,
            "phone":"9876543210"
        }
    monkeypatch.setattr(
        "customer.pipeline.get_url_data",
        fake_get_url_data
    )
    result = run_api_customer_pipeline("https://example.com")
    assert result["customer"]["name"] == "Bob"
    assert result["reason"] == "Invalid age"

def test_run_api_customer_pipeline_rejects_missing_age(monkeypatch):
    def fake_get_url_data(url):
        return {
            "name":"Charlie",
            "age": None,
            "phone":"9876543210"
        }
    monkeypatch.setattr(
        "customer.pipeline.get_url_data",
        fake_get_url_data
    )
    result = run_api_customer_pipeline("https://example.com")
    assert result["customer"]["name"] == "Charlie"
    assert result["reason"] == "Age not mentioned"

def test_run_api_customers_pipeline(monkeypatch):
    def fake_get_url_data(url):
        return [
            {
                "name": "Alice",
                "age": 25,
                "phone":"9876543120"
            },
            {
                "name": "Bob",
                "age":-5,
                "phone" : "9123456780"
            }
        ]
    monkeypatch.setattr(
        "customer.pipeline.get_url_data",
        fake_get_url_data
    )
    result = run_api_customers_pipeline("https://example.com")
    assert len(result["processed"]) == 1
    assert len(result["rejected"]) == 1
    assert result["processed"][0]["name"] == "Alice"
    assert result["rejected"][0]["reason"] == "Invalid age"

def test_run_api_customers_pipeline_rejects_missing_fields(monkeypatch):
    def fake_get_url_data(url):
        return [
            {
                "user_name" : "Charlie",
                "years" : 25
            }
        ]
    monkeypatch.setattr(
        "customer.pipeline.get_url_data",
        fake_get_url_data
    )
    result = run_api_customers_pipeline("https://example.com")
    assert len(result['rejected']) == 1
    assert result['rejected'][0]['reason'] == 'Age not mentioned'

def test_run_api_customers_pipeline_rejects_wrong_age_type(monkeypatch):
    def fake_get_url_data(url):
        return [
            {
                "name" : "David",
                "age" : "25",
                "phone" : "9871234560"
            }
        ]
    monkeypatch.setattr(
        "customer.pipeline.get_url_data",
        fake_get_url_data
    )
    result = run_api_customers_pipeline("https://example.com")
    assert len(result["processed"]) == 0
    assert len(result['rejected']) == 1
    assert result['rejected'][0]['reason'] == 'Incorrect data type'

def test_run_api_customers_pipeline_api_error(monkeypatch):
    import requests
    def fake_get_url_data(url):
        raise requests.RequestException("API unavailable")
    monkeypatch.setattr(
        "customer.pipeline.get_url_data",
        fake_get_url_data
    )
    with pytest.raises(requests.RequestException):
        run_api_customers_pipeline("https://example.com")

def test_run_api_customers_pipeline_cleans_customer(monkeypatch):
    def fake_get_url_data(url):
        return [
            {
                "name":"Alice",
                "age": 25,
                "phone":"9123467580"
            }
        ]
    monkeypatch.setattr(
        "customer.pipeline.get_url_data",
        fake_get_url_data
    )
    result = run_api_customers_pipeline("https://example.com")
    assert len(result["processed"]) == 1
    assert result["processed"][0]["name"] == "Alice"

def test_run_api_customers_pipeline_multiple_valid_customers(monkeypatch):
    def fake_get_url_data(url):
        return [
            {
                "name" : "Alice",
                "age" : 25,
                "phone" : "9213456780"
            },
            {
                "name" : "Bob",
                "age" : 24,
                "phone" : "93124567780"
            }
        ]
    monkeypatch.setattr(
        "customer.pipeline.get_url_data",
        fake_get_url_data
    )
    result = run_api_customers_pipeline("https://example.com")
    assert len(result["processed"]) == 2
    assert len(result["rejected"]) == 0
    assert result['processed'][0]['name'] == 'Alice'
    assert result['processed'][1]['name'] == "Bob"

def test_run_api_customers_pipeline_empty_response(monkeypatch):
    def fake_get_url_data(url):
        return []
    monkeypatch.setattr(
        "customer.pipeline.get_url_data",
        fake_get_url_data
    )
    result = run_api_customers_pipeline("https://example.com")
    assert result['processed'] == []
    assert result['rejected'] == []

def test_run_customer_database_pipeline(tmp_path):
    customer_path = tmp_path / "customers.csv"
    database_path = tmp_path / "astra.db"
    customer_path.write_text(
        "name,age,phone\n"
        "Alice,25,9876543210\n"
        'Bob,30, 91234567789\n'
        "Charlie,abc,9999999999\n"
    )
    result = run_customer_database_pipeline(
        customer_path,
        database_path
    )
    connection = create_connection(database_path)
    customers = get_customers(connection)
    assert len(customers) == 2
    assert len(result['processed']) == 2
    assert len(result["rejected"]) == 1
    connection.close()

def test_pipeline_keeps_previous_customers_when_later_save_fails(tmp_path):
    customer_path = tmp_path / "customers.csv"
    database_path = tmp_path / "astra.db"

    customer_path.write_text(
        "name,age,phone\n"
        "Alice,25,9876543210\n"
        "Bob,30,9123456789\n"
        "Charlie,35,9999999999\n"
    )

    connection = create_connection(database_path)
    create_customers_table(connection)

    connection.execute("""
        CREATE TRIGGER fail_charlie_insert
        BEFORE INSERT ON customers
        WHEN NEW.name = 'Charlie'
        BEGIN
            SELECT RAISE(ABORT, 'Simulated database failure');
        END;
    """)
    connection.commit()
    connection.close()

    with pytest.raises(Exception, match="Simulated database failure"):
        run_customer_database_pipeline(customer_path, database_path)

    connection = create_connection(database_path)
    customers = get_customers(connection)
    connection.close()

    assert [customer["name"] for customer in customers] == [
        "Alice",
        "Bob",
    ]

def test_pipeline_logs_and_reraises_database_failure(
        tmp_path, monkeypatch, caplog
):
    customer_path = tmp_path /"customers.csv"
    database_path = tmp_path/"astra.db"
    customer_path.write_text(
        "name,age,phone\n"
        "Alice,25,9876543210\n"
        "Bob,30, 9123456789\n"
    )
    original_save_customer = pipeline_module.save_customer
    def fail_on_bob(connection,customer):
        if customer["name"] == "Bob":
            raise RuntimeError("Simulated save failure")
        return original_save_customer(connection,customer)
    monkeypatch.setattr(pipeline_module,"save_customer",fail_on_bob)
    caplog.set_level(logging.ERROR)
    with pytest.raises(RuntimeError, match="Simulated save failure"):
        pipeline_module.run_customer_database_pipeline(customer_path, database_path)
    assert "Customer database pipeline failed" in caplog.text
    assert "Simulated save failure" in caplog.text
    
def test_database_pipeline_closes_connection_on_error(tmp_path,monkeypatch):
    from customer import pipeline
    database_path = tmp_path/"astra.db"
    csv_path = tmp_path/"missing.csv"
    connections = []
    original_create_connection = pipeline.create_connection
    def tracked_connection(path):
        connection = original_create_connection(path)
        connections.append(connection)
        return connection
    monkeypatch.setattr(
        pipeline, "create_connection", tracked_connection
    )
    with pytest.raises(FileNotFoundError):
        run_customer_database_pipeline(csv_path, database_path)
    assert len(connections) == 1
    with pytest.raises(Exception, match='closed'):
        connections[0].execute("SELECT 1")

