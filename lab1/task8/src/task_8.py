from lab1.utils import read_data_from_file, write_data_into_file, check_list_elems


def main(n, s):
    output_file_path = "lab1/task8/txtf/output.txt"
    min_elem = -10 ** 9
    max_elem = 10 ** 9

    if not (1 <= n <= 10 ** 3):
        return "Введено некорректное значение n"
    if not check_list_elems(s, min_elem, max_elem):
        return "В массиве имеются числа неудовлетворяющие условию"

    result = []
    for i in range(0, n - 1):
        ind = i
        for j in range(i + 1, n):
            if s[j] < s[ind]:
                ind = j
        if i != ind:
            s[i], s[ind] = s[ind], s[i]
            result.append(f'Swap elements at indices {i + 1} and {ind + 1}.')
    result.append('No more swaps needed.')
    write_data_into_file(output_file_path, result)
    return [' '.join(map(str, s))]


if __name__ == "__main__":
    data_file_path = "lab1/task8/txtf/input.txt"
    output_file_path = "lab1/task8/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n, s = int(data[0]), list(map(int, data[1].split()))

    main(n, s)
