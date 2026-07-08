# The Problem - Day 20
> Topic: Arrays + Hashing\
> Level: Medium\
> Source: GPT\
> Date: 2026-04-19


You are given a list of numbers. Your task is to **find the most frequently occurring number** in the list and print it. If two numbers have the same frequency, print the one that appears first in the list.

## Example:
**Input**:
```py
numbers = [1, 3, 2, 1, 4, 3, 1, 2]
```

**Output**:
```bash
1
```
Because 1 appears 3 times which is the highest frequency.

## What you need to think about
You have done character frequency in strings before. This is the same concept applied to numbers.
Ask yourself this:
"Once I have the frequency of every number, how do I find the one with the highest count while respecting the order of first appearance?"

# My approach
First i will create a dictionary for all elements. If any number `i` repeats again, for that number increase the value by 1 as `i + 1`. Then return thr first element who has the largestvalue.

## Logic - 1
Code has bug.
```py
numbers = [1, 3, 2, 1, 4, 3, 1, 2]
seen = {}

# create map for all numbers
for i in numbers:
    if i not in seen:
        seen[i] = 1
    else:
        seen[i] += 1

# return first number has largets value
largest = 0
for key, val in seen.items():
    if val > largest:
        largest = key
    elif val == largest:
        continue

print(largest)
```

## Improvement from GPT
You are comparing `val` against `largest`, but `largest` is supposed to store the highest frequency seen so far, not the key. Then when you find a higher frequency, you store the `key` into `largest` instead of the `val`.

You are mixing up two things. You need to track both the best `key` and the best `value` separately, exactly like you did in [**Day 18**](../../Biginner/day_18-Hashing/soln18.py).


## Logic - 2
```py
numbers = [1, 3, 2, 1, 4, 3, 1, 2]
seen = {}

# create map for all numbers
for i in numbers:
    if i not in seen:
        seen[i] = 1
    else:
        seen[i] += 1

# return first number has largets value
l_key = 0
l_val = 0

for key, val in seen.items():
    if val > l_val:
        l_val = val
        l_key = key

print(l_key)
```
**Output**:
```bash
1
```
