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

def get_customer_positions(customers):
    list_name = []
    for i, customer in enumerate(customers):
        list_name.append((i,customer['name']))
    return list_name
customers = [
    {"name": "Alice", "age": "25"},
    {"name": "Bob", "age": "17"},
]
print(get_customer_positions(customers))

def sort_customers_by_age(customers):
    return sorted(customers, key = lambda customer:customer["age"])

def count_age_groups(customers):
    counts = {
        "adult":0,
        "minor":0
    }
    for customer in customers:
        if customer["age"] >= 18:
            counts["adult"] += 1
        else:
            counts["minor"] += 1
    return counts 