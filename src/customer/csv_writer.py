import csv
def write_customers_csv(path,customers):
    with open(path,"w",newline="") as file:
        fieldnames = ["name","age","phone"]
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(customers)
        