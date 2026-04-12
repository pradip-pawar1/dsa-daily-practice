# The Problem - Day 15
> Topic: Strings + Hashing\
> Level: Beginner+
> > Source : Custom (GPT)\
> Date: 2026-04-11


You are given two strings. Your task is to check whether the **two strings are anagrams of each other or not**.
Two strings are anagrams if they contain the exact same characters with the exact same frequencies, just in different order.

## Example:
**Input**:
```py
a = "listen"
b = "silent"
```

**Output**:
```bash
True
```
**Input**:
```py
a = "hello"
b = "world"
```

**Output**:
```bash
False
```

## What you need to think about
You already know how to count character frequencies using a dictionary. You did it in Day 13.
Ask yourself this:

"If I build a frequency map for both strings, what exactly do I compare to know if they are anagrams?"

That one question contains the entire solution path.

# My approach
First i have to, check the `len()` of both `string`. Because if the lenth of string is not exactly same then, its is not **Anagrams**. So First i check the length of `str` if its not same then return `False`, no need to use loops.

Second, if its same then, we create a frequency map of each character and store them into new `dict`.

Third, now i have 2 `dict` for both strings `a` and `b`. Now i pick `i` element form `dict_1` and uding loop find its same occurance in `dict_2`. If i found it with same frequency, I'll move towards next element `i + 1`, and loop continues till `i + n`. If i don't found the element `i`, means it not exist in `dict_2`. Hence the strings are not **Anagrams**.

## Locic - 1:
Logic with bugs and errors.
```py
a = "listen"
b = "silent"

dict_1 = {}
dict_2 = {}

result = False

if len(a) == len(b):
    # create frequency map 
    for i in a:
        if i not in dict_1:
            dict_1[i] = 1
        else:
            dict_1[i] += 1

    for j in b:
        if j not in dict_2:
            dict_2[j] = 1
        else:
            dict_2[j] += 1

# check the dicts
for key, val in dict_1.items():
    if (dict_1[key] and dict_1 [val]) not in dict_2:
        result == False
        break

    else:
        result == True

print(result)
```
---

# Mistake and Improvement for GPT
This code is overall wrong logically and overly complecated. 

```py
if (dict_1[key] and dict_1[val]) not in dict_2:
```

I have `dict_1` and `dict_2`. I am looping `dict_1` with `key` and `value`. I just have to ceck if the `key` exist in `dict_2`? If yes, then does it have same `value`?

---
## Logic - 2
```py
a = "listen"
b = "silent"

dict_1 = {}
dict_2 = {}

result = True

if len(a) == len(b):
    # create frequency map 
    for i in a:
        if i not in dict_1:
            dict_1[i] = 1
        else:
            dict_1[i] += 1

    for j in b:
        if j not in dict_2:
            dict_2[j] = 1
        else:
            dict_2[j] += 1
else:
    result = False

# check the dicts
for key, val in dict_1.items():
    if key not in dict_2:
        result = False
    elif dict_2[key] != val:
        result = False

print(result)
```
**Output**:
```bash
True
```