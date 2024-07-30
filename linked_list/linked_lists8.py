class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist():
    def __init__(self):
        self.head = None
        self.tail = None

    def add_at_beginning(self, new_data):
        node_n = Node(new_data)
        node_n.next = self.head
        self.head = node_n
    # inserting at end

    def inserting_at_end(self, new_data):
        node_n = Node(new_data)
        if self.head is None:
            self.head = node_n
            self.tail = node_n
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node_n
            self.tail = None

    def printlist(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end="-->")
            current_node = current_node.next
        print("None")


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

ll = linkedlist()

ll.head = node1
ll.head.next = node2
ll.head.next.next = node3
ll.tail = node3

ll.add_at_beginning(10)
ll.inserting_at_end(20)
ll.printlist()
