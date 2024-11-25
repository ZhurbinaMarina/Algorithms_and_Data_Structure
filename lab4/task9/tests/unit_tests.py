import unittest
from lab4.task9.src.task_9 import main
from lab4.utils import measurement_of_time

max_cnt_command = 10 ** 5
max_time = 2


class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [[10, ["+ 1", "+ 2", "* 3", "-", "+ 4", "* 5", "-", "-", "-", "-"], ["1", "3", "2", "5", "4"]],
                 [7, ["+ 1", "+ 2", "-", "+ 3", "+ 4", "-", "-"], ["1", "2", "3"]]]

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
