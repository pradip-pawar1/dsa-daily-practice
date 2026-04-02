# The problem Day 6
> Topic: Arrays (Python Lists)\
> Level: Beginner+


You are given a list of numbers. Your task is to find the **sum of all even numbers in the list**.
You cannot use sum() or any built-in function.

### Example:
**Input:**
```
numbers = [1, 2, 3, 4, 5, 6]
```

**Output:**
```
12
```
---


## What you need to think about
You already know how to walk through a list and check each element. Now ask yourself this:
"How do I know if a number is even, and what do I do with it when it is?"

# My appraoch.
To iterate the list i will use `for` loop. I will make a variable as `sum = 0` and inside for loop i'll add a condition to check, weather the curret number `i` is even or not? If it's odd then let it go but if it's even then add current number `i` to `sum` as `sum += i`. 

## Attempt 1
```
numbers = [1, 2, 3, 4, 5, 6]
total = 0

for i in numbers:
    if i%2 == 0:
        sum += i
    
print(total)
```
---
> Solved in first attempt within 5 Min.