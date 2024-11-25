from lab4.utils import read_data_from_file, write_data_into_file, is_elem
class Queue:
    def __init__(self, size):
        self.size = size
        self.head = -1
        self.tail = 0
        self.queue = [None] * size

    def enqueue(self, elem, command):
        if None not in self.queue:
            return "The queue is overcrowded"
        else:
            if command == "+":
                self.queue[self.tail] = elem
            elif command == "*":
                if (self.tail - self.head) % 2 == 0:
                    self.queue[(self.tail - self.head) // 2 + 1 + self.head: self.tail + 1] = self.queue[(self.tail - self.head) // 2 + self.head:self.tail]
                    self.queue[(self.tail - self.head) // 2 + self.head] = elem
                else:
                    self.queue[(self.tail - self.head) // 2 + 2 + self.head: self.tail + 1] = self.queue[(self.tail - self.head) // 2 + 1 + self.head:self.tail]
                    self.queue[(self.tail - self.head) // 2 + 1 + self.head] = elem
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
    if not is_elem(m, 1, 10 **5):
        return ["Введено некорректное значение m"]

    queue = Queue(m)
    deleted_elements = []

    for command in data:
        if command[0] == "+" or command[0] == "*":
            elem = int(command.split()[1])
            result = queue.enqueue(elem, command[0])
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
    data_file_path = "../txtf/input.txt"
    output_file_path = "../txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n = int(data.pop(0))

    write_data_into_file(output_file_path, main(n, data))
