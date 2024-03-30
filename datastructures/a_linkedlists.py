# creating a linkedlist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertatIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if index==position:
            self.head = new_node
        else:
            while (current_node!=None and position+1!=index):
                position+=1
                current_node=current_node.next

            if current_node!=None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index is not valid")

    def insertAtend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    # def insert_before(self, pointer, data):
    # def insert_before(self, index, data):
    # def insert_after(self, pointer, data):
    # def insert_after(self, index, data):




    def updateNode(self, val, index):
        current_node = self.head
        position=0
        if position == index:
            current_node.data = val
        else:
            while(current_node!=None and position!=index):
                position+=1
                current_node = current_node.next
            if(current_node!=None):
                current_node.data = val
            else:
                print("invalid index")

    def remove_first_node(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return

        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next

        current_node.next = None

    def remove_at_index(self, index):
        if self.head == None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.head = self.head.next
        else:
            while(current_node!=0 and position+1!=index):
                position += 1
                current_node = current_node.next

            if current_node!=None:
                current_node.next=current_node.next.next
            else:
                print("invalid index")

    def remove_given_data(self, val):
        current_node = self.head
        if (current_node.data==val):
            self.head = self.head.next
            return

        while current_node is not None and current_node.next.data!=val:
                current_node = current_node.next

        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next



    def sizell(self):
        size = 0
        current_node = self.head
        if self.head == None:
            return size
        while(current_node):
            size+=1
            current_node = current_node.next
        return size

    def getNth(self, index):
        count = 0
        current_node = self.head
        while(current_node):
            if count == index:
                return current_node.data
            count+=1
            current_node = current_node.next
    #     TC-O(N)
    #     SC-O(1)










    #  traversal
    def printll(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next


llist = LinkedList()
# llist.insertAtBegin(10)
# llist.insertAtBegin(20)
# llist.insertAtBegin(30)
# llist.insertatIndex(40,2)
llist.insertAtend(50)
llist.insertAtend(10)
llist.insertAtend(20)
llist.insertAtend(30)
llist.insertAtend(40)
llist.insertatIndex(100, 5)
# llist.insertatIndex(50, 1)
# llist.updateNode(50, 4)
# llist.remove_last_node()
# llist.remove_at_index(1)
# llist.remove_given_data(10)
# print(llist.sizell())
# print(llist.getNth(6))
llist.printll()



