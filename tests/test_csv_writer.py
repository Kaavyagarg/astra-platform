from customer.csv_writer import write_customers_csv

def test_write_customers_csv(tmp_path):
    path = tmp_path/"output.csv"
    customers = [
        {"name":"Alice","age":"25","phone":"9876543210"},
        {"name":"Bob","age":"17","phone":"9123456780"}
    ]
    write_customers_csv(path,customers)
    assert path.exists()