_min = 10 ** (-9)
_max = 10 ** 9
f = open('input_4.txt')
a, b = map(int, f.readline().split())
f.close()
if (_min <= a <= _max) and (_min <= b <= _max):
    f_output = open('output_4.txt', 'w')
    f_output.write(str(a + b ** 2))
    f_output.close()
else:
    f_output = open('output_4.txt', 'w')
    f_output.write('Введены некоректные данные')
    f_output.close()
