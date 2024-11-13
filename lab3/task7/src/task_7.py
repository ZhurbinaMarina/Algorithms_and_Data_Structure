from lab3.utils import read_data_from_file, write_data_into_file

ORDER = [chr(i) for i in range(ord('a'), ord('z') + 1)]


def digital_sort(n, s, radix, indx):
    row = s[radix]
    a = [[row[i], i + 1, None] for i in range(n)]
    for i in range(n):
        elem_pos = indx[i] - 1
        a[elem_pos][2] = i

    a.sort(key=lambda x: (x[0], x[2]))
    return [elem[1] for elem in a]


def main(n, m, k, s):
    indx = [i for i in range(1, n + 1)]
    if not (1 <= n <= 10 ** 6):
        return "Введено некорректное значение n"
    if not (1 <= k <= 10 ** 6):
        return "Введено некорректное значение k"
    if not (1 <= m <= 10 ** 6):
        return "Введено некорректное значение m"

    for i in range(k):
        indx = digital_sort(n, s, m - 1 - i, indx)
    return [' '.join([str(elem) for elem in indx])]


if __name__ == "__main__":
    data_file_path = "../txtf/input.txt"
    output_file_path = "../txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n, m, k = map(int, data[0].split())
    a = []
    for i in range(n):
        a.append(data[i + 1].strip())

    write_data_into_file(output_file_path, main(n, m, k, a))
