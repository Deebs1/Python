class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        if self.root is None:
            return True
        return False

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.root
        self.root = new_node
        print("Data pushed to stack: ", data)

    def pop(self):
        if (self.isEmpty()):
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Top element is: ", stack.peek())

print("popped element from stack is: ", stack.pop())
print("popped element from stack is: ", stack.pop())
print("popped element from stack is: ", stack.pop())
print("popped element from stack is: ", stack.pop())
print("popped element from stack is: ", stack.pop())