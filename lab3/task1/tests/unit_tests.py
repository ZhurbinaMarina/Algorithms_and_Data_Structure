import unittest
from lab3.task1.src.task_1_3 import main
from lab3.utils import measurement_of_time, generate_list

max_arr_size = 10 ** 4
mn_elem = -10 ** 9
mx_elem = 10 ** 9
max_time = 2


class TestCase(unittest.TestCase):

    def test_task(self):
        tests = [[5, [2, 3, 9, 2, 2], ["2 2 2 3 9"]],
                 [8, [3, 4, 2, 5, 2, 9, 2, 1], ["1 2 2 2 3 4 5 9"]]]

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
