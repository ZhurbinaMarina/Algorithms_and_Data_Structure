import unittest
from lab1.task2.src.task_2 import main
from lab1.utils import measurement_of_time, generate_list

max_arr_size = 10 ** 3
mn_elem = -10 ** 9
mx_elem = 10 ** 9
max_time = 2


class TestCase(unittest.TestCase):

    def test_task(self):
        tests = [[3, [6, 1, 3], ["1 1 2", "1 3 6"]],
                 [5, [4, 2, 3, 8, 5], ["1 1 2 4 4", "2 3 4 5 8"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)

    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")
