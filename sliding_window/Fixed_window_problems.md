# Problem 1: Maximum Average Sub-array I
> Date: 2026-07-14\
> Source: Gemini

## Description
Given an array of integers and an integer $k$, find a **contiguous sub-array** of length $k$ that has the maximum average value, and return this value.

**Example**:
```py
nums = [1, 12, -5, -6, 50, 3]
k = 4
```

**Output**:
```bash
12.75
```

## Code Implementation
**Answer**: [Code File](../Fixed_sliding_window/problem1Soln.py)
```py

```py
def max_average(arr, k):
    # Build first window 
    currentWindow = sum(arr[:k])
    maxWindow = currentWindow

    # Start moving
    for i in range(k, len(arr)):
        # add new element and subtract last Element
        currentWindow = currentWindow + arr[i] - arr[i - k]
        # update maxWindow
        maxWindow = max(maxWindow, currentWindow)

    return maxWindow/k

avg = max_average([1, 12, -5, -6, 50, 3], 4)
print(avg)
```
---

# Problem 2: Find the maximum number of vowels

> Date: 2026-07-14\
> Source: Gemini

## Description
Given a string $s$ and an integer $k$, find the maximum number of vowels `('a', 'e', 'i', 'o', 'u')` in any sub-string of $s$ with length $k$.

Input: `s = "abciiidef", k = 3`

Expected Output: `3` (The sub-string "iii" contains 3 vowels)


## Code Implementation
**Answer**: [Code file](../Fixed_sliding_window/problem2soln.py)
```py
def find_max_vowels(string, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    currentVowel = 0

    for char in string[:k]:
        if char in vowels:
            currentVowel += 1

    maxVowels = currentVowel

    for i in range(k, len(string)):
        if string[i] in vowels:
            currentVowel += 1
        if string[i - k] in vowels:
            currentVowel -= 1

        maxVowels = max(currentVowel, maxVowels)
    return maxVowels

max_vowels = find_max_vowels("abciiidef", 3)
print(max_vowels)
```

**Output**:
```bash
3
```
---

# Problem 3: Defuse the Bomb
> Date: 2026-07-14\
> Source: Gemini

# Description
You have a circular bomb with an array of passwords code and a key k. To defuse the bomb, you need to replace every number in the array with the **sum of the next $k$ numbers**.

Given an array of integers code and a fixed window size $k$, **replace every element at index `i`** with the sum of the next $`k`$ elements ahead of it.

**Input**: 
```py
code = [1, 2, 3, 4]
k = 2
```
**Expected Output**: 
```bash
[5, 7, 5, 3]
```

## Code Implementation
**Answer**: [Code file](../sliding_window/problem3Soln.py)

```py
def replace_i(arr, k):
    replaced_arr = []
    n = len(arr)

    # Baseline for index 0
    current_window = sum(arr[1:k + 1])
    replaced_arr.append(current_window)

    # slide for remening index
    for i in range(1, n):
        if i + k < n:
            current_window += arr[i + k]
            
        current_window -= arr[i]

        replaced_arr.append(current_window)

    return replaced_arr

new_arr = replace_i([1,2,3,4], 2)
print(new_arr)
```