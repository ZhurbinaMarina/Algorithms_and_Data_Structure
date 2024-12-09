import unittest
from lab5.task4.src.task_4 import main
from lab5.utils import measurement_of_time

max_size = 10 ** 5
max_time = 3


class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [[5, [5, 4, 3, 2, 1], ["3", "1 4", "0 1", "1 3"]],
                 [5, [1, 2, 3, 4, 5], ["0"]],
                 [5, [4, 10, 3, 5, 1], ["2", "1 4", "0 1"]]]

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
