# The Problem - Day 10
> Topic: Arrays (Python Lists)\
> Level: Beginner+


You are given a list of numbers. Your task is to **find the largest and smallest number at the same time in a single loop pass**.
You cannot use `max()`, `min()`, or any built-in function.

### Example
**Inpute**:
```py
numbers = [4, 7, 1, 9, 3, 6]
```

**Output**:
```bash
Largest: 9
Smallest: 1
```

## What you need to think about
You have done largest before. You have done logic building. Now ask yourself this:

"**Can I track two things simultaneously inside one single loop?**"

That is the entire challenge.

---

# My approach
I will use 2 condition in a same loop. First I'll create 2 variables as `largest = list[0]` and `smallest = list[0]`, both initialize with **first element of the list**. 

When i start a `for loop`, inside i have 2 conditions:
1. As `if i > largest`
2. As `elif i < smallest`

When `if i > largest` will execuated, then change the value of `largest` with `i`. And when `elif i < smallest` then change the value of `smallest` with `i`.

Make sure that both condition can't be execuated. And both cannot be true at once. 
**Example**: If `i = 4`and `largest & smallest = 4`, not both condition will faile. But if `largest & smallest = 4` and `i = 7`, then `if` condition will execuate and `elif` is fale by default. Same when `i = 1` then `if` will not execuated, as it failse by default. But smallest will change.

## Logic - Attempt 1

```py
# Q. You are given a list of numbers. Your task is to find the largest and smallest number at the same time in a single loop pass.

numbers = [4, 7, 1, 9, 3, 6]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

    elif i < smallest:
        smallest = i

print(f"Largest : {largest}")
print(f"Smallest : {smallest}")
```

**Output**:
```bash
Largest : 9
Smallest : 1
```
---

## Small Improvement
Insted using `if` and `elif`, we can use directly 2 `if` statements. This can improve understnadingand readability. _Improvement form GPT_.

## Locic (Same) - Attempt 2

```py
numbers = [4, 7, 1, 9, 3, 6]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print(f"Largest : {largest}")
print(f"Smallest : {smallest}")
```

> Same output, same result. Just improved readabality...

