import json 
import pytest
from customer.json_reader import read_customer_json

def test_read_customer_json(tmp_path):
    file_path = tmp_path/"customers.json"
    customers = [
        {"name":"Bob","age":17,"phone":"9123456780"}
    ]
    file_path.write_text(json.dumps(customers), encoding="utf-8")
    result = read_customer_json(file_path)
    assert result == customers

def test_read_customer_json_file_not_found(tmp_path):
    file_path = tmp_path / "missing.json"
    with pytest.raises(FileNotFoundError):
        read_customer_json(file_path)
def test_read_customer_json_invalid_format(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text('[{"name":"Bob"',encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        read_customer_json(file_path)