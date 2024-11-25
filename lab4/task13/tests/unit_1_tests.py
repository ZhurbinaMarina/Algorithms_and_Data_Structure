import unittest
from lab4.task13.src.task_13_1 import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_is_empty_initially(self):
        self.assertTrue(self.stack.is_empty())

    def test_push_and_is_empty(self):
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_push_multiple_elements(self):
        self.stack.push(5)
        self.stack.push(10)
        self.stack.push(15)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.doubly_linked_list.head.key, 15)

    def test_pop_single_element(self):
        self.stack.push(1)
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 1)
        self.assertTrue(self.stack.is_empty())

    def test_pop_multiple_elements(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 3)
        self.assertFalse(self.stack.is_empty())

        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 2)
        self.assertFalse(self.stack.is_empty())

        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 1)
        self.assertTrue(self.stack.is_empty())

    def test_pop_from_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.pop()



if __name__ == "__main__":
    unittest.main()
