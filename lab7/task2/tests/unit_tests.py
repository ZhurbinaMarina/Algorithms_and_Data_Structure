import unittest
from lab7.task2.src.task_2 import main
from lab7.utils import measurement_of_time

max_time = 1

class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [[1, ['0', '1']],
                 [5, ['3', '1 2 4 5']],
                 [96234, ['14', '1 2 6 7 21 22 66 198 594 1782 5346 16038 16039 32078 96234']]]

        for test in tests:
            result = test.pop()
            self.run_test(test, result)

    def run_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')


if __name__ == "__main__":
    unittest.main()
