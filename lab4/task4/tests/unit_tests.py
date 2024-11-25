import unittest
from lab4.task4.src.task_4 import main
from lab4.utils import measurement_of_time

mn_len = 1
mx_elem = 10 ** 5
max_time = 5


class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [[["()()", "([])", "([)]", "((]]", ")("], ["Success", "Success", "3", "3", "1"]],
                 [["()()", "([])", "([)]", "((]]", ")(", "((([])))"], ["Success", "Success", "3", "3", "1", "Success"]],
                 [["()[]()", "([{}])", "{[)]", "((]]", "}{", "(({[])})"], ["Success", "Success", "3", "3", "1", "6"]],
                 [["[]", "{}[]", "[()]", "(())", "{", "{[}", "foo(bar);", "foo(bar[i);"],
                  ["Success", "Success", "Success", "Success", "1", "3", "Success", "10"]]]

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
