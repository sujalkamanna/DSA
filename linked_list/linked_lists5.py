class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list():
    def __init__(self):
        self.head = None
        self.tail = None

    def print_linked_list(self):
        current_node = self.head
        while current_node is not None:
                print(current_node.data,end = "-->")
                current_node = current_node.next
        print("None")                               

ll = linked_list()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

ll.head = node1
ll.head.next = node2
ll.head.next.next = node3
ll.tail = node3

print(ll.head.data)
print(ll.head.next.data)
print(ll.head.next.next.data)
print(ll.tail.data)

ll.print_linked_list()