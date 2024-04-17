import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as numbers_file:
        reader = csv.DictReader(numbers_file)
        data = {}
        for row in reader:
            for key in row.keys():
                if key not in data:
                    data[key] = [int(row[key])]
                else:
                    data[key].append(int(row[key]))
        return data


def selection_sort(list_of_numbers, direction=1):   # direction > 0 - vzestupně, direction < 0 - sestupně
    """
    Sorts numbers from smallest to biggest
    :param list_of_numbers: (list) List of numbers to sort
    :return: (list) List of sorted numbers
    """

    for i in range(len(list_of_numbers)):
        min_idx = i
        for l in range(i + 1, len(list_of_numbers)):
            if direction > 0:
                if list_of_numbers[min_idx] > list_of_numbers[l]:
                    min_idx = l
            elif direction < 0:
                if list_of_numbers[min_idx] < list_of_numbers[l]:
                    min_idx = l
            else:
                return None
        list_of_numbers[min_idx], list_of_numbers[i] = list_of_numbers[i], list_of_numbers[min_idx]
    return list_of_numbers


def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers) - 1):
        for l in range(len(list_of_numbers) - 1):
            if list_of_numbers[l] > list_of_numbers[l + 1]:
                list_of_numbers[l], list_of_numbers[l + 1] = list_of_numbers[l + 1], list_of_numbers[l]
    return list_of_numbers


def insertion_sort():
    ...


def main():
    dictionary = read_data("numbers.csv")
    print(dictionary)
    print(selection_sort(dictionary["series_1"], 1))
    print(bubble_sort(dictionary["series_1"]))


if __name__ == '__main__':
    main()
