import argparse
from lab7.utils import read_data_from_file, is_elem, write_data_into_file


def min_operations(n):
    queue = [(1, 0)]
    visited = {1}
    parent = {1: None}

    while queue:
        current, steps = queue.pop(0)

        if current == n:

            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return steps, path

        for next_num in (current + 1, current * 2, current * 3):
            if next_num <= n and next_num not in visited:
                visited.add(next_num)
                parent[next_num] = current
                queue.append((next_num, steps + 1))


def main(n):
    if not is_elem(n, 1, 10 ** 6):
        return ["Введено некорректное значение n"]

    steps, path = min_operations(n)
    return [str(steps), ' '.join([str(elem) for elem in path])]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?', const='..', type=str, default='..')
    args = parser.parse_args()

    data_file_path = f"{args.filepath}/txtf/input.txt"
    output_file_path = f"{args.filepath}/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n = int(data.pop(0))

    write_data_into_file(output_file_path, main(n))
