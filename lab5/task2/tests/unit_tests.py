import unittest
from lab5.task2.src.task_2 import main
from lab5.utils import measurement_of_time

max_size = 10 ** 5
max_time = 3


class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [[5, [4, -1, 4, 1, 1], ["3"]],
                 [5, [-1, 0, 4, 0, 3], ["4"]],
                 [11, [1, -1, 0, 1, 3, 0, 2, 6, 3, 6, 2], ["5"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)

    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")


if __name__ == "__main__":
    unittest.main()
