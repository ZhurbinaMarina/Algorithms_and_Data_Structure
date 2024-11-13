from lab3.utils import read_data_from_file, write_data_into_file, check_list_elems, generate_random_int


# Randomized-QuickSort +
def partition3(a, l, r):
    x = a[l]
    m1 = l
    m2 = r
    i = l
    while i <= m2:
        if a[i] < x:
            a[m1], a[i] = a[i], a[m1]
            m1 += 1
            i += 1
        elif a[i] > x:
            a[i], a[m2] = a[m2], a[i]
            m2 -= 1
        else:
            i += 1
    return m1, m2


def randomized_quick_sort_p3(a, l, r):
    if l < r:
        k = generate_random_int(l, r)
        a[l], a[k] = a[k], a[l]
        m1, m2 = partition3(a, l, r)
        randomized_quick_sort_p3(a, l, m1 - 1)
        randomized_quick_sort_p3(a, m2 + 1, r)


def main(n, s):
    min_elem = -10 ** 9
    max_elem = 10 ** 9

    if not (1 <= n <= 10 ** 4):
        return "Введено некорректное значение n"
    if not check_list_elems(s, min_elem, max_elem):
        return "В массиве имеются числа неудовлетворяющие условию"

    randomized_quick_sort_p3(s, 0, len(s) - 1)
    return [' '.join([str(elem) for elem in s])]


if __name__ == "__main__":
    data_file_path = "../txtf/input.txt"
    output_file_path = "../txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n, s = int(data[0]), list(map(int, data[1].split()))
    write_data_into_file(output_file_path, main(n, s))
