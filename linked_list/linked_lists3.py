#insertion in singly linked list

# 1 at the beginning
# 2 after a node in betweeen of a ll
# 3 at the end

class Node():
    def __init__(self,value=None) -> None:
        self.value =value
        self.next = None

class sll():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert_to_ssl(self,value,location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

singly = sll()
singly.insert_to_ssl(1,1)
singly.insert_to_ssl(2,1)
print([node.value for node in sll])

