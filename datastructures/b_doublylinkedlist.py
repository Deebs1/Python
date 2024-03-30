class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Doublylinkedlist:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insertatEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def insertatIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if index == position:
            self.insertAtBegin(data)
        else:
            while (current_node != None and position + 1 != index):
                position += 1
                current_node = current_node.next
            if current_node != None:

                new_node.prev = current_node
                new_node.next = current_node.next
                if current_node.next:
                    current_node.next.prev = new_node
                current_node.next = new_node



            else:
                print("Index is not valid")

    def insertAfter(self, prev_node, data):
        if prev_node is None:
            print("This node doesn't exist")
            return
        else:
            new_node = Node(data)
            new_node.prev = prev_node
            new_node.next = prev_node.next
            if (prev_node.next):
                prev_node.next.prev = new_node
            prev_node.next = new_node

    def insertBefore(self, next_node, data):
        new_node = Node(data)
        if next_node is None:
            print("This node doesn't exist")
            return
        else:
            new_node.prev = next_node.prev
            new_node.next = next_node
            if next_node.prev:
                next_node.prev.next = new_node
            else:
                self.head = new_node
            next_node.prev = new_node

    def insert_at_pointertonode(self, pointer, data):
        new_node = Node(data)
        if self.head is None or pointer is None:
            return
        if self.head == pointer:
            self.insertAtBegin(data)
        else:
            if pointer.next:
                new_node.prev = pointer.prev
                new_node.next = pointer
                pointer.prev.next = new_node
                pointer.prev = new_node
            else:
                new_node.next = pointer
                new_node.prev = pointer.prev
                pointer.prev.next = new_node
                pointer.prev = new_node
                pointer.next = None

    def remove_first_node(self):
        current_node = self.head
        if self.head is None:
            return
        else:
            self.head = current_node.next
            self.head.prev = None

    def remove_last_node(self):
        current_node = self.head
        if self.head is None:
            return
        while (current_node.next.next):
            current_node = current_node.next
        current_node.next = None

    def remove_at_index(self, index):
        if self.head is None:
            print("DoublyLinkedlist is empty")
        current_node = self.head
        position = 0
        if index == position:
            self.head = current_node.next
            self.head.prev = None
            return
        else:
            while current_node != None and position + 1 != index:
                position += 1
                current_node = current_node.next
            if current_node != None:
                if current_node.next.next:
                    current_node.next.next.prev = current_node
                current_node.next = current_node.next.next
            else:
                print("Invalid index")

    def remove_after_node(self, pointer):
        if self.head is  None or pointer is None:
            return
        if pointer.next is None:
            print("Invalid index")
        if pointer.next and pointer.next.next:
            pointer.next.next.prev = pointer
            pointer.next = pointer.next.next
        else:
            pointer.next = None

    def remove_before_node(self, pointer):
        if self.head is None or pointer is None:
            return
        if pointer == self.head:
            print("cant remove")
            return
        if pointer.prev == self.head:
            self.head = pointer
            pointer.prev = None
        else:

            pointer.prev.prev.next = pointer
            pointer = pointer.prev.prev

    def remove_at_pointertonode(self, pointer):
        if self.head is None or pointer is None:
            return
        if pointer == self.head:
            self.head = pointer.next
            pointer.next.prev = None
            return
        if pointer.next:
            pointer.prev.next = pointer.next
            pointer.next.prev = pointer.prev
        else:
            pointer.prev.next = None

    def get_all_nodes(self):
        nodes = []
        ptr = self.head
        while ptr:
            nodes.append(ptr)
            ptr = ptr.next
        return nodes

    def printll(self):
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while (current_node):
            print(current_node.data, end=" ")
            current_node = current_node.next

#     updatenode, remove given data, size, getNth node, searching, reverse
    def update_node(self, val, index):
        if self.head is None:
            print("Linkedlist is empty")
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
            return
        while(current_node!=None and position!=index):
            position+=1
            current_node = current_node.next

        if (current_node != None):
            current_node.data = val
        else:
            print("invalid index")


dll = Doublylinkedlist()
# dll.insertAtBegin(10)
# dll.insertAtBegin(20)
# dll.insertAtBegin(30)
# dll.insertAtBegin(40)
dll.insertatEnd(10)
dll.insertatEnd(20)
dll.insertatEnd(30)
dll.insertatEnd(40)
# dll.update_node(50,6)
# dll.insertatIndex(200, 2)
# dll.insertBefore(dll.head.next.next.next.next, 100)
# dll.remove_last_node()
# dll.remove_at_index(3)
# dll.insert_at_pointertonode(dll.head.next.next.next.next, 1000)
# dll.remove_after_node(dll.head.next.next.next.next.next)
# dll.remove_before_node(dll.head.next.next.next.next.next)

dll.remove_at_pointertonode(dll.head.next.next.next.next.next)
dll.printll()

