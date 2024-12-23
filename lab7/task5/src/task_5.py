import argparse
from lab7.utils import read_data_from_file, write_data_into_file



def main(n, a, m, b, l, c):
    dp = [[[0] * (l + 1) for _ in range(m + 1)] for __ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return [str(dp[n][m][l])]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?', const='..', type=str, default='..')
    args = parser.parse_args()

    data_file_path = f"{args.filepath}/txtf/input.txt"
    output_file_path = f"{args.filepath}/txtf/output.txt"

    data = read_data_from_file(data_file_path)
    n = int(data.pop(0))
    a = list(map(int, data.pop(0).split()))
    m = int(data.pop(0))
    b = list(map(int, data.pop(0).split()))
    l = int(data.pop(0))
    c = list(map(int, data.pop(0).split()))

    write_data_into_file(output_file_path, main(n, a, m, b, l, c))
