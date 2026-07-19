# Problem 1 - Day 30

> Topic: Stack\
> Name: Build a Stack from Scratch\
> Level: Easy\
> Source: Claude\
> Date: 2026-07-18\
> Code File: [Click Here](problem1_solution.py)

### Code description
> Technique: OOP + Stack Implementation\
> Time complexity: O(1) for all operations\
> Space complexity: O(n)

## The Problem
Build a `Stack class` using a **Python list** with these four operations:
1. `push(item)` adds item to top of stack.
2. `pop()` removes and returns top item. If stack is empty print "**Stack** is empty" and return None.
3. `peek()` returns top item without removing it. If stack is empty print "Stack is empty" and return None.
4. `is_empty()` returns True if stack is empty, False if not.

Example:
```py
pythons = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())     # 3
print(s.pop())      # 3
print(s.pop())      # 2
print(s.is_empty()) # False
print(s.pop())      # 1
print(s.is_empty()) # True
print(s.pop())      # Stack is empty
```

## What you need to think about
This is your **first OOP problem** in this series. A class holds data and operations together.

**Ask yourself this**:
"*Which end of the Python list acts as the top of the stack, and which built in list operations naturally support push and pop from that end?*"

# My approach
The right end of the list will act as the pop, and using simple OOP's principle i will create 5 methods:
1. `IsEmpty()`: Checks weather the stack is empty of not?
2. `view()`: Show the stack
3. `push()`: Pushed the item, in a stack
4. `pop()`: Remove the last/top item form the stack
5. `peek/top()`: Returns the top most element of the stack

## Code
```py
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
```
