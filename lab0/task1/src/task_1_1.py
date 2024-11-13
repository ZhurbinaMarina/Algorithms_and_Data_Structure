_min = 10 ** (-9)
_max = 10 ** 9
a, b = map(int, input().split())
if (_min <= a <= _max) and (_min <= b <= _max):
    print(a + b)
else:
    print('Введены некоректные данные')
