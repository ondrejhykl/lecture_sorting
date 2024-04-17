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
        for l in range(len(list_of_numbers) - 1 - i):
            if list_of_numbers[l] > list_of_numbers[l + 1]:
                list_of_numbers[l], list_of_numbers[l + 1] = list_of_numbers[l + 1], list_of_numbers[l]
    return list_of_numbers


def insertion_sort(list_of_numbers):
    for i in range(1, len(list_of_numbers)):
        current_num = list_of_numbers.pop(i)
        j = i
        while j > 0:
            j -= 1
            if current_num > list_of_numbers[j]:
                j += 1
                break
        list_of_numbers.insert(j, current_num)
    return list_of_numbers


def main():
    dictionary = read_data("numbers.csv")
    print(dictionary)
    print(selection_sort(dictionary["series_3"].copy(), 1))
    print(bubble_sort(dictionary["series_3"].copy()))
    print(insertion_sort(dictionary["series_3"].copy()))


if __name__ == '__main__':
    main()
