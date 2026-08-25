from customer.processor import process_customer,process_customers

def test_process_valid_customer():
    customer ={
        "name" : "   Kavya Garg   ",
        "city" : "  delhi  ",
        "age" : 29
    }
    result = process_customer(customer)
    assert result == {
        "name": "Kavya Garg",
        "city": "Delhi",
        "age": 29
    }

def test_process_invalid_customer():
    customer = {
        "name" : "  Rohan  ",
        "city" : " mumbai ",
        "age" : "35"
    }
    result = process_customer(customer)
    assert result == {
        "customer" : customer,
        "reason" : "Incorrect data type"
    }

def test_process_customers():
    customers = [
        {
            "name":"  Kavya  ",
            "city" : " delhi  ",
            "age" : 29
        },
        {
            "name":"  Rohan  ",
            "city" : "  mumbai  ",
            "age" : "35"
        },
        {
            "name":"  Anita  ",
            "city" : " bangalore  ",
            "age" : 28
        }
    ]
    result = process_customers(customers)
    assert result == {
        "processed" : [
            {
                "name":"Kavya",
                "city" : "Delhi",
                "age" : 29
            },
            {
             "name": "Anita",
             "city": "Bangalore",
             "age": 28  
            },
        ],
        "rejected":[
            {
            "customer": {
            "name":"  Rohan  ",
            "city" : "  mumbai  ",
            "age" : "35"
            },
            "reason" : "Incorrect data type"
            }
        ]
    }