from lab4.utils import read_data_from_file, write_data_into_file, is_elem


class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.stack = [None] * size

    def enqueue(self, elem):
        if None not in self.stack:
            return "The stack is overcrowded"
        else:
            self.top += 1
            self.stack[self.top] = elem
            return None

    def dequeue(self):
        if self.stack_empty():
            return "The stack is empty"
        else:
            elem = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return elem

    def stack_empty(self):
        if self.top == -1:
            return True
        return False

    def last_elem(self):
        return self.stack[self.top]

    def first_elem(self):
        return self.stack[0]

def main(m, data):
    if not is_elem(m, 1, 10 ** 6):
        return ["Введено некорректное значение m"]

    stack = Stack(m)
    deleted_elements = []

    for command in data:
        if command[0] == "+":
            elem = int(command.split()[1])
            if not is_elem(elem, -10 ** 9, 10 ** 9):
                return ["Введено некорректное значение элемента стека"]
            result = stack.enqueue(elem)
            if result:
                deleted_elements.append(result)
                return deleted_elements
        elif command[0] == "-":
            result = str(stack.dequeue())
            deleted_elements.append(result)
            if result == "The stack is empty":
                return deleted_elements
    return deleted_elements


if __name__ == "__main__":
    data_file_path = "lab4/task1/txtf/input.txt"
    output_file_path = "lab4/task1/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    m = int(data.pop(0))

    write_data_into_file(output_file_path, main(m, data))

