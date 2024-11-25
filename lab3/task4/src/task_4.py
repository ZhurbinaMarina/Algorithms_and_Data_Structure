from lab3.utils import read_data_from_file, write_data_into_file, is_list_elems


def main(s, p, segments, points):
    min_elem = -10 ** 8
    max_elem = 10 ** 8

    if not (1 <= s <= 5 * 10 ** 4):
        return "Введено некорректное значение s"
    if not (1 <= p <= 5 * 10 ** 4):
        return "Введено некорректное значение p"
    if not is_list_elems([elem[0] for elem in segments], min_elem, max_elem) or not is_list_elems(
            [elem[1] for elem in segments], min_elem, max_elem):
        return "В массиве отрезков имеются числа неудовлетворяющие условию"
    if not is_list_elems(points, min_elem, max_elem):
        return "В массиве точек имеются числа неудовлетворяющие условию"

    elems_with_type = []

    for start, end in segments:
        elems_with_type.append((start, 'start'))
        elems_with_type.append((end, 'end'))

    for point in points:
        elems_with_type.append((point, 'point'))

    elems_with_type.sort(key=lambda x: (x[0], x[1] == 'end'))

    result = {}
    cnt = 0

    for event in elems_with_type:
        if event[1] == 'start':
            cnt += 1
        elif event[1] == 'end':
            cnt -= 1
        else:
            result[event[0]] = cnt

    return [' '.join([str(result[point]) for point in points])]


if __name__ == "__main__":
    data_file_path = "../txtf/input.txt"
    output_file_path = "../txtf/output.txt"

    data = read_data_from_file(data_file_path)
    s, p = map(int, data[0].split())
    segments = []

    for i in range(s):
        segments.append(list(map(int, data[i + 1].split())))
    points = list(map(int, data[s + 1].split()))
    write_data_into_file(output_file_path, main(s, p, segments, points))
