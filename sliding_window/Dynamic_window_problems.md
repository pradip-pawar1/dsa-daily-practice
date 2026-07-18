# Problem 1

> Level: Easy-Medium\
> Date: 2026-07-10\
> Code File: [Click Here](../Array/day_28-medium/soln28.py)

### Code description
> Technique: Dynamic Sliding Window\
> Time complexity: O(n)\
> Space complexity: O(1)

## The Problem
You are given a __list of positive numbers and a target value__. Your task is to find the length of the smallest contiguous subarray whose sum is greater than the target. If no such subarray exists, print 0.


### Example 1 - Valid Case:
**Input**:
```py
numbers = [2, 1, 5, 2, 3, 2]
target = 7
```
**Output**:
```bash
2
```
> Because [5, 2] has sum 7 which is not greater, but [5, 3] = 8 which is greater and length is 2.

### Example 2 - No Valid Subarray:
**Input**:
```py
numbers = [1, 1, 1, 1]
target = 10
```
**Output**:
```bash
0
```
> Because even the entire array sums to 4 which is not greater than 10.


# My approach
The correct **sliding window approach** does not need a `sub_arr` list at all. I only need `left`, `total`, and `result`. When move `right forward`, add `arr[right]` to total. When `total > target`, record the **window length**, then subtract `arr[left]` from total and move left forward.

## Code

```py
def find_small_length(arr, target):
    left = 0 # left pointer
    total = 0 
    result = float('inf')

    # move right pointer 
    for right in range(len(arr)):
        total += arr[right] # move right add to total

        while total > target: # condition to trace
            window_len = right - left + 1 # length of sub-array
            if result > window_len:
                result = window_len
            total -= arr[left]
            left += 1
            

    return result
```
---

# Problem 2

> Level: Medium\
> Date: 2026-07-17\
> Code File: [Click Here](../Array/day_29-medium/soln29.py)

### Code description
> Technique: Dynamic Sliding Window\
> Time complexity: O(n)\
> Space complexity: O(1)


## The Problem
You are given a **list of positive numbers** and a target value `k`. Your task is to f**ind the length of the longest contiguous subarray** whose **sum** is exactly equal to `k`.

If no such subarray exists, `return 0`.

## Example 1 - Valid Case:
**Input**:
```py
numbers = [1, 2, 3, 1, 1, 1]
k = 6
```
**Output**:
```bash
4
```

> Because [2, 3, 1] = 6 with length 3, and [1, 2, 3] = 6 with length 3, but [3, 1, 1, 1] = 6 with length 4. Longest is 4.

# My approach
I have an **$array$**, and a **target value**. I have to find the length of contiguous subarray, whoes sum is exactly **equal to the target** value.

1. I'll always expand first
2. Then I'll check if sum excides I'll shrink the window: `if total > target: `
3. If sum equals I'll record the `max`. 

## Code
```py
def longest_length(arr, target):
    left = 0
    total = 0
    result = 0

    for right in range(len(arr)):
        total += arr[right]  # always expand first

        if total > target:   # shrink if exceeded
            total -= arr[left]
            left += 1

        if total == target:  # record if equal
            result = max(result, right - left + 1)

    return result
```
