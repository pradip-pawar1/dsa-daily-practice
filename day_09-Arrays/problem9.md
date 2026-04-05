# The Problem Day 9
> Topic: Arrays (Python Lists)\
> Level: Beginner+


You are given a list of numbers. Your task is to **find the missing number** in the list.
The list contains numbers from 1 to n in random order, but **exactly one number is missing**. You have to find which one.

### Example
**Input:**
```py
numbers = [1, 3, 4, 5, 2, 7, 8, 6, 10]
n = 10
```

**Output:**
```bash 
9
```

## What you need to think about
You know what the list should contain. You know what it actually contains. Ask yourself this:

"**If I know the total sum of numbers from 1 to n**, and I know the sum of what is actually in the list, what does the difference tell me?"

That one mathematical insight eliminates the need for any complex logic.

---

# My thinking
I tried to think a lot, but i din't found any patter. Scince, this is mathematical question, i don't know the formula. So i did **GPT** and get the formula as, `sum = n * (n + 1) / 2`. After that i have to calculate the sum of all elements form a list `sumNums`. And then substract `sumNums - sum`  to get the `missing` element.

## Logic
**Code**

```py
numbers = [1, 3, 4, 5, 2, 7, 8, 6, 10]
n = len(numbers) + 1

expected_sum = n * (n + 1) / 2
sumNums = 0

for i in numbers:
    sumNums += i

missing = expected_sum - sumNums
print(missing)
```
**Output**
```bash
9
```
---
