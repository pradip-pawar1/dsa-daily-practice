# The Problem - Day 23

> Topic: Arrays + Hashing\
> Name: First Duplicate Number\
> Level: Medium\
> Source: Claude\
> Date: 2026-04-22


## The Problem
You are given a list of numbers. Your task is to **find the first number that appears more than once in the list** and print it. _If no duplicate exists_, __print -1__.

First duplicate means the number whose **second occurrence appears earliest in the list**.


First duplicate does not mean the smallest duplicate. It means the duplicate you encounter first as you walk through the list from left to right.

### Example 1 - Valid Case:
**Input**:
```py
numbers = [2, 3, 4, 2, 5, 3]
```
**Output**:
```bash
2
```
Because 2 appears again at index 3, and 3 appears again at index 5. Since 2 repeats first, answer is 2.

### Example 2 - No Duplicate Case:
**Input**:
```py
numbers = [1, 2, 3, 4, 5]
```
**Output**:
```bash
-1
```
Because no number repeats at all.


## What you need to think about
You are walking through the list one element at a time. **Ask yourself this**:

"How do I know at any point during my walk whether I have already seen this number before?"
That question contains the entire solution.


# My approach
First i will store all values in a `dict` as `seen = {}` with their frequency as repetation. Then i will use a loop and for each number `n` i will check, if this value is repeted more that once or not?

If **YES**, then this is a result and breake the loop. If **NO** the result is `-1`.

## Logic - 1
```py
numbers = [2, 3, 4, 2, 5, 3]
seen = {} # map

# create map with frequency
for i in numbers:
    if i not in seen:
        seen[i] = 1
    else:
        seen[i] += 1

# check first repeting element
n_val = 0
n_key = 0

for key, val in seen.items():
    if val > 1:
        n_key = key
        n_val = val
        break

    else:
        n_key = -1

print(n_key)
```

**Output**:
```bash
2
```
---

## Improvement
You are building the full frequency map first, then looping through the dictionary to find the first key with frequency greater than one. But dictionary insertion order is based on first appearance, not on which number repeated first.

**Example**:
```py
numbers = [2, 3, 4, 3, 2]
```

Here `3` repeats first at index `3`, and `2` repeats second at index `4`. So the correct answer is `3`. But your dictionary order will be `2, 3, 4` based on first appearance. When you loop through it, you will find `2` first and print `2`, which is wrong.

Your two loop approach cannot solve this problem correctly. You need a single loop that detects the duplicate the moment the second occurrence is seen.

## Logic - 2
I don't have to use two loops, insted i will use a single loop and check if the number `i` i where seen before then result is `i`. Else result is `-1`.

```py
numbers = [2, 3, 4, 3, 2]
seen = {} # map
result = -1 # result

# Condition checking
for i in numbers:
    if i in seen:
        result = i
        break

    seen[i] = True

print(result)
```

**Output**:
```bash
3
```