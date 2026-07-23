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

    # check the bracket maching
    def match(self, item):
        char = list(item)

        for i in char:
            if (i == '(') or (i == '[') or (i == '{'):
                self.push(i)

            if i == ')':
                if self.isEmpty() == True:
                    return False
                elif self.peek() == '(':
                    self.pop_stack()
                else:
                    return False
                
            elif i == ']':
                if self.isEmpty() == True:
                    return False
                elif self.peek() == '[':
                    self.pop_stack()
                else:
                    return False
                
            elif i == '}':
                if self.isEmpty() == True:
                    return False
                elif self.peek() == '{':
                    self.pop_stack()
                else:
                    return False
                
        return True if len(self.stack) == 0 else False

o = Stack()

text1 = "{[()]}"
text2 = "{[(])}" 
text3 = "{[}"
print(f"Case 1: {o.match(text1)}")
print(f"Case 2: {o.match(text2)}")
print(f"Case 3: {o.match(text3)}")