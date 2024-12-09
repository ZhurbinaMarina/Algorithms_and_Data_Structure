import unittest
from lab5.task6.src.task_6 import main
from lab5.utils import measurement_of_time

max_cnt_commands = 10 ** 6
max_time = 2


class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [[8, ["A 3", "A 4", "A 2", "X", "D 2 1", "X", "X", "X"], ["2", "1", "3", "*"]],
                 [11, ["A 2", "A 6", "A 1", "A 5", "A 3", "X", "D 2 1", "X", "X", "X", "X"], ["1", "1", "2", "3", "5"]],
                 [7, ["A 5", "A 4", "A 3", "X", "D 1 2", "X", "X"], ["3", "2", "4"]]]

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
