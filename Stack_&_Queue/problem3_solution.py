class Stack:
    def __init__(self):
            self.stack = []
    
    # IsEmpty method
    def isEmpty(self):
            return len(self.stack) == 0

    # Push method
    def push(self, item):
        self.stack.append(item)

    # pop method
    def pop_stack(self):
        if self.isEmpty() == True:
            return False
        else:
            return self.stack.pop()
    
    # peek/top method
    def peek(self):
        if self.isEmpty() == True:
            return False
        else:
            return self.stack[-1]

    # reverse the string using stack 
    def reverse_str(self, string:str) -> str:
        new_str = ""

        for i in string:
            self.push(i)

        while self.isEmpty() != True:
            new_str += self.pop_stack()

        return new_str
             

print(Stack().reverse_str("hello"))
print(Stack().reverse_str("a"))
print(Stack().reverse_str("madam"))