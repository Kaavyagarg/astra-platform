def get_customer_names(customers):
    list_name =[]
    for customer in customers:
        list_name.append(customer["name"])
    return list_name
customers = [
    {"name": "Alice", "age": "25"},
    {"name": "Bob", "age": "17"},
]
print(get_customer_names(customers))