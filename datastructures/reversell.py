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

    def reversell(self):
        prev = None
        curr = self.head

        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def printll(self):
        current_node = self.head
        while (current_node):
            print(current_node.data, end=" ")
            current_node = current_node.next

    # def __str__(self):
    #     linkedListStr = ""
    #     temp = self.head
    #     while temp:
    #         linkedListStr = (linkedListStr +
    #                          str(temp.data) + " ")
    #         temp = temp.next
    #     return linkedListStr




llist = LinkedList()
llist.insertatBegin(10)
llist.insertatBegin(20)
llist.insertatBegin(30)
llist.insertatBegin(40)
llist.insertatBegin(50)
llist.reversell()
llist.printll()
# print(llist)
