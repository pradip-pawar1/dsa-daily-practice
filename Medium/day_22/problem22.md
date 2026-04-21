# The Problem - Day 22

> Topic: Strings + Hashing\
> Name: Count Distinct Common Characters\
> Level: Medium\
> Source: Claude\
> Date: YYYY-MM-DD


## The Problem
You are given two strings. Your task is to **find the number of distinct characters that are common** in both strings.

Distinct means **unique**, do not count the same character more than once even if it appears multiple times.
Common means the character must exist in both strings, not just one of them.

## Examples
**Example 1** - Valid Case:

**Input**:
```py
a = "abcdef"
b = "bdfxyz"
```
**Output**:
```bash
3
```

Because b, d, f appear in both strings. So the count is 3.

**Example 2** - Where you might go wrong:
**Input**:
```py
a = "aabbcc"
b = "abcabc"
```

**Output**:
```bash
3
```
Even though a, b, c appear multiple times in both strings, you count each common character only once. So the answer is still 3, not 6 or anything else.

## What you need to think about
You know how to build a frequency map using a dictionary. You have done it before.
**Ask yourself this**:

"If I store the characters of one string in a dictionary, how do I check which characters of the second string are common, without counting the same character more than once?"


# My approach
I will create 2 empty `dict` as `aSeen = {}` and `bSeen = {}`. The i will use two loops:

**Loop - 1**: for creating map of a\
**Loop - 2**: for creating map of b. And if it's already in the `dict` then don't add it.

Then finally create a variable as `count` and check through loop if same `char` exists in both `dict`, increment `count += 1`.

## Logic - 1

```py
# a = "abcdef"
# b = "bdfxyz"

a = "aabbcc"
b = "abcabc"

aSeen = {} # map of a
bSeen = {} # map of b

count = 0 # result

# Create map of a 
for i in a:
    if i not in aSeen:
        aSeen[i] = True

# create map of b    
for i in b:
    if i not in bSeen:
        bSeen[i] = True

# find reslut         
for j in aSeen:
    if j in bSeen:
        count += 1

print(count) # show result
```
**Output**:
```
3
```
---