import unittest
from lab3.task3.src.task_3 import main
from lab3.utils import measurement_of_time

max_time = 2


class TestCase(unittest.TestCase):

    def test_task(self):
        tests = [[3, 2, [2, 1, 3], ["НЕТ"]],
                 [5, 3, [1, 5, 3, 4, 1], ["ДА"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)

    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")
