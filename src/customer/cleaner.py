def clean_customer(customer):
    cleaned_customer = {
        "name" : customer['name'].strip(),
        "city" : customer.get("city","Unknown").strip().title(),
        "age" : customer['age']
    }


    return cleaned_customer

def clean_customers(customers):
    cleaned_customers = []
    for customer in customers:
        cleaned_customers.append(clean_customer(customer))
    return cleaned_customers

       