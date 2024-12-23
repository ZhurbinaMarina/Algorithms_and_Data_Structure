import argparse
from lab7.utils import read_data_from_file, is_elem, write_data_into_file


def count_money(n, moneys, i, a):
    if n in a:
        return i
    else:
        new_a = set()
        for elem in a:
            for money in moneys:
                new_a.add(elem + money)

    return count_money(n, moneys, i + 1, new_a)


def main(n, k, a):
    if not is_elem(n, 1, 10 ** 3):
        return ["Введено некорректное значение n"]
    if not is_elem(n, 1, 100):
        return ["Введено некорректное значение k"]

    for elem in a:
        if not is_elem(elem, -1, 10 ** 500):
            return ["Введено некорректное значение номинала монеты"]
    answer = count_money(n, a, 0, {0})
    return [str(answer)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?', const='..', type=str, default='..')
    args = parser.parse_args()

    data_file_path = f"{args.filepath}/txtf/input.txt"
    output_file_path = f"{args.filepath}/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n, k = map(int, data.pop(0).split())
    data = [int(elem) for elem in data[0].split()]

    write_data_into_file(output_file_path, main(n, k, data))
