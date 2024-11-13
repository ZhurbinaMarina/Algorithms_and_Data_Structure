import unittest
from lab3.task7.src.task_7 import main
from lab3.utils import measurement_of_time

max_time = 2


class TestCase(unittest.TestCase):

    def test_task(self):
        tests = [[3, 3, 1, ['bab', 'bba', 'baa'], ["2 3 1"]],
                 [3, 3, 2, ['bab', 'bba', 'baa'], ["3 2 1"]],
                 [3, 3, 3, ['bab', 'bba', 'baa'], ["2 3 1"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)

    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")
