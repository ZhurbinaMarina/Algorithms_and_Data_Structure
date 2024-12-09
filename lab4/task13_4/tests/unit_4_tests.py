import unittest
from lab4.task13_1.src.task_13_4 import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.doubly_linked_list = DoublyLinkedList()

    def test_append(self):
        self.doubly_linked_list.append(5)
        self.doubly_linked_list.append(10)
        self.assertEqual(self.doubly_linked_list.head.key, 5)
        self.assertEqual(self.doubly_linked_list.head.next.key, 10)

    def test_prepend(self):
        self.doubly_linked_list.append(10)
        self.doubly_linked_list.prepend(5)
        self.assertEqual(self.doubly_linked_list.head.key, 5)
        self.assertEqual(self.doubly_linked_list.head.next.key, 10)

    def test_delete_node(self):
        self.doubly_linked_list.append(5)
        self.doubly_linked_list.append(10)
        self.doubly_linked_list.append(15)
        self.doubly_linked_list.delete_node(10)

        self.assertEqual(self.doubly_linked_list.head.next.key, 15)
        self.assertIsNotNone(self.doubly_linked_list.head.next.prev)

        print()

    def test_delete_first(self):
        self.doubly_linked_list.append(5)
        self.doubly_linked_list.append(10)
        self.doubly_linked_list.delete_first()

        self.assertEqual(self.doubly_linked_list.head.key, 10)

    def test_delete_last(self):
        self.doubly_linked_list.append(5)
        self.doubly_linked_list.append(10)
        self.doubly_linked_list.delete_last()

        self.assertEqual(self.doubly_linked_list.head.key, 5)
        self.assertIsNone(self.doubly_linked_list.head.next)

    def test_insert_before(self):
        self.doubly_linked_list.append(5)
        self.doubly_linked_list.append(15)
        self.doubly_linked_list.insert_before(15, 10)

        self.assertEqual(self.doubly_linked_list.head.next.key, 10)
        self.assertEqual(self.doubly_linked_list.head.next.next.key, 15)

    def test_search_found(self):
        self.doubly_linked_list.append(5)
        found_node = self.doubly_linked_list.search(5)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.key, 5)

    def test_search_not_found(self):
        self.doubly_linked_list.append(5)
        found_node = self.doubly_linked_list.search(10)
        self.assertIsNone(found_node)



if __name__ == "__main__":
    unittest.main()
