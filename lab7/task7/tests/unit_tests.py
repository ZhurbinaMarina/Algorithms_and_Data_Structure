import unittest
from lab7.task7.src.task_7 import main
from lab7.utils import measurement_of_time

max_size = 10 ** 5
max_time = 3


class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [['k?t*n', 'kitten', ['YES']],
                 ['k?t?n', 'kitten', ['NO']]]

        for test in tests:
            result = test.pop()
            self.run_test(test, result)

    def run_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')


if __name__ == "__main__":
    unittest.main()
