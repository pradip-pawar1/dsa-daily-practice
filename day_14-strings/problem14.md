# The Problem Day 14
> Topic: Strings\
> Level: Beginner+\
> Source : Custom (GPT)\
> Date: 2026-04-10


## Description:
You are given a string. Your task is to **find the first non-repeating character in the string** and print it.
If every character repeats, print `None`.

## Example:
**Input**: 1
```py
text = "aabbcdeff"
```
**Output**:
```bash
c
```
---
**Input**: 2
```py
text = "aabbcdeefcfd"
```
**Output**:
```bash
None
```
---

## What you need to think about
You already know how to count frequency of each character using a dictionary. That is step one.

Ask yourself this:

"**Once I have the frequency of every character, how do I find the first one that appeared only once**, while respecting the original order of the string?"

Notice that two steps are involved here. Think about what you do first and what you do second.

# My approach
As yesterday i figured out how to find the frequency of each character as per their repetation using `Dictionary`. I have to again find out the frequency of the string and this time my, from the `dict` i have to return the first element who not repeted. If all the element are repeted the return.

## Logic - 1
```py
text = "aabbcdeefcfd"
my_dict = {}
result = "" # result

# Loop to find frequency
for i in text:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

# Loop to find first non-repeating character
for i in my_dict:
    if my_dict[i] == 1:
        result = i
        break
    
    if my_dict[i] not in my_dict:
        result = None        

print(result)
```
**Output**:

```bash
None
```

If input changes:
```py
text = "aabbcdeff"
```
Then output also changes:
```bash
c
```

---

# Mistake and Improvement for GPT
I have some dead code in my logic, which is completly differt from my actual thinking.
```py
if my_dict[i] not in my_dict:
        result = None
```

This condition cheecks for `keys` not `values`, and as my `keys` are strings they never get `True`. But accidently i am getting correct resluts, because result is initialized to `""` and when no character has count `1`, the loop ends without setting `result`, and you print `""` not `None`.

## Logic - 2
```py
text = "aabbcdeff"
my_dict = {}
result = "" # result

# Loop to find frequency
for i in text:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

# Loop to find first non-repeating character
for i in my_dict:
    if my_dict[i] == 1:
        result = i
        break
    
# check if no character found non-repeating
if result == "":
    result = None   

print(result)
```

**Output**:
```bash
c
```