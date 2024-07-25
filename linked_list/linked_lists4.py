class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Singly_Linked_list():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end='-->')
            current = current.next
        print()


sll = Singly_Linked_list()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

sll.head = node1
sll.head.next = node2
sll.head.next.next = node3
sll.head.next.next.next = node4
sll.tail = node4

# print(sll.head)

print(sll.head.data)
print(sll.head.next.data)
print(sll.head.next.next.data)
print(sll.tail.data)

sll.print_list()
