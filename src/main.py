import json

def load_operations():
    with open('../trash/operations.json', ) as f:
        return json.load(f)
