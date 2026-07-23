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
```pyDay 
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
---
# Problem 2 - Day 31

> Topic: Stack\
> Name: Valid Parentheses\
> Level: Easy\
> Source: Claude\
> Date: 2026-07-22\
> Code file: [Click Here](problem2_solution.py)

### Code description
> Technique: Stack\
> Time complexity: O(n)\
> Space complexity: O(n)\

## The Problem
You are given a string containing only these characters: `(, ), {, }, [, ]`.

Your task is to check whether the string is valid or not and print True or False.

A string is valid if:

1. Every opening bracket has a corresponding closing bracket.
2. Brackets are closed in the correct order.
Key Words Explained

Valid order means if you open a bracket, the very next closing bracket must close that specific opening bracket, not some other one.

### Example 1 - Valid Case:

**Input**:
```py
text = "{[()]}"
```
**Output**:
```bash
True
```
### Example 2 - Invalid Case:

**Input**:
```py
text = "{[(])}"
```
**Output**:
```bash
False
```
> Because ] tries to close ( which is wrong.

### Example 3 - Where beginners go wrong:

**Input**:
```py
text = "{[}"
```
**Output**:
```bash
False
```
> Because [ was never closed properly.

What you need to think about

You have a Stack class already built. Think about what you push and when.

**Ask yourself this**: "When I see an opening bracket I push it. When I see a closing bracket, what do I check against and how does the stack help me verify the correct order?"

# My approach

I will use the base principle of $stack$, **LIFO**.
1. I'll create 4 key operations of Stack in a class.
2. Then I'll convert a string into a list of string: `list(str)`
3. Using for loop, i'll iterate on that list:
    - If `i == opening bracket`, then push it to stack,
    - If `i == clsoing bracket`, then check peek of the stack. If it is closing bracket of the same `i`. Pop the peek
    - If $stack$ left empty in end, `return True`

## Code
```py
class Stack:
    # 4 key oeration method
    # match bracket method
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
                
        if self.isEmpty() == True:    
            return True
```
---

# Problem 3 - Day 32

> Topic: Stack\
> Name: Reverse a String using Stack\
> Level: Easy\
> Source: Claude\
> Date: 2026-07-23\
> Code file: [Click Here](problem3_solution.py)

### Code description
> Technique: Stack\
> Time complexity: O(n)\
> Space complexity: O(n)

## The Problem
You are given a string. Your task is to **reverse it using a Stack**. You cannot use slicing, built in reverse functions, or any other technique. Only stack operations.

### Example 1 - Valid Case:

**Input**:
```py
text = "hello"
```
**Output**:
```bash
"olleh"
```
### Example 2 - Where beginners go wrong:

**Input**:
```py
text = "madam"
```
**Output**:
```bash
"madam"
```
This is a palindrome so input and output look the same. Do not let that confuse you. Your logic should still push and pop correctly.

# My approach
Stack's **LIFO** operation naturally makes a string reverse.

1. I'll convert a string into a list of character
2. The last element will be the first who get out, so I willl add that element in new string
3. After completing stact return the new string.

## Code
```py
class Stack:
    # Core operations
    
    # reverse the string using stack 
    def reverse_str(self, string:str) -> str:
        new_str = ""

        for i in string:
            self.push(i)

        while self.isEmpty() != True:
            new_str += self.pop_stack()

        return new_str
```