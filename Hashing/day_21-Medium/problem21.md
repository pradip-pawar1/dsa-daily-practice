# The Problem - Day 21

> Topic: Arrays + Hashing\
> Name: Subarray with Zero Sum\
> Level: Medium\
> Source: Claude\
> Date: 2026-04-20


## The Problem
You are given a list of numbers. Your task is to check whether there **exists any subarray whose elements sum to zero (0)**. Print True if it exists, False if not.
A subarray is a continuous portion of the list.

## Example:
**Input**:
```py
numbers = [4, 2, -3, 1, 6]
```
**Output**:
```bash
True
```
Because 2 + (-3) + 1 = 0.

## What you need to think about
Think about the running sum as you walk through the list. Ask yourself this:

"If my running sum at two different points in the list is the same value, what does that tell me about the elements between those two points?"

That one insight is the entire key to this problem.

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
I got some hints form GPT.

## Logic - 2
### Improvement:
I will not store all elements of the list, insted i will store `currentSum` to `seen`. That's how i can know if the `currentSum` is repeated or not. If **yes**, then `result = True` and break. Also keep if zero occurs naturaly it's also a valid condition.

### Code
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
