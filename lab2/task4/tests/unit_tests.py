import unittest
from lab2.task4.src.task_4 import main
from lab2.utils import measurement_of_time, generate_list

max_arr_size = 10 ** 4
mn_elem = 1
mx_elem = 10 ** 9
max_time = 2


class TestCase(unittest.TestCase):

    def test_task(self):
        tests = [[5, [1, 5, 8, 12, 13], 5, [8, 1, 23, 1, 11], ["2 0 -1 0 -1"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)

    def test_random(self):
        a = generate_list(max_arr_size, mn_elem, mx_elem)
        b = generate_list(max_arr_size, mn_elem, mx_elem)
        result = []
        for elem in b:
            try:
                idx = a.index(elem)
                result.append(idx)
            except ValueError:
                result.append(-1)

        self.check_test((max_arr_size, a, max_arr_size, b), [' '.join([str(x) for x in sorted(result)])])

    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")
