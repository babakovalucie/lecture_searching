from pathlib import Path
import json


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name
    with open(file_path, mode="r") as file:
        data = json.load(file)
    if field in data.keys():
        return data[field]
    else:
        return None

def linear_search(searched_data, searched_number):
    positions = []
    count = 0
    idx = 0
    searched_dictionary = {}
    while idx < len(searched_data):
        if searched_data[idx] == searched_number:
            count += 1
            positions.append(idx)
        idx += 1

    searched_dictionary["positions"] = positions
    searched_dictionary["count"] = count
    return searched_dictionary

def main():
    my_data = read_data("sequential.json","unordered_numbers")
    print(my_data)
    found_numbers = linear_search(my_data,5)
    print(found_numbers)
if __name__ == "__main__":
    main()
