import unittest
from lab7.task1.src.task_1 import main
from lab7.utils import measurement_of_time


max_time = 1


class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [[2, 3, [1, 3, 4], ['2']],
                 [34, 3, [1, 3, 4], ['9']]]

        for test in tests:
            result = test.pop()
            self.run_test(test, result)

    def run_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')


if __name__ == "__main__":
    unittest.main()
