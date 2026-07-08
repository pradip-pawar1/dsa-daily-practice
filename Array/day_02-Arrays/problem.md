# The Problem: Day 2
>## Topic: Arrays (Python Lists)

You are given a list of numbers. Your task is to find the second largest number in that list.
You cannot use max(), sort(), or any built-in shortcut. Pure logic only.

### Example:

**Input:**
```py
numbers = [3, 7, 1, 9, 4, 6]
```

**Output:**
```
7
```

## What you need to think about
You already know how to track the largest number as you walk through a list. Now ask yourself this:
"While I am tracking the largest, what else can I track at the same time that would give me the second largest?"

---


# My approch

As I already know, how to find largest number for list or array. I'll use the same approch to track second largest number. Like; I have list of nunbers as array. 

**E.x,**
```py
numbers = [3, 7, 1, 9, 4, 6]
```
I'll Initialize a variable as `max_num = 0`, and `second_large = 0`.
Then run a for loop on `numbers`. Inside for loop check current number, if current number is `>` `max_num` then `max_num` is currnt number.And before initilaizing **current largest number to `max_num`**, first add it to `second_large` then current number = `max_num`. Else, the current number is `< max_num` then `max_num` and `second_large` remain as it is.

## Attempt 1
```py
numbers = [3, 7, 1, 9, 4, 10, 1]

max_num = numbers[0]
second_large = 0

for i in numbers:
    if i > max_num:
        second_large = max_num
        max_num = i

print(f"Largesr number is: {max_num}, \nSecond largest number is: {second_large}")
```
---
# Improvement form GPT:
Run your code mentally on this list:
```py
numbers = [3, 7, 1, 9, 4, 6]
```

Walk through it step by step. What is `max_num` and `second_large` after each iteration? Write it out. You will find a case where a number gets ignored completely, even though it deserves to be the second largest.

Here is the specific question: _what happens when you encounter a number that is not greater than max_num, but is still greater than second_large?_ Does your code handle that case?

Right now your else branch does nothing. Is that always correct?

Think about what the second largest number really means. It is not just **"the number that was largest before the current largest."** It is the largest number among all numbers that are not the maximum. Those are two different things.

# What I did wrong?
1. I am initializing `max_num` and `second_large` as 0 but for some specific condition it fails.
2. I am  not handling a case where second largest number is less that `max_num` but still grater that last `second_large`.

# What I changed?
I fixed the initialization problem.

**Example**:
```py
max_num = numbers[0]
second_large = numbers[0]
```
But with a condition where it handels the case where `second_large < max_num` but last `second_large > current secodn large`.

## Attempt 2
```py
numbers = [-9, 9, 3, 1, 7, 9]

max_num = numbers[0]
second_large = numbers[0]

for i in numbers[1:]:
    if i > max_num:
        second_large = max_num
        max_num = i
    elif i > second_large and i != max_num:
        second_large = i

print(f"Largest: {max_num}")
print(f"Second largest: {second_large}")
```

**Output**
```bash
Largest: 9
Second largest: 7
```
---