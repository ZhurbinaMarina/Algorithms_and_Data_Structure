from lab1.utils import read_data_from_file, write_data_into_file, check_list_elems


def main(n, s):
    min_elem = -10 ** 9
    max_elem = 10 ** 9

    if not (1 <= n <= 10 ** 3):
        return "Введено некорректное значение n"
    if not check_list_elems(s, min_elem, max_elem):
        return "В массиве имеются числа неудовлетворяющие условию"

    for i in range(1, n):
        a = s[i]
        j = i - 1
        while j >= 0 and a < s[j]:
            s[j + 1] = s[j]
            j = j - 1
        s[j + 1] = a
    return [' '.join(map(str, s))]


if __name__ == "__main__":
    data_file_path = "lab1/task1/txtf/input.txt"
    output_file_path = "lab1/task1/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n, s = int(data[0]), list(map(int, data[1].split()))

    write_data_into_file(output_file_path, main(n, s))
