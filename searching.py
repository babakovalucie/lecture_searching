import time
from pathlib import Path
import json
from generators import unordered_sequence, ordered_sequence
import matplotlib.pyplot as plt


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
    # jeste dalsi moznost:
    #    for i in range(len(searched_data)):
    #        if searched_data[i] == searched_number:
    #            count += 1
    #            positions.append(i)

    searched_dictionary["positions"] = positions
    searched_dictionary["count"] = count
    return searched_dictionary

def binary_search(searched_data, searched_number):
    left = 0
    right = len(searched_data) - 1
    while left <= right:
        mid = (left + right) // 2
        if searched_data[mid] == searched_number:
            return mid
        elif searched_data[mid] < searched_number:
            left = mid + 1
        else:
            right = mid - 1
    return None

def test_complexity(list_of_n):
    for n in list_of_n:
        number = 5
        unordered_data = unordered_sequence(n)
        ordered_data = ordered_sequence(n)
        times_linear = []
        times_binary = []
        duration_linear = 0
        duration_binary = 0
        repetitions = 100
        for measurments in range(100):
            start_time_linear = time.perf_counter()
            found_number = linear_search(unordered_data, number)
            end_time_linear = time.perf_counter()
            duration_linear += end_time_linear - start_time_linear

            start_time_binary = time.perf_counter()
            found_number = binary_search(ordered_data, number)
            end_time_binary = time.perf_counter()
            duration_binary += end_time_binary - start_time_binary
        times_linear.append(duration_linear / repetitions)
        times_binary.append(duration_binary / repetitions)

def pattern_search(sequence, pattern):
    idx = {}
    return idx

def main():
    my_data = read_data("sequential.json","unordered_numbers")
    print(my_data)
    found_numbers = linear_search(my_data,5)
    print(found_numbers)

    my_data_2 = read_data("sequential.json","ordered_numbers")



    print(found_number)
    print(duration)
if __name__ == "__main__":
    main()
