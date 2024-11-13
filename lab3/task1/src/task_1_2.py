from lab3.utils import read_data_from_file, write_data_into_file, check_list_elems, generate_random_int


# Randomized-QuickSort
def partition(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l < r:
        k = generate_random_int(l, r)
        a[l], a[k] = a[k], a[l]
        m = partition(a, l, r)
        randomized_quick_sort(a, l, m - 1)
        randomized_quick_sort(a, m + 1, r)


def main(n, s):
    min_elem = -10 ** 9
    max_elem = 10 ** 9

    if not (1 <= n <= 10 ** 4):
        return "Введено некорректное значение n"
    if not check_list_elems(s, min_elem, max_elem):
        return "В массиве имеются числа неудовлетворяющие условию"

    randomized_quick_sort(s, 0, len(s) - 1)
    return [' '.join([str(elem) for elem in s])]


if __name__ == "__main__":
    data_file_path = "../txtf/input.txt"
    output_file_path = "../txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n, s = int(data[0]), list(map(int, data[1].split()))
    write_data_into_file(output_file_path, main(n, s))
