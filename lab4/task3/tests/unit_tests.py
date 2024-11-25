import unittest
from lab4.task3.src.task_3 import main
from lab4.utils import measurement_of_time

max_cnt = 500
mn_len = 1
mx_elem = 10 ** 4
max_time = 2


class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [[5, ["()()", "([])", "([)]", "((]]", ")("], ["YES", "YES", "NO", "NO", "NO"]],
                 [6, ["()()", "([])", "([)]", "((]]", ")(", "((([])))"], ["YES", "YES", "NO", "NO", "NO", "YES"]],
                 [6, ["()()", "([])", "([)]", "((]]", ")(", "((([))))"], ["YES", "YES", "NO", "NO", "NO", "NO"]]]

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
