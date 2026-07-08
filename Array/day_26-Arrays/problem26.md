# The Problem - Day 26

> Topic: Arrays + Two Pointer\
> Name: Remove Duplicates from Sorted Array\
> Level: Easy\
> Source: Claude\
> Date: YYYY-MM-DD


## The Problem
You are given a sorted list of numbers. Your task is to remove all duplicates and return only the unique elements, maintaining the same sorted order.
You cannot use `set()` or any built in function. You must use the two pointer technique.

## Key Words Explained
Sorted means elements are already **arranged smallest to largest**.
Two pointer same direction means both pointers start from the left and move forward, but at different speeds.

### Example 1 - Valid Case:
**Input:**
```
numbers = [1, 1, 2, 3, 3, 4, 5, 5]
```
**Output:**
```
[1, 2, 3, 4, 5]
```
### Example 2 - All Duplicates:
**Input:**
```
numbers = [1, 1, 1, 1]
```
**Output:**
```
[1]
```

## What you need to think about
You have two pointers moving in the same direction but at different speeds. One is exploring, one is building.
**Ask yourself this**:
"What condition tells me that the current element is different from the last unique element I already recorded?"

# My approach
> Technique: Two pointer technique in same direction\
> Time complexity: O(n)\
> Space complexity: O(1)

There is strict rule of using **Two pointer technique**, and I'll use **Two pointer technique in same direction**. Because it is the best for removing duplicates. It's _**space complexity is O(1)**_, and _**time complexity is O(n)**_. 

## Logic - 1
```py
def remove_duplicate(arr):
    slow = 0 

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1

arr = [1, 1, 2, 3, 3, 4, 5, 5]
count = remove_duplicate(arr)

print(arr[:count])
```
**Output**:
```bash
[1, 2, 3, 4, 5]
```
