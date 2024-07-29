class Singly_Linked_List():
    def __init__(self):
        self.head = None
        self.tail = None


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


linked_list = Singly_Linked_List()

obj1 = Node(1)
obj2 = Node(2)
obj3 = Node(3)

linked_list.head = obj1
linked_list.head.next = obj2
linked_list.head.next.next = obj3
linked_list.tail = obj3

print(linked_list.head.value)
print(linked_list.tail.value)
