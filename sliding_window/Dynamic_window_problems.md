# Problem 1

> Topic: Arrays + Sliding Window\
> Name: Smallest Subarray with Sum Greater than Target\
> Level: Easy-Medium\
> Source: Claude\
> Date: 2026-07-10\
> Code File: [Click Here](../Array/day_28-medium/soln28.py)

### Code description
> Technique: Dynamic Sliding Window\
> Time complexity: O(n)\
> Space complexity: O(1)

## The Problem
You are given a __list of positive numbers and a target value__. Your task is to find the length of the smallest contiguous subarray whose sum is greater than the target. If no such subarray exists, print 0.

## Key Words Explained
- Smallest subarray means you want the shortest possible window, not the largest.
- Greater than target means strictly greater, not equal.
- Dynamic sliding window means the window size is not fixed like Day 27. It can shrink and grow based on a condition.

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

## What you need to think about
Unlike Day 27 the window size here is not fixed. It grows and shrinks.
Ask yourself this:
"**When should I expand the window, and when should I shrink** it from the left to find something smaller?"

# My approach
I have a list/array, and i have to find a sub-array whose sum is grater that the `target` value and return that sub-arrays length. I will use I will inatialize `left = 0`, `sum = 0`, and `result = 0`. And the `right_pointer` will run in a $for$ loop.

Then start the $for$ loop. Inside loop i will create a `sub_array`, and add one element every iteration as `arr[right]`. Then I'll calculate the sum of `sub_array`, if it is greater that `target` means, $While% loop condition meets (`while sum > target`). Inside that I'll check does my last `reslut` is grater that current once? If yes, then I'll change it with new length. and remove one element from `sub_array` as `sub_arr.pop(left)`. and increment left with 1.

## LOgic -1:
```py
def find_small_length(arr, target):
    left = 0
    total = 0
    result = float('inf')

    # move right pointer 
    for right in range(len(arr)):
        sub_arr = []
        sub_arr.append(arr[right])
        total = sum(sub_arr)

        while total > target:
            if result < len(sub_arr):
                result = len(sub_arr)
            else:
                sub_arr.pop(left)
                left += 1
    return result
      
print(find_small_length([2,1,5,2,3,2], 7))
```

## Mistake, Bugs & Solution
I am using the approcah fundimantely wrong, by creating a sub-array, but sliding windown is all about changing the same array.

**Bug 1**: I am creating a new `empty sub_arr` inside the for loop on every iteration. That means I reset the **subarray** on every step. The whole point of sliding window is that you maintain a running window across iterations, not rebuild it from scratch each time.

**Bug 2**: I am doing `total = sum(sub_arr)` which uses the built-in `sum()`. More importantly, since i rebuild `sub_arr` every iteration with only one element, total is always just `arr[right]`. i was never actually accumulating a window sum.

**Bug 3**: The **while condition logic is inverted**. I want to shrink the window when `total > target` and record the length. But inside the while loop I am checking `if result < len(sub_arr)` which saves the larger length, not the smaller one. I initialized `result = float('inf')` which means I want the minimum, so I should update result only when I find something smaller.

**Bug 4**: `sub_arr.pop(left)` is wrong. `pop()` takes an index position within the list, not a value. And since i am rebuilding `sub_arr` each iteration anyway, this does not work at all.

### Corrwct approach
The correct **sliding window approach** does not need a `sub_arr` list at all. I only need `left`, `total`, and `result`. When move `right forward`, add `arr[right]` to total. When `total > target`, record the **window length**, then subtract `arr[left]` from total and move left forward.

## Logic 2
**Answer**: [Code file](../day_28-medium/soln28.py)

> Technique: Dynamic Sliding Window\
> Time complexity: O(n)\
> Space complexity: O(1)


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
      
print(find_small_length([2,1,5,2,3,2], 7)) # output 3
print(find_small_length([2,5, 3, 7, 9, 2, 3], 6)) # output 1
print(find_small_length([2,5, 3, 7, 9, 2, 3], 15)) # output 2
```
**Output**:
```bash
3
1
2
```
---
