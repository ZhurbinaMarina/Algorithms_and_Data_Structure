from lab5.utils import read_data_from_file, write_data_into_file, is_elem


def heapify(n, arr, i, res):
    if i * 2 + 2 < n:
        if (arr[i] > arr[2 * i + 1]) or (arr[i] > arr[2 * i + 2]):
            if arr[2 * i + 1] < arr[2 * i + 2]:
                arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
                res.append(f'{i} {2 * i + 1}')
                heapify(n, arr, 2 * i + 1, res)
            else:
                arr[i], arr[2 * i + 2] = arr[2 * i + 2], arr[i]
                res.append(f'{i} {2 * i + 2}')
                heapify(n, arr, 2 * i + 2, res)
            if arr[2 * i + 1] > arr[2 * i + 2]:
                arr[2 * i + 1], arr[2 * i + 2] = arr[2 * i + 2], arr[2 * i + 1]
    elif i * 2 + 1 < n:
        if arr[i] > arr[i * 2 + 1]:
            arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
            res.append(f'{i} {2 * i + 1}')
            heapify(n, arr, 2 * i + 1, res)


def heap_sort(n, arr):
    res = []
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, arr, i, res)
    print(arr)
    return res

def main(n, data):
    if not is_elem(n, 1, 10 ** 5):
        return ["Введено некорректное значение n"]

    for elem in data:
        if not is_elem(elem, 0, 10 ** 9):
            return ["Введено некорректное значение элемента массива"]

    result = heap_sort(n, data)
    print(result)
    return [str(len(result))] + result


if __name__ == "__main__":
    data_file_path = "../txtf/input.txt"
    output_file_path = "../txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n = int(data.pop(0))
    data = [int(elem) for elem in data[0].split()]

    write_data_into_file(output_file_path, main(n, data))
