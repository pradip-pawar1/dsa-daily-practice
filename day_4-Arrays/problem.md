# The Problem : Day 4
You are given a list of numbers. Your task is to find whether a **given number exists in the list or not**, without using the `in` keyword or any built-in search function.
Print True if found, False if not.

### Example:
**Input:**
```
numbers = [4, 7, 2, 9, 1]
target = 7
```
**Output:**
```
True
```

## What you need to think about
You have a list. You have a target. You need to walk through the list yourself and check each element one by one.
Ask yourself this:
"At what point do I stop searching, and what do I report if I never find it?"

---
# My approach
First i create a variable as `result = False` to store the result. Then I am using simple for loop `for i in list`, where I stores the current iterable element for the list.
Then I'll compare current iterable `i` with target value as `if i == target`. If this condition is true the change the result to `result = True`. And once found the target then break the loop. And print the result.

---
# Attempt 1
```
numbers = [4, 7, 2, 9, 1]
target = 7

result = False

for i in numbers:
    if i == target:
        result = True
        break

print(result)
```
> Logic is to the point and the Method is known as **Linear search**.