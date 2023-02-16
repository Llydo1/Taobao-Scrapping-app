import os
import json

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return True

def write_json_to_file(path, data):
    try:
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
            print(f"Successfully written JSON to {path}")
    except Exception as e:
        print(f"An error occurred while writing JSON to {path}: {e}")
        return False
    return True