import re
import argparse
from lab7.utils import read_data_from_file, write_data_into_file


def main(pattern_s, s):
    pattern_s = pattern_s.replace('?', '.').replace('*', '.*')
    pattern = re.compile(f'^{pattern_s}$')
    return ["YES"] if pattern.match(s) else ["NO"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?', const='..', type=str, default='..')
    args = parser.parse_args()

    data_file_path = f"{args.filepath}/txtf/input.txt"
    output_file_path = f"{args.filepath}/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    pattern = data.pop(0).strip()
    s = data.pop(0).strip()

    write_data_into_file(output_file_path, main(pattern, s))
