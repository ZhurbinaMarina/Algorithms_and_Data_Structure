import unittest
from lab2.task2.src.task_2 import main
from lab2.utils import measurement_of_time, generate_list

max_arr_size = 10 ** 5
mn_elem = -10 ** 9
mx_elem = 10 ** 9
max_time = 2


class TestCase(unittest.TestCase):

    def test_task(self):
        tests = [[4, [5, 2, 8, 5], ["1 2 2 5", "3 4 5 8", "1 4 2 8", "2 5 5 8"]],
                 [8, [4, 6, 1, 5, 3, 5, 1, 9],
                  ["1 2 4 6", "3 4 1 5", "1 4 1 6", "5 6 3 5", "7 8 1 9", "5 8 1 9", "1 8 1 9", "1 1 3 4 5 5 6 9"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)

    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")
