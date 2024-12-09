from lab1.utils import read_data_from_file, write_data_into_file


def main(n, s):
    if not (1 <= n <= 10 ** 5):
        return "Введено некорректное значение n"

    ord_A = ord("A")
    a = [0] * (ord("Z") - ord_A + 1)
    for elem in s:
        a[ord(elem) - ord_A] += 1
    left_side = ''
    center = ''
    for i in range(len(a)):
        ch, cnt = chr(i + ord_A), a[i]
        h = ch * (cnt // 2)
        left_side += h
        if center == "" and cnt % 2 == 1:
            center = ch
    return [left_side + center + left_side[::-1]]


if __name__ == "__main__":
    data_file_path = "lab1/task10/txtf/input.txt"
    output_file_path = "lab1/task10/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n, s = int(data[0]), data[1]

    write_data_into_file(output_file_path, main(n, s))
