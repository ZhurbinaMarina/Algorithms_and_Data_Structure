import unittest
from lab6.task6.src.task_6 import main
from lab6.utils import measurement_of_time


max_time = 2


class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [[8, [1, 2, 3, 4, 5, 6, 7, 8], ["Yes", "Yes", "Yes", "No", "Yes", "No", "No", "Yes"]]]

        for test in tests:
            result = test.pop()
            self.run_test(test, result)

    def run_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')


if __name__ == "__main__":
    unittest.main()
