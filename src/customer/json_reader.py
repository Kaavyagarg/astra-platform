import json
from pathlib import Path
def read_customer_json(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    with open(path,'r',encoding = "utf-8") as file:
        customers = json.load(file)
    return customers

