from lab5.utils import read_data_from_file, write_data_into_file, is_elem


class TreeDepth:
    def __init__(self, n, parents):
        self._parents = parents
        self._n = n
        self._max_depth = None
        self._depths = [None] * self._n

    def max_depth(self):
        if self._max_depth is not None:
            return self._max_depth
        for idx, parent in enumerate(self._parents):
            parent_stack = []
            while parent != -1 and self._depths[idx] is None:
                parent_stack.append(idx)
                idx, parent = parent, self._parents[parent]
            if parent == -1:
                depth = 0
            else:
                depth = self._depths[idx]
            while parent_stack:
                depth += 1
                self._depths[parent_stack.pop()] = depth
            if self._max_depth is None:
                self._max_depth = depth
            elif self._max_depth < depth:
                self._max_depth = depth
        return [str(self._max_depth + 1)]


def main(n, data):
    if not is_elem(n, 1, 10 ** 5):
        return ["Введено некорректное значение n"]

    for elem in data:
        if not is_elem(elem, -1, n - 1):
            return ["Введено некорректное значение для узла дерева"]


    tree = TreeDepth(n, data)
    max_depth = tree.max_depth()
    return max_depth


if __name__ == "__main__":
    data_file_path = "../txtf/input.txt"
    output_file_path = "../txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n = int(data.pop(0))
    data = [int(elem) for elem in data[0].split()]

    write_data_into_file(output_file_path, main(n, data))
