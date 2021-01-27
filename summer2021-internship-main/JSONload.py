import json

def js_r(filename: str): # Parses json data from given file
    with open(filename) as f_in:
        return json.load(f_in)


