# creation of linked list

class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None


class ssl():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

lst = ssl()
node1 = Node(1)
node2 = Node(2)

lst.head = node1
lst.head.next = node2
lst.tail = node2

print(lst.head.value)
print(lst.tail.value)


