class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Singly_Linked_list():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end='-->')
            current = current.next
        print()


sll = Singly_Linked_list()

data_list = [1, 2, 3, 4, 5]
for data in data_list:
    sll.append(data)
sll.print_list()
