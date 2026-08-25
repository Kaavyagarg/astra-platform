from customer.cleaner import clean_customer,clean_customers
def test_clean_customer():
    customer ={
        "name":"  Kavya Garg  ",
        "city": "  delhi  ",
        "age" : 29
    }
    result = clean_customer(customer)
    assert result == {
        "name": "Kavya Garg",
        "city": "Delhi",
        "age": 29
    }
def test_clean_customers():
    customers = [
        {"name":"   Kavya   ","city":"  delhi  ","age": 29},
        {"name": "  Rohan  ","city": "  MUMBAI  ","age": 35},
        {"name": "  Anita ","city": "  banglore ","age":28},
        {"name":"Rita","city":"","age": 31}
    ]
    result = clean_customers(customers)

    assert result == [
      {"name":"Kavya","city":"Delhi","age": 29},
      {"name": "Rohan","city": "Mumbai","age": 35},
      {"name": "Anita","city": "Banglore","age":28},
      {"name":"Rita","city":"","age": 31}     
    ]