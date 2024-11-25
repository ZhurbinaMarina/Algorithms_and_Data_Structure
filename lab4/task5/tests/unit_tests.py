import unittest
from lab4.task5.src.task_5 import main
from lab4.utils import measurement_of_time

max_cnt_command = 400000
mn_elem = 0
mx_elem = 10 ** 5
max_time = 5


class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [[5, ["push 2", "push 1", "max", "pop", "max"], ["2", "2"]],
                 [5, ["push 1", "push 2", "max", "pop", "max"], ["2", "1"]],
                 [3, ["push 1", "push 7", "pop"], []],
                 [8, ["push 10", "push 7", "push 18", "max", "pop", "max", "pop", "max"], ["18", "10", "10"]]]

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
