import unittest
from lab1.task10.src.task_10 import main
from lab1.utils import measurement_of_time, generate_list

max_time = 1


class TestCase(unittest.TestCase):

    def test_task(self):
        tests = [[3, "AAB", ["ABA"]],
                 [6, "QAZQAZ", ["AQZZQA"]],
                 [6, "ABCDEF", ["A"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)

    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")
