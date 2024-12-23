import unittest
from lab7.task5.src.task_5 import main
from lab7.utils import measurement_of_time

max_size = 10 ** 5
max_time = 3


class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [[3, [1, 2, 3], 3, [2, 1, 3], 3, [1, 3, 5], ['2']],
                 [5, [8, 3, 2, 1, 7], 7, [8, 2, 1, 3, 8, 10, 7], 6, [6, 8, 3, 1, 4, 7], ['3']]]

        for test in tests:
            result = test.pop()
            self.run_test(test, result)

    def run_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')


if __name__ == "__main__":
    unittest.main()
