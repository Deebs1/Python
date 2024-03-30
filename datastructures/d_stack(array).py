class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.arr = [None] * max_size
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def is_Full(self):
        return self.top == self.max_size - 1

    def push(self, data):
        if self.is_Full():
            print("Stack Overflow")
            return
        self.top += 1
        self.arr[self.top] = data

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return
        data = self.arr[self.top]
        self.top -= 1
        return data

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        return self.arr[self.top]

    def printstack(self):
        for i in range(self.top + 1):
            print(self.arr[i], end=" ")


stack = Stack(5)
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack: ", stack.arr[:stack.top+1])
print("Top element: ", stack.peek())
popped_element = stack.pop()
print("Popped element: ", popped_element)
print("Stack: ", stack.arr[:stack.top+1])
# from sys import maxsize
# def createStack():
#     stack = []
#     return stack
#
# def isEmpty(stack):
#     return len(stack) == 0
#
# def push(stack, data):
#     stack.append(data)
#     print(data + " pushed to stack")
#
# def pop(stack):
#     if len(stack==0):
#         return str(-maxsize -1)
#     return stack.pop()
#
# def peek(stack):
#     if len(stack) == 0:
#         return str(-maxsize -1)
#     return stack[len(stack)-1]
#
# stack = createStack()
# push(stack, str(10))
# push(stack, str(20))
# push(stack, str(30))
# print(pop(stack)+ " popped from stack")
