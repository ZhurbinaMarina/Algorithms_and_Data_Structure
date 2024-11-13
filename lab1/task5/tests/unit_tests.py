import unittest
from lab1.task5.src.task_5 import main
from lab1.utils import measurement_of_time, generate_list

max_arr_size = 10 ** 3
mn_elem = -10 ** 9
mx_elem = 10 ** 9
max_time = 2


class TestCase(unittest.TestCase):

    def test_task(self):
        tests = [[4, [6, 1, 3, 1], ["1 1 3 6"]],
                 [5, [4, 2, 3, 8, 5], ["2 3 4 5 8"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)

    def test_random(self):
        s = generate_list(max_arr_size, mn_elem, mx_elem)
        self.check_test((max_arr_size, s), [' '.join([str(x) for x in sorted(s)])])

    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")
