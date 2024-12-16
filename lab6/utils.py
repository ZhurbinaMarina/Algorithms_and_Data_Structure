import random
from time import time


def generate_list(size, min_elem, max_elem):
    return [random.randint(min_elem, max_elem) for _ in range(size)]


def generate_random_int(min_elem, max_elem):
    return random.randint(min_elem, max_elem)


def is_list_elems(arr, min_elem, max_elem):
    for elem in arr:
        if not (min_elem <= elem <= max_elem):
            return False
    return True


def is_elem(elem, min_elem, max_elem):
    if min_elem <= elem <= max_elem:
        return True
    return False


def is_len_line(s, min_len, max_len):
    if min_len <= len(s) <= max_len:
        return True
    return False


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
    f = open(file_path, 'wt', encoding="utf-8")
    for row in data:
        f.write(row + '\n')
    f.close()
