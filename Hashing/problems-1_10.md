# Problem 1 - Day 15
> Topic: Strings + Hashing\
> Name: Strings are anagrams or not?\
> Level: Beginner+\
> Source : Claude\
> Date: 2026-04-11\
> Code File: [Click Here](solution_1.py)


## The problem
You are given two strings. Your task is to check whether the **two strings are anagrams of each other or not**.
Two strings are anagrams if they contain the exact same characters with the exact same frequencies, just in different order.

### Example 1:
**Input**:
```py
a = "listen"
b = "silent"
```

**Output**:
```bash
True
```
### Example 2: 
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
**Ask yourself this**: "If I build a frequency map for both strings, what exactly do I compare to know if they are anagrams?"

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

## Mistake and Improvement for GPT
This code is overall wrong logically and overly complecated. 

```py
if (dict_1[key] and dict_1[val]) not in dict_2:
```

I have `dict_1` and `dict_2`. I am looping `dict_1` with `key` and `value`. I just have to ceck if the `key` exist in `dict_2`? If yes, then does it have same `value`?

---
## Code
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
---

# Problem 2 - Day 16
> Topic: Hashing (Python Dictionaries)\
> Name: appear more than once\
> Level: Beginner+\
> Source: Custom (GPT)\
> Date: 2026-04-12\
> Code file: [Click Here](solution_2.py)

## The problem
You are given a list of numbers. Your task is to find all numbers that appear more than once in the list and print them.

### Example:

**Input**:
```py
numbers = [1, 3, 2, 3, 5, 1, 4, 2, 2]
```
**Output**:
```bash
[1, 3, 2]
```

---

# My Approach
First, I'll create a map of all key as elements of list, and their frequirency as their repetation. Then implement the same logic as [Day 15](solution_1.py), just i have to reverse it. Now i have to only exclude keys with single keys.

I will cheak frequency map `if value > 1` means key is repeating. So once i found key is repeating i will add it to new list.


## Code
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
---

# Problem 3 - Day 17
> Topic: Hashing (Python Dictionaries)\
> Name: Two sum\
> Level: Beginner+\
> Source: Custom (GPT)\
> Date: 2026-04-13\
> Code file: [Click Here](solution_3.py)

## The problem
You are given a list of numbers. Your task is to **find whether any two numbers in the list add up to a given target sum**.
Print `True` if such a pair exists, `False` if not.


### Example:
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

## Code: Solved by GPT
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
---

# Problem 4 - Day 18
> Topic: Strings + Hashing\
> Name: Highest frequecncy chracter\
> Level: Beginner+\
> Source: GPT\
> Date: 2026-04-16\
> Code file: [Click Here](solution_4.py)

## The problem
You are given a string. Your task is to **find the most frequently occurring character in the string and print it along with its count**.
If two characters have the same highest frequency, _print the one that appears first_ in the string.

### Example:
**Input**:
```py
text = "aabbcccdd"
```
**Output**:
```bash
c 3
```

# My approach
I will create a new dictionary where store all character with their frequency. Then throught second loop, find most larget value and store in a variable with key.

## Code
```py
text = "aabbcccdd"
freq_map = {}

for i in text:
    if i not in freq_map:
        freq_map[i] = 1
    else:
        freq_map[i] += 1

most_key = ""
most_val = 0

for key, val in freq_map.items():
    if val > most_val:
        most_val = val
        most_key = key
    
print(f"{most_key} : {most_val}")
```
---

# Problem 5 - Day 19
> Topic: Arrays + Hashing\
> Name: longest consecutive sequence in the list\
> Level: Medium\
> Source: GPT\
> Date: 2026-04-17\
> Code file: [Click Here](solution_5.py)

## The problem
You are given a list of numbers. Your task is to **find the longest consecutive sequence in the list** and print its length.
A consecutive sequence means numbers that follow one after another like 1, 2, 3, 4 regardless of their order in the list.

### Example:
**Input**:
```py
numbers = [100, 4, 200, 1, 3, 2]
```
**Output**:
```bash
4
```
Because 1, 2, 3, 4 is the longest consecutive sequence and its length is 4.

# My approach
First I'll store all elements in a dict as `myDict`. And then create a variable as `count` to store the smallest number from the `numbers list`.

Also i create another **empty list**, and increament count in each iteration.and if `i` matches with `count` then increment `i` to new list. In the end i have sequence of list and i will prent its lenth.

## Code: Solved by GPT
```py
numbers = [100, 4, 200, 1, 3, 2]
seen = {}

# Step 1: Store all numbers in seen
for i in numbers:
    seen[i] = True

longest = 0

# Step 2: Find sequence starts and count
for i in numbers:
    if (i - 1) not in seen:  # i is a start
        current = i
        length = 1
        
        # Step 3: Count forward
        while (current + 1) in seen:
            current += 1
            length += 1
        
        # Step 4: Update longest
        if length > longest:
            longest = length

print(longest)
```
---

# Problem 6 - Day 20
> Topic: Arrays + Hashing\
> Name: The most frequently occurring number\
> Level: Medium\
> Source: GPT\
> Date: 2026-04-19\
> Code file: [Click Here](solution_6.py)

## The problem
You are given a list of numbers. Your task is to **find the most frequently occurring number** in the list and print it. If two numbers have the same frequency, print the one that appears first in the list.

### Example:
**Input**:
```py
numbers = [1, 3, 2, 1, 4, 3, 1, 2]
```

**Output**:
```bash
1
```
Because 1 appears 3 times which is the highest frequency.

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

You are mixing up two things. You need to track both the best `key` and the best `value` separately, exactly like you did in [**Day 18**](solution_4.py).


## Code
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
---


# Problem 7 - Day 21

> Topic: Arrays + Hashing\
> Name: Subarray with Zero Sum\
> Level: Medium\
> Source: Claude\
> Date: 2026-04-20\
> Code file: [Click Here](solution_7.py)


## The Problem
You are given a list of numbers. Your task is to check whether there **exists any subarray whose elements sum to zero (0)**. Print True if it exists, False if not.
A subarray is a continuous portion of the list.

### Example:
**Input**:
```py
numbers = [4, 2, -3, 1, 6]
```
**Output**:
```bash
True
```
Because 2 + (-3) + 1 = 0.

# My approach
I will create a dictionary as `seen`, inside that dictionary i will create a map of all elements of a list.

I will focus on **running sum**. If at any point it repeats, means inside all values are cutting each others. E.x., at **index 1**, `x = 4` and at **index 5**, `x = 4`, means values at index `2, 3, & 4` are canceling out each others. So it is a **Subarray with Zero Sum**.

And any value of remaning sum itself is zero (0), means condition is true. Subarray exists with zero sum. `Result` is `True` and `breake` the loop.

## Logic - 1
```py
numbers = [4, 2, -3, 1, 6]
seen = {}
result = False

# Create map 
for i in numbers:
    seen[i] = True

# check subarray exists or not
currentSum = 0
for i in seen:
    if i == 0:
        result = True
        break
    
    currentSum += i
    # stucked..!

print(result)
```

## Improvement:
I will not store all elements of the list, insted i will store `currentSum` to `seen`. That's how i can know if the `currentSum` is repeated or not. If **yes**, then `result = True` and break. Also keep if zero occurs naturaly it's also a valid condition.

## Code
```py
numbers = [4, 2, -3, 1, 6]
seen = {} # dictionary store sum

result = False # Result
currentSum = 0 # Current sum

# Create map 
for i in numbers:
    # create map 
    currentSum += i
    seen[currentSum] = True

    # if zero occurs
    if i == 0:
        result = True
        break

    # if repetating sum found in seen 
    elif currentSum in seen:
        result = True
        break

# result
print(result)
```
**Output**:
```bash
True
```

## Logic - 3
### Improvements
It still has 2 bugs.

**Bug one**. Look at the order of your code inside the loop:
```py
currentSum += i
seen[currentSum] = True  # you store it first

elif currentSum in seen:  # then check if it exists
```

**Bug two**. Your zero check is wrong:
```py
if i == 0:
```

### Code:
```py
numbers = [4, 2, -3, 1, 6]
seen = {} # dictionary store sum

result = False # Result
currentSum = 0 # Current sum

# Create map 
for i in numbers:
    # create map 
    currentSum += i

    # if zero occurs
    if currentSum == 0:
        result = True
        break

    # if repetating sum found in seen 
    elif currentSum in seen:
        result = True
        break

    # Add to seen 
    seen[currentSum] = True

# result
print(result)
```
---
# Problem 8 - Day 22

> Topic: Strings + Hashing\
> Name: Count Distinct Common Characters\
> Level: Medium\
> Source: Claude\
> Date: 2026-04-21\
> Code file: [Click Here](solution_8.py)


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

# My approach
I will create 2 empty `dict` as `aSeen = {}` and `bSeen = {}`. The i will use two loops:

**Loop - 1**: for creating map of a\
**Loop - 2**: for creating map of b. And if it's already in the `dict` then don't add it.

Then finally create a variable as `count` and check through loop if same `char` exists in both `dict`, increment `count += 1`.

## Code

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
# Problem 9 - Day 23

> Topic: Arrays + Hashing\
> Name: First Duplicate Number\
> Level: Medium\
> Source: Claude\
> Date: 2026-04-22\
> Code file: [click file](solution_9.py)


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
---

## Improvement
You are building the full frequency map first, then looping through the dictionary to find the first key with frequency greater than one. But dictionary insertion order is based on first appearance, not on which number repeated first.

**Example**:
```py
numbers = [2, 3, 4, 3, 2]
```

Here `3` repeats first at index `3`, and `2` repeats second at index `4`. So the correct answer is `3`. But your dictionary order will be `2, 3, 4` based on first appearance. When you loop through it, you will find `2` first and print `2`, which is wrong.

Your two loop approach cannot solve this problem correctly. You need a single loop that detects the duplicate the moment the second occurrence is seen.

## Code
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
---
