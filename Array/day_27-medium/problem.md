# The Problem - Day 27

> Topic: Arrays + Sliding Window\
> Name: Maximum Sum Subarray of Size K\
> Level: Easy\
> Source: Claude\
> Date: 2026-07-08


## The Problem
You are given a list of numbers and a number `k`. Your task is to find the **maximum sum of any contiguous subarray** of size exactly `k`.

## Key Words Explained
- Subarray means a continuous portion of the list. You cannot skip elements.
- Size `k` means the subarray must contain exactly `k` elements, _no more no less_.
- **Sliding window** means you take a window of size `k`, calculate its sum, then slide it one step forward by removing the leftmost element and adding the next right element. This avoids recalculating the entire sum every time.

### Example 1 - Valid Case:
**Input**:
```py
numbers = [2, 1, 5, 1, 3, 2]
k = 3
```
**Output**:
```bash
9
```

> Because subarray [2, 1, 5] = 8, [1, 5, 1] = 7, [5, 1, 3] = 9, [1, 3, 2] = 6. Maximum is 9.

### Example 2 - Where you might go wrong:
**Input**:
```py
numbers = [1, 1, 1, 1, 1]
k = 2
```

**Output**:
```bash
2
```
> Every window has sum 2. Do not overcomplicate it.

## What you need to think about
Calculating the sum of every window from scratch would be slow. Ask yourself this:
"When I slide the window one step forward, what exactly changes in the sum and what stays the same?"

# My approach

This kinds of problems always use siliding window, and here it's already mentioned to use.

## Logic - 1
> Technique: Sliding Window\
> Time complexity: O(n)\
> Space complexity: O(1)

```py
# Sliding window technique
def max_sum(arr:list, k:int):
    # Time complexity = O(n)

    n = len(arr)

    # if array is less that subarray
    if n < k:
        return 0
    
    windowSum = sum(arr[:k]) # Sum of k
    maxSum = windowSum # Max sum
    # sliding window
    for i in range(k, n):
        windowSum = windowSum + arr[i] - arr[i - k]
        maxSum = max(maxSum, windowSum)

    return maxSum

numbers = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum(numbers, k))
```

**Output**:
```bash
9
```