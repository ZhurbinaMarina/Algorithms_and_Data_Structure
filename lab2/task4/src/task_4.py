from lab2.utils import read_data_from_file, write_data_into_file, check_list_elems


def binary_search(s, value):
    left = 0
    right = len(s) - 1
    while left <= right:
        mid = (left + right) // 2
        if value == s[mid]:
            return mid

        if value > s[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main(n, a, k, b):
    min_elem = 1
    max_elem = 10 ** 9

    if not (1 <= n <= 10 ** 5):
        return "Введено некорректное значение n"
    if not check_list_elems(a, min_elem, max_elem):
        return "В первом массиве имеются числа неудовлетворяющие условию"

    if not (1 <= k <= 10 ** 5):
        return "Введено некорректное значение k"
    if not check_list_elems(b, min_elem, max_elem):
        return "Во втором массиве имеются числа неудовлетворяющие условию"

    result = []
    for elem in b:
        result.append(str(binary_search(a, elem)))
    return [' '.join([str(elem) for elem in result])]


if __name__ == "__main__":
    data_file_path = "../txtf/input.txt"
    output_file_path = "../txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n, a, k, b = int(data[0]), list(map(int, data[1].split())), int(data[2]), list(map(int, data[3].split()))
    write_data_into_file(output_file_path, main(n, a, k, b))
