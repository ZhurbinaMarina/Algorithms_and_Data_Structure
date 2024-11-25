class Node:
    """Класс для представления узла двусвязного списка."""

    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete_node(self, key):
        current = self.head

        if not current:
            return

        if current.key == key:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return

        while current and current.key != key:
            current = current.next

        if not current:
            print("Элемент не найден.")
            return

        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

    def delete_first(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return

        last = self.head
        while last.next:
            last = last.next

        last.prev.next = None

    def insert_before(self, key, data):
        current = self.head
        while current and current.key != key:
            current = current.next

        if not current:
            print("Элемент для вставки не найден.")
            return

        new_node = Node(data)
        new_node.prev = current.prev
        new_node.next = current

        if current.prev:
            current.prev.next = new_node
        else:
            self.head = new_node

        current.prev = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.key, end=' ')
            current = current.next
        print()


def main():
    s = DoublyLinkedList()

    s.append(5)
    s.append(10)
    s.append(20)
    s.append(30)

    print("Содержимое списка после добавления элементов:")
    s.display()

    s.prepend(23)
    print("Содержимое списка после добавления элемента в начало:")
    s.display()

    s.delete_node(20)
    print("Содержимое списка после удаления элемента 20:")
    s.display()

    s.delete_first()
    print("Содержимое списка после удаления первого элемента:")
    s.display()

    s.delete_last()
    print("Содержимое списка после удаления последнего элемента:")
    s.display()

    s.insert_before(10, 25)
    print("Содержимое списка после вставки 25 перед 10:")
    s.display()

    found = s.search(10)
    if found is not None:
        print("Элемент 10 найден:", found.key, found)
    if found is not None:
        found = s.search(25)
        print("Элемент 25 найден:", found.key, found)


if __name__ == "__main__":
    main()
