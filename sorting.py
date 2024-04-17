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


def selection_sort(list_of_numbers, direction=1):
    """
    Sorts numbers from smallest to biggest
    :param list_of_numbers: (list) List of numbers to sort
    :return: (list) List of sorted numbers
    """
    if direction > 0:
        for i in range(1, len(list_of_numbers)):
            for l in range(len(list_of_numbers)):
                if list_of_numbers[l] > list_of_numbers[i]:
                    list_of_numbers[l], list_of_numbers[i] = list_of_numbers[i], list_of_numbers[l]
    else:
        for i in range(1, len(list_of_numbers)):
            for l in range(len(list_of_numbers)):
                if list_of_numbers[l] < list_of_numbers[i]:
                    list_of_numbers[l], list_of_numbers[i] = list_of_numbers[i], list_of_numbers[l]
    return list_of_numbers


def main():
    dictionary = read_data("numbers.csv")
    print(dictionary)
    print(selection_sort(dictionary["series_3"], 1))


if __name__ == '__main__':
    main()
