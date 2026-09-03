from customer.analysis import get_customer_names
def test_get_customer_names():
    customers = [
        {"name":"Alice","age":"25"},
        {"name":"Bob","age":"17"}
    ]
    assert get_customer_names(customers) == ["Alice","Bob"]