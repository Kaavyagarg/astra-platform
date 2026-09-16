from customer.pipeline import run_customer_pipeline
import pytest
from customer.parser import convert_age
from customer.csv_reader import read_customers_csv
from customer.pipeline import run_api_customer_pipeline
from customer.pipeline import run_api_customers_pipeline
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