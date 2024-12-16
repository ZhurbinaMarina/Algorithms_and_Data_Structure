import argparse
from lab6.utils import read_data_from_file, write_data_into_file


def main(a):
    d = {}
    for elem in a:
        k, v = elem.split()
        d[k] = d.get(k, 0) + int(v)
    answer = list(d.items())
    answer.sort(key=lambda x: x[0])

    return [x[0] + ' ' + str(x[1]) for x in answer]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?', const='..', type=str, default='..')
    args = parser.parse_args()

    data_file_path = f"{args.filepath}/txtf/input.txt"
    output_file_path = f"{args.filepath}/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    data = [x.strip() for x in data]

    write_data_into_file(output_file_path, main(data))
