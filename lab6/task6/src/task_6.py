import argparse
from math import sqrt
from lab6.utils import read_data_from_file, is_elem, write_data_into_file


def is_perfect_square(n):
    s = int(sqrt(n))
    return s ** 2 == n


def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4);


def main(n, a):
    if not is_elem(n, 1, 10 ** 6):
        return ["Введено некорректное значение n"]

    for elem in a:
        if not is_elem(elem, -1, 10 ** 500):
            return ["Введено некорректное значение числа для проверки"]
    answer = []
    for elem in a:
        if is_fibonacci(elem):
            answer.append("Yes")
        else:
            answer.append("No")
    return answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?', const='..', type=str, default='..')
    args = parser.parse_args()

    data_file_path = f"{args.filepath}/txtf/input.txt"
    output_file_path = f"{args.filepath}/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n = int(data.pop(0))
    data = [int(elem) for elem in data]

    write_data_into_file(output_file_path, main(n, data))
