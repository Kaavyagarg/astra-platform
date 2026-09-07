from customer.pipeline import run_customer_pipeline
import pytest
from customer.parser import convert_age
from customer.csv_reader import read_customers_csv
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

