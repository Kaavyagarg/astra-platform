from customer.file_reader import read_customers_file
import pytest
def test_file_reader():
    assert read_customers_file("data/customers.txt")==['Alice','Bob','Charlie']
def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_customers_file("data/does_not_exist.txt")