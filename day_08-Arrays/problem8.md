# The Problem Day 8
> Topic: Arrays (Python Lists)\
> Level: Beginner+


You are given a list of numbers. Your task is to **move all zeros to the end of the list while keeping the order of all non-zero numbers exactly the same**.
You cannot use any built-in sorting or filtering functions.

### Example:
**Input:**
```py
numbers = [0, 1, 3, 0, 5, 0, 2]
```

**Output:**
```bash
[1, 3, 5, 2, 0, 0, 0]
```

## What you need to think about
You have two kinds of elements in the list. Non-zeros need to stay in their original order. Zeros need to pile up at the end.
Ask yourself this:
"Instead of moving zeros, what if **I focus on collecting what I want to keep first, and then deal with what is left**?"
That shift in perspective is the key to this problem.

---

# My approach
I have a list, of length `n`. I have to move all zeros at last of the list. First, i will create a new list _(Allowed for this question)_, and an variable `count = 0`. 

Then by traversing, I will add a condition that if the element `i` is not equals to `0` then add it to new list. Else if the element is zero, so increment `count += 1`. 

By this, i will have non-zeros in the same order as they occures and secondly, I also have the count of zeros. Now, add `count` times 0 to the `newList` at last.

## Attempt 1

```py
numbers = [0, 1, 3, 0, 5, 0, 2]
newList = []

count = 0

for i in numbers:
    if i != 0:
        newList.append(i)
    else:
        count += 1

for j in range(count):
    newList.append(0)

print(newList)
```
**Output**
```bash
[1, 3, 5, 2, 0, 0, 0]
```
> Logic and code took 11 mins

The time complexity of the approacxh is **O(n)**.

---
