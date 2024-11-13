import unittest
from lab2.task5.src.task_5 import main
from lab2.utils import measurement_of_time, generate_list

max_arr_size = 10 ** 5
mn_elem = 0
mx_elem = 10 ** 9
max_time = 2


class TestCase(unittest.TestCase):

    def test_task(self):
        tests = [[5, [2, 3, 9, 2, 2], ["1"]],
                 [4, [1, 2, 3, 4], ["0"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)

    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")
