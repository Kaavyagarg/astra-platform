from pathlib import Path
path = Path("data/customers.txt")
if not path.exists():
    raise FileNotFoundError(f"File not found: {path}")
def read_customers_file(path):
    with open(path,'r') as file:
        lines = file.readlines()
        cleaned_lines =[]
        for line in lines:
            cleaned_lines.append(line.strip('\n'))
    return cleaned_lines

customers = read_customers_file("data/customers.txt")
print(customers)