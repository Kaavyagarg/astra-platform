import csv
def read_customers_csv(path):
    with open(path,'r',encoding="utf-8",newline="") as file:
        reader = csv.DictReader(file)
        customers =[]
        for row in reader:
            customers.append(row)
        return customers

