class Stack:
    def __init__(self):
        self.stack = []

    # view stack 
    def view(self):
        print(self.stack)

    # IsEmpty method
    def isEmpty(self):
            return len(self.stack) == 0

    # Push method
    def push(self, item):
        self.stack.append(item)
        print(f"{item} is added to stack")

    # pop method
    def pop_stack(self):
        if self.isEmpty() == True:
            print("Stack is empty")
        else:
            return self.stack.pop()
    
    # peek/top method
    def peek(self):
        if self.isEmpty() == True:
            print("Stack is empty")
        else:
            print(self.stack[-1])
             
obj = Stack()


