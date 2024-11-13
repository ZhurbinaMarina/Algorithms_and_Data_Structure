import unittest
from lab3.task4.src.task_4 import main
from lab3.utils import measurement_of_time

max_time = 2


class TestCase(unittest.TestCase):

    def test_task(self):
        tests = [[2, 3, [[0, 5], [7, 10]], [1, 6, 11], ["1 0 0"]],
                 [1, 3, [[-10, 10]], [-100, 100, 0], ["0 0 1"]],
                 [3, 2, [[0, 5], [-3, 2], [7, 10]], [1, 6], ["2 0"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)

    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")
