import unittest
from lab4.task8.src.task_8 import main
from lab4.utils import measurement_of_time

max_cnt_command = 10 ** 6
max_time = 2


class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [[7, ["8", "9", "+", "1", "7", "-", "*"], ["-102"]],
                 [7, ["12", "15", "3", "+", "21", "*", "+"], ["390"]],
                 [5, ["120", "2", "+", "10", "*"], ["1220"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)


    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")
