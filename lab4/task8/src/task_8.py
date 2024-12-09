from lab4.utils import read_data_from_file, write_data_into_file, is_elem
from lab4.task1.src.task_1 import Stack

def main(n, data):
    if not is_elem(n, 1, 10 ** 6):
        return ["Введено некорректное значение n"]

    result = []
    stack = Stack(n)

    for elem in data:
        if elem == "+":
            value_1 = stack.dequeue()
            value_2 = stack.dequeue()
            res = value_1 + value_2
            stack.enqueue(res)
        elif elem == "-":
            value_1 = stack.dequeue()
            value_2 = stack.dequeue()
            res = value_2 - value_1
            stack.enqueue(res)
        elif elem == "*":
            value_1 = stack.dequeue()
            value_2 = stack.dequeue()
            res = value_1 * value_2
            stack.enqueue(res)
        else:
            res = int(elem)
            stack.enqueue(res)
    return [str(stack.dequeue())]


if __name__ == "__main__":
    data_file_path = "lab4/task8/txtf/input.txt"
    output_file_path = "lab4/task8/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n = int(data.pop(0))
    data = data[0].split()

    write_data_into_file(output_file_path, main(n, data))