class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        currentnode = self.head 
        while currentnode is not None:
            print(currentnode.data,end="-->")
            currentnode = currentnode.next
        print("None") 

    def add_at_start(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node