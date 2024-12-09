from lab2.utils import read_data_from_file, write_data_into_file, check_list_elems


def merge_sort(s, left, right):
    cnt = 0
    if left < right:
        mid = (left + right) // 2
        cnt += merge_sort(s, left, mid)
        cnt += merge_sort(s, mid + 1, right)
        cnt += merge(s, left, mid, right)
    return cnt


def merge(s, left, mid, right):
    cnt = 0
    s_l = s[left:mid + 1] + [10 ** 10]
    s_r = s[mid + 1:right + 1] + [10 ** 10]

    i, j = 0, 0
    for k in range(left, right + 1):
        if s_l[i] <= s_r[j]:
            s[k] = s_l[i]
            i += 1
        else:
            s[k] = s_r[j]
            j += 1
            cnt += len(s_l) - i - 1
    return cnt


def main(n, s):
    min_elem = -10 ** 9
    max_elem = 10 ** 9

    if not (1 <= n <= 10 ** 5):
        return "Введено некорректное значение n"
    if not check_list_elems(s, min_elem, max_elem):
        return "В массиве имеются числа неудовлетворяющие условию"

    return [str(merge_sort(s, 0, len(s) - 1))]


if __name__ == "__main__":
    data_file_path = "lab2/task3/txtf/input.txt"
    output_file_path = "lab2/task3/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n, s = int(data[0]), list(map(int, data[1].split()))
    write_data_into_file(output_file_path, main(n, s))
