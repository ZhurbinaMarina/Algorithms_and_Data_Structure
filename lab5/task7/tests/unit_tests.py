import unittest
from lab5.task7.src.task_7 import main
from lab5.utils import measurement_of_time, generate_list

max_time = 2
max_arr_size = 10 ** 5
mn_elem = -10 ** 9
mx_elem = 10 ** 9


class TestCase(unittest.TestCase):
    def test_task(self):
        tests = [[5, [2, 3, 8, 1, 7], ["8 7 3 2 1"]],
                 [8, [6, 2, 4, 5, 1, 7, 3, 9], ["9 7 6 5 4 3 2 1"]],
                 [7, [3, 6, 1, 4, 8, 2, 5], ["8 6 5 4 3 2 1"]]]

        for test in tests:
            result = test.pop()
            self.check_test(test, result)

    def test_random(self):
        s = generate_list(max_arr_size, mn_elem, mx_elem)
        self.check_test((max_arr_size, s), [' '.join([str(x) for x in sorted(s, reverse=True)])])

    def check_test(self, args, right_answer):
        result, time = measurement_of_time(main, *args)
        self.assertEqual(result, right_answer, "Wrong answer")
        self.assertLessEqual(time, max_time, 'Time limit exceeded')
        print(f"Время выполнения: {time}")


if __name__ == "__main__":
    unittest.main()
