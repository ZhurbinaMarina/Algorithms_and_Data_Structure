import unittest
from lab2.task3.src.task_3 import main
from lab2.utils import measurement_of_time, generate_list

max_arr_size = 10 ** 5
mn_elem = -10 ** 9
mx_elem = 10 ** 9
max_time = 2


class TestCase(unittest.TestCase):

    def test_task(self):
        tests = [[10, [1, 8, 2, 1, 4, 7, 3, 2, 3, 6], ["17"]],
                 [8, [4, 6, 1, 5, 3, 5, 1, 9], ["12"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)


    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")
