import random
from time import time


def generate_list(size, min_elem, max_elem):
    return [random.randint(min_elem, max_elem) for _ in range(size)]


def check_list_elems(arr, min_elem, max_elem):
    for elem in arr:
        if not (min_elem <= elem <= max_elem):
            return False
    return True


def measurement_of_time(func, *args):
    start_time = time()
    result = func(*args)
    return [result, time() - start_time]


def read_data_from_file(file_path):
    f = open(file_path)
    data = f.readlines()
    f.close()
    return data


def write_data_into_file(file_path, data):
    f = open(file_path, 'wt')
    for row in data:
        f.write(row + '\n')
    f.close()
