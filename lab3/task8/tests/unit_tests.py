import unittest
from lab3.task8.src.task_8 import main
from lab3.utils import measurement_of_time, generate_random_int

max_arr_size = 10 ** 5
mn_elem = -10 ** 9
mx_elem = 10 ** 9
max_time = 10


class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [[3, 2, [[3, 3], [5, -1], [-2, 4]], ["[3,3],[-2,4]"]],
                 [2, 1, [[1, 3], [-2, 2]], ["[-2,2]"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)


    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")
