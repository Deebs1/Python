class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.last = None
    def insert_begin(self, data):
        new_node = Node(data)
        if self.last is None:
            self.last = new_node
            self.last.next = self.last
            return
        new_node.next = self.last.next
        self.last.next = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.last is None:
            self.last = new_node
            self.last.next = self.last
            return
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node

    def addAfter(self, data, item):

        if (self.last == None):
            return None

        temp = Node(data)
        p = self.last.next
        while p:
            if (p.data == item):
                temp.next = p.next
                p.next = temp

                if (p == self.last):
                    self.last = temp
                    return self.last
                else:
                    return self.last
            p = p.next
            if (p == self.last.next):
                print(item, "not present in the list")
                break

    def remove_first_node(self):
        if self.last is None:
            return "empty"
        
        self.last.next = self.last.next.next
        self.last = self.last.next.next







    def printcll(self):
        if self.last is None:
            print("List is empty")
            return
        current_node = self.last.next
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
            if current_node == self.last.next:
                break

cllist = CircularLinkedList()
# cllist.insert_begin(10)
# cllist.insert_begin(20)
# cllist.insert_begin(30)
# cllist.insert_begin(40)
cllist.insert_end(10)
cllist.insert_end(20)
cllist.insert_end(30)
cllist.insert_end(40)
# cllist.addAfter(1342, 90)
cllist.remove_first_node()
cllist.printcll()