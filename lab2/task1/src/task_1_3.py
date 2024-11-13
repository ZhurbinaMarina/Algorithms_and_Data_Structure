from lab2.utils import read_data_from_file, write_data_into_file, check_list_elems


def merge_sort(s):
    if len(s) > 1:
        mid = len(s) // 2
        s_left = s[:mid]
        s_right = s[mid:]
        if len(s_left) > 1:
            s_left = merge_sort(s_left)
        if len(s_right) > 1:
            s_right = merge_sort(s_right)

        return merge(s_left, s_right)


def merge(s_left, s_right):
    s = [0] * (len(s_left) + len(s_right))

    s_left.append(10 ** 10)
    s_right.append(10 ** 10)
    i, j = 0, 0
    for k in range(len(s)):
        if s_left[i] <= s_right[j]:
            s[k] = s_left[i]
            i += 1
        else:
            s[k] = s_right[j]
            j += 1
    return s


def main(n, s):
    min_elem = -10 ** 9
    max_elem = 10 ** 9

    if not (1 <= n <= 2 * 10 ** 4):
        return "Введено некорректное значение n"
    if not check_list_elems(s, min_elem, max_elem):
        return "В массиве имеются числа неудовлетворяющие условию"

    s = merge_sort(s)
    return [' '.join([str(elem) for elem in s])]


if __name__ == "__main__":
    data_file_path = "../txtf/input.txt"
    output_file_path = "../txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n, s = int(data[0]), list(map(int, data[1].split()))

    write_data_into_file(output_file_path, main(n, s))
