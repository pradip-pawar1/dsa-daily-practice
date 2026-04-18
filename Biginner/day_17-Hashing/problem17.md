# The Problem - Day 17
> Topic: Hashing (Python Dictionaries)\
> Level: Beginner+\
> Source: Custom (GPT)\
> Date: 2026-04-13


You are given a list of numbers. Your task is to **find whether any two numbers in the list add up to a given target sum**.
Print `True` if such a pair exists, `False` if not.

## Example:
**Input**:
```py
numbers = [2, 7, 4, 1, 9]
target = 11
```
**Output**:
```bash
True
```
> Because `2 + 9 = 11`.

## What you need to think about
There is a slow way and a fast way to solve this.

Ask yourself this:

"For every number I look at, **what is the one specific value I need to find elsewhere in the list to complete the pair**, and how can I check that instantly without looping again?"

That question points you toward using a dictionary in a way you have not used it before.

# Logic: Solved by GPT
```py
numbers = [2, 7, 4, 1, 9]
target = 11

seen = {}
result = False

for i in numbers:
    complement = target - i
    
    if complement in seen:
        result = True
        break
    
    seen[i] = True

print(result)
```
