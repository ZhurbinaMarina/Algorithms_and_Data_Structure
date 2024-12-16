import unittest
from lab6.task5.src.task_5 import main
from lab6.utils import measurement_of_time

max_size = 10 ** 5
max_time = 3


class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [[['McCain 10', 'McCain 5', 'McCain 1', 'Obama 9', 'Obama 8', ], ['McCain 16', 'Obama 17']],
                 [['ivanov 100', 'ivanov 500', 'ivanov 300', 'petr 70', 'tourist 2', 'tourist 1'],
                  ['ivanov 900', 'petr 70', 'tourist 3']]]

        for test in tests:
            result = test.pop()
            self.run_test(test, result)

    def run_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')


if __name__ == "__main__":
    unittest.main()
