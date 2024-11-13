import unittest
from lab2.task1.src.task_1 import main
from lab2.utils import measurement_of_time, generate_list

max_arr_size = 2 * 10 ** 4
mn_elem = -10 ** 9
mx_elem = 10 ** 9
max_time = 2


class TestCase(unittest.TestCase):

    def test_task(self):
        tests = [[6, [1, 5, 2, 4, 3, 2], ["1 2 2 3 4 5"]],
                 [8, [4, 6, 1, 5, 3, 5, 1, 9], ["1 1 3 4 5 5 6 9"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)

    def test_random(self):
        s = generate_list(max_arr_size, mn_elem, mx_elem)
        self.check_test((max_arr_size, s), [' '.join([str(x) for x in sorted(s)])])

    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")
