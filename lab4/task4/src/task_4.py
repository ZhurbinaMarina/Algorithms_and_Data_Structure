from lab4.utils import read_data_from_file, write_data_into_file, is_len_line, is_elem
from lab4.task1.src.task_1 import Stack


def bracket_sequence(s):
    stack = Stack(10 ** 4)

    for i in range(len(s)):
        if s[i] == '(':
            stack.enqueue(('(', i))
        elif s[i] == '[':
            stack.enqueue(('[', i))
        elif s[i] == '{':
            stack.enqueue(('{', i))
        elif s[i] == ')':
            if stack.stack_empty():
                return str(i + 1)
            if not stack.last_elem()[0] == '(':
                return str(i + 1)
            stack.dequeue()
        elif s[i] == ']':
            if stack.stack_empty():
                return str(i + 1)
            if not stack.last_elem()[0] == '[':
                return str(i + 1)
            stack.dequeue()
        elif s[i] == '}':
            if stack.stack_empty():
                return str(i + 1)
            if not stack.last_elem()[0] == '{':
                return str(i + 1)
            stack.dequeue()

    if not stack.stack_empty():
        return str(stack.first_elem()[1] + 1)
    return "Success"


def main(data):
    result = []

    for line in data:
        if not is_len_line(line, 1, 10 ** 5):
            return ["Введена строка некорректной длины"]
        result.append(bracket_sequence(line))
    return result


if __name__ == "__main__":
    data_file_path = "../txtf/input.txt"
    output_file_path = "../txtf/output.txt"

    data = read_data_from_file(data_file_path)

    write_data_into_file(output_file_path, main(data))
