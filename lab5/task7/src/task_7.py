from lab5.utils import read_data_from_file, write_data_into_file, is_elem


def heap_sort(n, arr):
    build_max_heap(n, arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, index=0, size=i)
    return [" ".join([str(elem) for elem in arr])]


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(n, arr):
    start = parent(n - 1)
    while start >= 0:
        max_heapify(arr, index=start, size=n)
        start = start - 1


def max_heapify(arr, index, size):
    l = left(index)
    r = right(index)
    if (l < size and arr[l] < arr[index]):
        largest = l
    else:
        largest = index
    if (r < size and arr[r] < arr[largest]):
        largest = r
    if (largest != index):
        arr[largest], arr[index] = arr[index], arr[largest]
        max_heapify(arr, largest, size)

def main(n, data):
    if not is_elem(n, 1, 10 ** 5):
        return ["Введено некорректное значение n"]

    for elem in data:
        if not is_elem(elem, -10 ** 9, 10 ** 9):
            return ["Введено некорректное значение элемента массива"]

    result = heap_sort(n, data)
    return result


if __name__ == "__main__":
    data_file_path = "lab5/task7/txtf/input.txt"
    output_file_path = "lab5/task7/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n = int(data.pop(0))
    data = [int(elem) for elem in data[0].split()]

    write_data_into_file(output_file_path, main(n, data))
