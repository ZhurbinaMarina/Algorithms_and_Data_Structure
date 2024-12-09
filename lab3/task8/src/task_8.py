from lab3.utils import read_data_from_file, write_data_into_file


def main(n, k, coords):
    if not (1 <= n <= 10 ** 5):
        return "Введено некорректное значение n"
    if not (1 <= k <= 10 ** 5):
        return "Введено некорректное значение k"

    coords.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2) ** 0.5)
    result = ','.join([str(elem) for elem in coords[:k]]).replace(' ', '')
    return [result]


if __name__ == "__main__":
    data_file_path = "lab3/task8/txtf/input.txt"
    output_file_path = "lab3/task8/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n, k = map(int, data[0].split())
    coords = []

    for i in range(n):
        coords.append(list(map(int, data[i + 1].split())))

    write_data_into_file(output_file_path, main(n, k, coords))
