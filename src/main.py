import json

def load_operations():
    with open('operations.json', ) as f:
        return json.load(f)
