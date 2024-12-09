from lab3.utils import read_data_from_file, write_data_into_file, is_list_elems


def scarecrow_sort(n, k, s):
    a = [[] for _ in range(k)]
    for i in range(k):
        for j in range(i, n, k):
            a[i].append(s[j])

    for elem in a:
        elem.sort(reverse=True)

    result = []
    for i in range(len(a[0])):
        for elem in a:
            if len(elem) > 0:
                result.append(elem.pop())
    return result == sorted(s)


def main(n, k, s):
    min_elem = -10 ** 9
    max_elem = 10 ** 9

    if not (1 <= n <= 10 ** 5):
        return "Введено некорректное значение n"
    if not (1 <= k <= 10 ** 5):
        return "Введено некорректное значение k"
    if not is_list_elems(s, min_elem, max_elem):
        return "В массиве имеются числа неудовлетворяющие условию"

    result = [scarecrow_sort(n, k, s), scarecrow_sort(n, k, s[::-1])]
    if any(result):
        return ["ДА"]
    return ["НЕТ"]


if __name__ == "__main__":
    data_file_path = "lab3/task3/txtf/input.txt"
    output_file_path = "lab3/task3/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n, k = map(int, data[0].split())
    s = list(map(int, data[1].split()))

    write_data_into_file(output_file_path, main(n, k, s))
