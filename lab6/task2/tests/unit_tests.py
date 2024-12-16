import unittest
from lab6.task2.src.task_2 import PhoneBook

max_size = 10 ** 5
max_time = 3


class TestCase(unittest.TestCase):
    def setUp(self):
        self.phoneBook = PhoneBook()

    def test_add(self):
        self.assertEqual(self.phoneBook.find('123'), 'not found')
        self.phoneBook.add('123', 'Mom')
        self.assertEqual(self.phoneBook.find('123'), 'Mom')
        self.phoneBook.add('123', 'Daddy')
        self.assertEqual(self.phoneBook.find('123'), 'Daddy')

    def test_find(self):
        self.assertEqual(self.phoneBook.find('666'), 'not found')
        self.phoneBook.add('666', 'Mom')
        self.assertEqual(self.phoneBook.find('666'), 'Mom')

    def test_delete(self):
        self.phoneBook.add('345', 'Mom')
        self.assertEqual(self.phoneBook.find('345'), 'Mom')
        self.phoneBook.delete('345')
        self.assertEqual(self.phoneBook.find('345'), 'not found')


if __name__ == "__main__":
    unittest.main()
