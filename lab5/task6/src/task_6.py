from lab5.utils import read_data_from_file, write_data_into_file, is_elem

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.n = 0
        self.commands = []

    def insert(self, x):
        self.heap.append(x)
        self.commands.append(x)
        self.n += 1
        for i in range(self.n // 2 - 1, -1, -1):
            self._heapify(i)

    def _heapify(self, i):
        if i * 2 + 2 < self.n:
            if (self.heap[i] > self.heap[2 * i + 1]) or (self.heap[i] > self.heap[2 * i + 2]):
                if self.heap[2 * i + 1] < self.heap[2 * i + 2]:
                    self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                    self._heapify(2 * i + 1)
                else:
                    self.heap[i], self.heap[2 * i + 2] = self.heap[2 * i + 2], self.heap[i]
                    self._heapify(2 * i + 2)
                if self.heap[2 * i + 1] > self.heap[2 * i + 2]:
                    self.heap[2 * i + 1], self.heap[2 * i + 2] = self.heap[2 * i + 2], self.heap[2 * i + 1]
        elif i * 2 + 1 < self.n:
            if self.heap[i] > self.heap[i * 2 + 1]:
                self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                self._heapify(2 * i + 1)

    def increase_key(self, i, key):
        elem = self.commands[i]
        self.heap[self.heap.index(elem)] = key
        self.commands.append("-")
        for i in range(self.n // 2 - 1, -1, -1):
            self._heapify(i)

    def extraxt_min(self):
        if len(self.heap) > 0:
            _min = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.commands.append("-")
            self.n -= 1
            for i in range(self.n // 2 - 1, -1, -1):
                self._heapify(i)
            return _min
        return "*"


def main(n, data):
    if not is_elem(n, 1, 10 ** 6):
        return ["Введено некорректное значение n"]

    queue = PriorityQueue()
    result = []
    for elem in data:
        if elem[0] == "A":
            queue.insert(int(elem.split()[1]))
        elif elem[0] == "X":
                _min = queue.extraxt_min()
                result.append(str(_min))
        elif elem[0] == "D":
            elem = elem.split()
            queue.increase_key(int(elem[1]) - 1, int(elem[2]))

    return result


if __name__ == "__main__":
    data_file_path = "lab5/task6/txtf/input.txt"
    output_file_path = "lab5/task6/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n = int(data.pop(0))

    write_data_into_file(output_file_path, main(n, data))