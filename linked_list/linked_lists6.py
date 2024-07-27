class Node():
    def __init__(self,data) -> None:
        self.data = data 
        self.next = None

class linkeed_list():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def print_linked_list(self):
        current_node = self.head 
        while current_node is not None:
            print(current_node.data,end=" --> ")
            current_node = current_node.next
        print("None")

ll = linkeed_list()

node1 = Node('A')
node2 = Node('B')
node3 = Node('C')

ll.head = node1
ll.head.next = node2
ll.head.next.next = node3
ll.tail = node3

ll.print_linked_list()
