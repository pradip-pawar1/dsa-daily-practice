# The problem : Day 5
>Topic: Arrays (Python Lists)\
>Level: Beginner+

You are given a list of numbers. Your task is to **count how many times a given number appears** in the list.
You cannot use `.count()` or any built-in counting function.

### Example:
**Input:**
```py
numbers = [1, 3, 5, 3, 7, 3, 9]
target = 3
```

**Output:**
```bash
3
```

## What you need to think about
You already know how to walk through a list and check each element. Now ask yourself this:
"Instead of stopping when I find the target, what should I do every time I find it?"
That one shift in thinking is all you need.

---
# My approach
I'll iterate a list through for loop, and create a variable `count = 0` and each time when I go/found the `target` number I'll increase the value of `count` by 1.

---
# Attemp 1
```py
numbers = [1, 3, 5, 3, 7, 3, 9]
target = 3

count = 0

for i in numbers:
    if i == target:
        count += 1

print(count)
```

**Output:**
```bash
3
```
---
> Solved in first attempt within 7 Min.