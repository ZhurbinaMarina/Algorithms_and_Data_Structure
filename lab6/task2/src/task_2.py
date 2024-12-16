import argparse
from lab6.utils import read_data_from_file, is_elem, write_data_into_file


class PhoneBook:
    def __init__(self):
        self.numbers = {}

    def add(self, number, name):
        self.numbers[number] = name

    def delete(self, number):
        if number in self.numbers:
            del self.numbers[number]

    def find(self, number):
        return self.numbers.get(number, 'not found')


def main(n, a):
    if not is_elem(n, 1, 10 ** 5):
        return ["Введено некорректное значение n"]
    phoneBook = PhoneBook()
    answer = []
    for elem in a:
        data = elem.split()

        if data[0] == 'add':
            phoneBook.add(data[1], data[2])
        elif data[0] == 'find':
            answer.append(phoneBook.find(data[1]))
        else:
            phoneBook.delete(data[1])

    return answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?', const='..', type=str, default='..')
    args = parser.parse_args()

    data_file_path = f"{args.filepath}/txtf/input.txt"
    output_file_path = f"{args.filepath}/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n = int(data.pop(0))
    data = [elem.strip() for elem in data]

    write_data_into_file(output_file_path, main(n, data))
