"""
Program to check file from json
"""

import json
from os.path import exists as file_exists

def check_file_from_json():
    with open("./json_xml/json/sample.json", "r") as f:
        data = json.load(f)
    for folder in data:
        for file in data[folder]:
            if file_exists(f'./{folder}/{file}'):
                print(f"{file} exists in {folder}")
            else:
                print(f"{file} does not exists in {folder}")


if __name__ == "__main__":
    check_file_from_json()