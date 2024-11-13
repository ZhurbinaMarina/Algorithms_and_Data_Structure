from lab2.utils import read_data_from_file, write_data_into_file, check_list_elems


def popular_elem(s, start, end):
    if start == end:
        return s[end]
    mid = (start + end) // 2
    left = popular_elem(s, start, mid)
    right = popular_elem(s, mid + 1, end)

    if left == right:
        return left
    left_count = sum(1 for i in range(start, end + 1) if s[i] == left)
    right_count = sum(1 for i in range(start, end + 1) if s[i] == right)

    return left if left_count > right_count else right


def main(n, s):
    min_elem = 0
    max_elem = 10 ** 9

    if not (1 <= n <= 10 ** 5):
        return "Введено некорректное значение n"
    if not check_list_elems(s, min_elem, max_elem):
        return "В массиве имеются числа неудовлетворяющие условию"

    answ = popular_elem(s, 0, n - 1)
    if s.count(answ) > n / 2:
        return ["1"]
    return ["0"]


if __name__ == "__main__":
    data_file_path = "../txtf/input.txt"
    output_file_path = "../txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n, s = int(data[0]), list(map(int, data[1].split()))
    write_data_into_file(output_file_path, main(n, s))
