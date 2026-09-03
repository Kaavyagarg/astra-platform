import csv
def read_customers_csv(path):
    with open(path,'r') as file:
        reader = csv.DictReader(file)
        customers =[]
        for row in reader:
            customers.append(row)
        return customers

customers = read_customers_csv("data/customers.csv")
print(customers)