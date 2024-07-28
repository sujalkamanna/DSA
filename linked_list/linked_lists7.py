class Node():
    def __init__(self,data) -> None:
        self.data = data 
        self.next = None

class linked_list():
    def __init__(self) -> None:
        self.head = None 
        self.tail = None 

    def insert_at_beginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_linked_list(self):
        current_node = self.head 
        while current_node is not None:
            print(current_node.data,end="-->")
            current_node = current_node.next
        print("None")            

node1= Node(1)
node2 = Node(2)        
node3 = Node(3)

ll = linked_list()

ll.head = node1
ll.head.next = node2
ll.head.next.next = node3 
ll.tail = node3

ll.insert_at_beginning(10)

ll.print_linked_list()