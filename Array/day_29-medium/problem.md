# The Problem - Day 29

> Topic: Arrays + Sliding Window\
> Name: Longest Subarray with Sum Equal to K\
> Level: Medium\
> Source: Claude\
> Date: 2026-07-17\
> Code File: [Click here](soln29.py)


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


## What you need to think about
You just solved shrink when sum exceeds target. Now the condition is different.

Ask yourself this:
"**When should I expand, when should I shrink**, and at exactly what moment do I record the window length?"

# My approach
I have an $array$, and a target value. I have to find the length of contiguous subarray, whoes sum is exactly equal to the target value.

### How I will solve
1. Create a $function$, as `longest_length`
2. Define three variable, `left` pointer, `sum`,  and `result` $ = 0$. 
3. Run a for loop, move `right pointer` and add it to sum
4. Define a $while$ loop condition as `sum == target` and calculate the window length as $$k = \text{right} - \text{left} + 1$$

5. Now check if previous length of the subarray is **smaller than current once** or not.
    - if yes, it's smaller. Then update the `result` with current length
    - If no, it's bigger. Then do nothing and continue the loop.

6. After that remove left element from the subarra $sum -= arr[left]$, and Increament the left with one `left += 1`.

## Logic - 1:

```py
def longest_length(arr, target):
    left = 0
    sum = 0
    result = 0

    for right in range(len(arr)):
        sum += arr[right]

        while sum == target:
            window_len = right - left + 1

            if result < sum:
                result = window_len
            sum -= arr[left]
            left += 1

    return result

print(longest_length([1, 2, 3, 1, 1, 1], 6))
```

**Output**:
```
4
```

## Mistake and Improvement
Your while loop runs `while sum == target`. Think about what happens inside that loop. You record the window length, then immediately subtract from the left and shrink the window. This means you are shrinking even when you do not need to, and you will miss longer valid windows.

For example with `[1, 2, 3, 1, 1, 1]` and `k = 6`:

When your window hits `[3, 1, 1, 1]` with sum `6`, you record length 4. Then you shrink. Now sum is 3 which is not equal to 6 so the while loop stops. That part works.

But the shrinking approach here is wrong in principle. In [Day 28](../day_28-medium/problem.md) you shrunk because you wanted to minimize length. Here you want to maximize length. Shrinking works against you.

### Solution
If the sum is less than target **I expand**. If the sum equals target **I record**. If the sum exceeds target **I shrink** once. A single `if` and `elif` structure is cleaner and more correct here.

## Logic - 2
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
---
