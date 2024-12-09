from lab4.utils import read_data_from_file, write_data_into_file, is_elem


class Queue:
    def __init__(self, size):
        self.size = size
        self.head = -1
        self.tail = 0
        self.queue = [None] * size

    def enqueue(self, elem):
        if None not in self.queue:
            return "The queue is overcrowded"
        else:
            self.queue[self.tail] = elem
            if self.tail == self.size - 1:
                self.tail = 0
            self.tail += 1
            if self.head == -1:
                self.head = 0
            return None

    def dequeue(self):
        if not any(self.queue):
            return "The queue is empty"
        else:
            elem = self.queue[self.head]
            self.queue[self.head] = None
            if self.head == self.size - 1:
                self.head = 0
            else:
                self.head += 1
            return elem


def main(m, data):
    if not is_elem(m, 1, 10 ** 6):
        return ["Введено некорректное значение m"]

    queue = Queue(m)
    deleted_elements = []

    for command in data:
        if command[0] == "+":
            elem = int(command.split()[1])
            if not is_elem(elem, -10 ** 9, 10 ** 9):
                return ["Введено некорректное значение элемента очереди"]
            result = queue.enqueue(elem)
            if result:
                deleted_elements.append(result)
                return deleted_elements
        elif command[0] == "-":
            result = str(queue.dequeue())
            deleted_elements.append(result)
            if result == "The queue is empty":
                return deleted_elements
    return deleted_elements


if __name__ == "__main__":
    data_file_path = "lab4/task2/txtf/input.txt"
    output_file_path = "lab4/task2/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    m = int(data.pop(0))

    write_data_into_file(output_file_path, main(m, data))

