# The Problem - Day 16
> Topic: Hashing (Python Dictionaries)\
> Level: Beginner+\
> Source: Custom (GPT)\
> Date: 2026-04-12


You are given a list of numbers. Your task is to find all numbers that appear more than once in the list and print them.

## Example:

**Input**:
```py
numbers = [1, 3, 2, 3, 5, 1, 4, 2, 2]
```
**Output**:
```bash
[1, 3, 2]
```


## What you need to think about
You already know how to build a frequency map using a dictionary. You did it with strings. Now apply the same thinking to a list of numbers.

Ask yourself this:
"Once I have the frequency of every number, how do I collect only those whose count is greater than one, without printing the same number twice?"

That last part is the real challenge of this problem.

---

# My Approach
First, I'll create a map of all key as elements of list, and their frequirency as their repetation. Then implement the same logic as [Day 15](../day_15-Str%20+%20Hashing/problem15.md), just i have to reverse it. Now i have to only exclude keys with single keys.

I will cheak frequency map `if value > 1` means key is repeating. So once i found key is repeating i will add it to new list.


## Logic - 1
```py
numbers = [1, 3, 2, 3, 5, 1, 4, 2, 2]
my_dict = {} # Empty dict
new_lst = [] # Empty list

# To create map
for i in numbers:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

# To find numbers
for key, val in my_dict.items():
    if val > 1:
        new_lst.append(key)

print(new_lst) # Result
```

**Output**:
```bash
[1, 3, 2]
```
---