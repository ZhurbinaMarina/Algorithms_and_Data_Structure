import time

t_start = time.perf_counter()
f = open('input.txt')
n = int(f.readline())
f.close()
_min = 0
_max = 45
if _min <= n <= _max:
    f_0, f_1 = 0, 1
    for i in range(n - 1):
        f_0, f_1 = f_1, f_0 + f_1
    f_output = open('output.txt', 'w')
    f_output.write(str(f_1))
    f_output.close()
    print("Время работы: %s секунд " % (time.perf_counter() - t_start))
else:
    f_output = open('output.txt', 'w')
    f_output.write('Введены некоректные данные')
    f_output.close()
