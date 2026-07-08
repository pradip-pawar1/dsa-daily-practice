# The Problem - Day 24

> Topic: Arrays + Two Pointer\
> Name: Pair with Target Sum in Sorted List\
> Level: Medium\
> Source: Claude\
> Date: 2026-04-23


## The Problem
You are given a sorted list of numbers and a target value. Your task is to **find whether any two numbers in the list add up to the target**. Print _**True** if found, **False** if not_.

**Important**: You cannot use a dictionary or hashing for this problem. You must use the two pointer technique only.


Two pointer means you place one pointer at the beginning of the list and one at the end, and move them toward each other based on a condition. You have used this idea before in Day 3 and Day 12.

### Example 1 - Valid Case:
**Input**:
```py
numbers = [1, 3, 5, 7, 9, 11]
target = 12
```
**Output**:
```bash
True
```
> Because 1 + 11 = 12.


### Example 2 - False Case:
**Input**:
```py
numbers = [1, 3, 5, 7, 9, 11]
target = 4
```
**Output**:
```bash
False
```
> Because no two numbers add up to 4.

## What you need to think about
You have one pointer at the start and one at the end. You check their sum. 

**Ask yourself this**:
"If the sum of the two pointers is too large, which pointer should I move and in which direction? And if the sum is too small, what should I do then?"
That logic is the entire solution.

# My approach
I will use 2 pointer approach to find this. As i used in [Day 3](../../Biginner/day_03-Arrays/soln-Array3.py), left and right. Left is `0` and right is `len(arr) - 1`. I'll move one point from both side to find the `target`.

## Logic - 1
```py
numbers = [1, 3, 5, 7, 9, 11]
target = 12

result = False

left = 0
right = len(numbers) - 1

while left < right:
    if (numbers[left] + numbers[right]) == target:
        result = True
        break
    
    left += 1
    right -= 1

print(result)
```
**Output**:
```bash
True
```

> I think this logic has a bug?

## Mistake and improvement
**Mistake**:  The list is sorted. That is the key information. If `numbers[left] + numbers[right]` is too large, which pointer should move and in which direction? Moving right inward gives a smaller number, making the sum smaller.

If the sum is too small, which pointer should move? Moving left inward gives a larger number, making the sum larger.

**Improvement**:
So the logic is, move only one pointer per iteration based on whether the sum is too large or too small. __Not both at once.__

## Logic - 2
```py
numbers = [1, 3, 5, 7, 9, 11]
target = 12

result = False

left = 0 # left index
right = len(numbers) - 1 # right index

while left < right: # loop
    addition = numbers[left] + numbers[right]

    if addition == target: # check soln
        result = True
        break

    elif addition > target: # if soln is to0 big
        right -= 1

    elif addition < target: # if soln is too small
        left += 1
    
print(result)
```
**Output**:
```bash'
True
```
---