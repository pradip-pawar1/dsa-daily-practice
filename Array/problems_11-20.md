# Problem 11 - Day 24

> Topic: Arrays + Two Pointer\
> Name: Pair with Target Sum in Sorted List\
> Level: Medium\
> Source: Claude\
> Date: 2026-04-23\
> Code File: [Click Here](problem11solution.py)


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
I will use 2 pointer approach to find this. As i used in [Day 3](../problem3solution.py), left and right. Left is `0` and right is `len(arr) - 1`. I'll move one point from both side to find the `target`.

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

## Mistake and improvement
**Mistake**:  The list is sorted. That is the key information. If `numbers[left] + numbers[right]` is too large, which pointer should move and in which direction? Moving right inward gives a smaller number, making the sum smaller.

If the sum is too small, which pointer should move? Moving left inward gives a larger number, making the sum larger.

**Improvement**:
So the logic is, move only one pointer per iteration based on whether the sum is too large or too small. __Not both at once.__

## Code
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
---

# Problem 12 - Day 26

> Topic: Arrays + Two Pointer\
> Name: Remove Duplicates from Sorted Array\
> Level: Easy\
> Source: Claude\
> Date: 2026-07-08\
> Code File: [Click Here](problem12solution.py)


## The Problem
You are given a sorted list of numbers. Your task is to remove all duplicates and return only the unique elements, maintaining the same sorted order.
You cannot use `set()` or any built in function. You must use the two pointer technique.


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

# My approach

There is strict rule of using **Two pointer technique**, and I'll use **Two pointer technique in same direction**. Because it is the best for removing duplicates. It's _**space complexity is O(1)**_, and _**time complexity is O(n)**_. 

## Code

> Technique: Two pointer technique in same direction\
> Time complexity: O(n)\
> Space complexity: O(1)

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
---

# Problem 13 - Day 27

> Topic: Arrays + Sliding Window\
> Name: Maximum Sum Subarray of Size K\
> Level: Easy\
> Source: Claude\
> Date: 2026-07-08\
> Code File: [Click Here](problem13solution.py)


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

## What you need to think about
Calculating the sum of every window from scratch would be slow. **Ask yourself this**:
"When I slide the window one step forward, what exactly changes in the sum and what stays the same?"

# My approach

This kinds of problems always use siliding window, and here it's already mentioned to use.

## Code
> Technique: Sliding Window\
> Time complexity: O(n)\
> Space complexity: O(1)

```py
def max_sum(arr:list, k:int):
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
---

# Problem 14 - Day 28

> Topic: Arrays + Sliding Window\
> Name: Smallest Subarray with Sum Greater than Target\
> Level: Easy-Medium\
> Source: Claude\
> Date: 2026-07-10\
> Code File: [Click Here](problem14solution.py)


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
I have a list/array, and i have to find a sub-array whose sum is grater that the `target` value and return that sub-arrays length. I will use I will inatialize `left = 0`, `sum = 0`, and `result = 0`. And the `right_pointer` will run in a $for$ loop.

Then start the $for$ loop. Inside loop i will create a `sub_array`, and add one element every iteration as `arr[right]`. Then I'll calculate the sum of `sub_array`, if it is greater that `target` means, $While$ loop condition meets (`while sum > target`). Inside that I'll check does my last `reslut` is grater that current once? If yes, then I'll change it with new length. and remove one element from `sub_array` as `sub_arr.pop(left)`. and increment left with 1.


## Mistake
I am using the approcah fundimantely wrong, by creating a sub-array, but sliding windown is all about changing the same array.


## Correct approach
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
      
print(find_small_length([2,1,5,2,3,2], 7)) # output 3
print(find_small_length([2,5, 3, 7, 9, 2, 3], 6)) # output 1
print(find_small_length([2,5, 3, 7, 9, 2, 3], 15)) # output 2
```
---

# Problem 15 - Day 29

> Topic: Arrays + Sliding Window\
> Name: Longest Subarray with Sum Equal to K\
> Level: Medium\
> Source: Claude\
> Date: 2026-07-17\
> Code File: [Click here](problem15solution.py)


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


## Mistake and Improvement
Your while loop runs `while sum == target`. Think about what happens inside that loop. You record the window length, then immediately subtract from the left and shrink the window. This means you are shrinking even when you do not need to, and you will miss longer valid windows.

For example with `[1, 2, 3, 1, 1, 1]` and `k = 6`:

When your window hits `[3, 1, 1, 1]` with sum `6`, you record length 4. Then you shrink. Now sum is 3 which is not equal to 6 so the while loop stops. That part works.

But the shrinking approach here is wrong in principle. In [Day 28](../day_28-medium/problem.md) you shrunk because you wanted to minimize length. Here you want to maximize length. Shrinking works against you.

### Solution
If the sum is less than target **I expand**. If the sum equals target **I record**. If the sum exceeds target **I shrink** once. A single `if` and `elif` structure is cleaner and more correct here.

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
---
