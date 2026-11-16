from customer.csv_reader import read_customers_csv
import pytest

from customer.csv_reader import read_customers_csv



def test_read_customers_csv():
    assert read_customers_csv("data/customers.csv") == [{'name': 'Alice', 'age': '25', 'phone': '9876543210'}, {'name': 'Bob', 'age': '17', 'phone': '9123456780'}, {'name': 'Charlie', 'age': 'abc', 'phone': '9999999999'}]

def test_read_customers_csv():
    assert read_customers_csv("data/customers.csv") == [
        {'name': 'Alice', 'age': '25', 'phone': '9876543210'},
        {'name': 'Bob', 'age': '17', 'phone': '9123456780'},
        {'name': 'Charlie', 'age': 'abc', 'phone': '9999999999'}
    ]


def test_read_customers_csv_file_not_found(tmp_path):
    file_path = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        read_customers_csv(file_path)