from lab4.task13.src.task_13_4 import DoublyLinkedList


class Stack:
    def __init__(self):
        self.doubly_linked_list = DoublyLinkedList()

    def is_empty(self):
        return self.doubly_linked_list.head is None

    def push(self, data):
        self.doubly_linked_list.prepend(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")

        popped_value = self.doubly_linked_list.head.key
        self.doubly_linked_list.delete_first()
        return popped_value

    def display(self):
        self.doubly_linked_list.display()


def main():
    stack = Stack()

    stack.push(5)
    stack.push(10)
    stack.push(15)

    print("Стек после добавления элементов:")
    stack.display()  #  15 10 5

    print("Удаленный элемент:", stack.pop())  # 15
    print("Стек после удаления элемента:")
    stack.display()

    print("Стек пуст?", stack.is_empty())

    stack.pop()
    stack.pop()
    print("Стек пуст?", stack.is_empty())


if __name__ == "__main__":
    main()
