import unittest
from lab3.task1.src.task_1_3 import main
from lab3.utils import measurement_of_time, generate_list


class TestCase(unittest.TestCase):

    def __init__(self):
        self.max_arr_size = 10 ** 4
        self.mn_elem = -10 ** 9
        self.mx_elem = 10 ** 9
        self.max_time = 2

    def test_task(self):
        tests = [[5, [2, 3, 9, 2, 2], ["2 2 2 3 9"]],
                 [8, [3, 4, 2, 5, 2, 9, 2, 1], ["1 2 2 2 3 4 5 9"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)

    def test_random(self):
        s = generate_list(self.max_arr_size, self.mn_elem, self.mx_elem)
        self.check_test((self.max_arr_size, s), [' '.join([str(x) for x in sorted(s)])])

    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, self.max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")
