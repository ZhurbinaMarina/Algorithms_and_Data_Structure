from lab4.utils import read_data_from_file, write_data_into_file, is_elem


class StackWithMax:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.stack = [None] * size
        self.max = -1

    def enqueue(self, elem):
        if None not in self.stack:
            return "The stack is overcrowded"
        else:
            self.top += 1
            if self.max == -1:
                self.max = elem
                self.stack[self.top] = self.max - elem
            else:
                self.stack[self.top] = self.max - elem
                if elem > self.max:
                    self.max = elem
            return None

    def dequeue(self):
        if self.stack_empty():
            return "The stack is empty"
        else:
            elem = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1

            if elem < 0:
                result = self.max
                self.max = self.max + elem
            else:
                result = self.max - elem
            return result

    def stack_empty(self):
        if self.top == -1:
            return True
        return False

    def max_elem(self):
        return self.max

    def last_elem(self):
        return self.stack[self.top]

    def first_elem(self):
        return self.stack[0]

def main(n, data):
    if not is_elem(n, 1, 400000):
        return ["Введено некорректное значение n"]

    stack = StackWithMax(n)
    answ = []

    for line in data:
        command = line.split()
        if command[0] == "push":
            elem = int(command[1])
            if not is_elem(elem, 0, 10 ** 5):
                return ["Введено некорректное значение элемента стека"]
            result = stack.enqueue(elem)
            if result:
                answ.append(result)
                return answ
        elif command[0] == "pop":
            result = str(stack.dequeue())
            if result == "The stack is empty":
                answ.append(result)
                return answ
        elif command[0] == "max":
            result = str(stack.max_elem())
            if result == "-1":
                answ.append("The stack is empty")
            else:
                answ.append(result)
    return answ


if __name__ == "__main__":
    data_file_path = "../txtf/input.txt"
    output_file_path = "../txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n = int(data.pop(0))

    write_data_into_file(output_file_path, main(n, data))

