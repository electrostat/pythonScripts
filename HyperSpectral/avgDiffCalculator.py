import csv
import os
import re

#Calculates the average difference between corresponding elements of two lists.
def average_difference(list1, list2):
    if not list1 or not list2 or len(list1) != len(list2):
        return None

    differences = [abs(float(x) - float(y[:-2])) for x, y in zip(list1, list2)]
    return sum(differences) / len(differences)

#Extracts a specific column from a text file and returns it as a list.
def column_to_list(file_path, column_index, delimiter='|'):
    try:
        with open("output.txt", 'r') as file:
            column_list = []
            for line in file:
                values = line.strip().split(delimiter)
                if column_index < len(values):
                    column_list.append(values[column_index])
        return column_list
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

