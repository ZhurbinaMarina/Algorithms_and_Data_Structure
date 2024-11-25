import unittest
from lab4.task1.src.task_1 import main
from lab4.utils import measurement_of_time

max_cnt_command = 10 ** 6
mn_elem = -10 ** 9
mx_elem = 10 ** 9
max_time = 2


class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [[6, ["+ 1", "+ 10", "-", "+ 2", "+ 1234", "-"], ["10", "1234"]],
                 [6, ["+ 1", "+ 10", "-", "+ 2", "+ 1234", "-", "-", "-", "-"], ["10", "1234", "2", "1", "The stack is empty"]],
                 [6, ["+ 5", "+ 10", "-", "-", "-", "-"], ["10", "5", "The stack is empty"]],
                 [3, ["+ 5", "+ 10", "+ 2", "+ 1"], ["The stack is overcrowded"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)


    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")
