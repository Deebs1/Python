class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertatBegin(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # iterative(O(N)) SC-O(1)
    def searchll(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return "element found"
            else:
                current_node = current_node.next
        return "element not found"


llist = LinkedList()
llist.insertatBegin(10)
llist.insertatBegin(20)
llist.insertatBegin(30)
llist.insertatBegin(40)
llist.insertatBegin(50)

element = int(input())
print(llist.searchll(element))

