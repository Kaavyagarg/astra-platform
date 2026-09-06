from customer.analysis import get_customer_names, get_customer_positions,sort_customers_by_age,count_age_groups
def test_get_customer_names():
    customers = [
        {"name":"Alice","age":"25"},
        {"name":"Bob","age":"17"}
    ]
    assert get_customer_names(customers) == ["Alice","Bob"]

def test_get_customer_positions():
    customers = [
            {"name":"Alice","age":"25"},
            {"name":"Bob","age":"17"}
        ]
    assert get_customer_positions(customers) == [(0,"Alice"),(1,"Bob")]

def test_sort_customers_by_age():
    customers = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 17},
        {"name": "Charlie", "age": 35},
    ]
    assert sort_customers_by_age(customers) == [
        {"name":"Bob","age":17},
        {"name":"Alice","age":25},
        {"name":"Charlie","age":35}
    ]

def test_count_age_groups():
    customers = [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 17},
            {"name": "Charlie", "age": 35},
        ]
    assert count_age_groups(customers) == {"adult":2,"minor":1}