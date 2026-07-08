# The Problem - Day 19
> Topic: Arrays + Hashing\
> Level: Medium\
> Source: GPT\
> Date: 2026-04-17


You are given a list of numbers. Your task is to **find the longest consecutive sequence in the list** and print its length.
A consecutive sequence means numbers that follow one after another like 1, 2, 3, 4 regardless of their order in the list.

## Example:
**Input**:
```py
numbers = [100, 4, 200, 1, 3, 2]
```
**Output**:
```bash
4
```
Because 1, 2, 3, 4 is the longest consecutive sequence and its length is 4.

## What you need to think about
You have a list in random order. You need to find sequences hidden inside it.

Ask yourself this:
"How do I quickly check whether the next number in a sequence exists in the list, without looping through the entire list every single time?"

That question points you toward using a dictionary or a set in a smart way.

## Hints
### Hint 1:
Before anything else, store all the numbers in a dictionary or set so you can check if a number exists instantly without looping.

### Hint 2:
Think about where a sequence starts. A number is the start of a sequence only if the number just before it does not exist in the list. For example, 1 is a sequence start because 0 is not in the list. But 2 is not a start because 1 exists.

Once you find a starting point, keep checking if the next number exists, then the next, and count how far the sequence goes.

# My approach
First I'll store all elements in a dict as `myDict`. And then create a variable as `count` to store the smallest number from the `numbers list`.

Also i create another **empty list**, and increament count in each iteration.and if `i` matches with `count` then increment `i` to new list. In the end i have sequence of list and i will prent its lenth.

## Logic - 1:
> Solved by GPT
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
**Output**:
```bash
4
```