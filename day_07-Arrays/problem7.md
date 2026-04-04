# The problem Day 7
> Topic: Arrays (Python Lists)\
> Level: Beginner+


You are given a list of numbers. Your task is to **remove all duplicates from the list** and print **only the unique numbers**, in the order they first appeared.
You cannot use set() or any built-in deduplication function.

### Example:
**Input:**
```
numbers = [1, 3, 2, 3, 5, 1, 4, 9]
```

**Output:**
```
[1, 3, 2, 5, 4, 9]
```

## What you need to think about
You are walking through the list one element at a time. Ask yourself this:
"_**Before I add a number to my result, how do I check whether I have already seen it before?**_"

---
# My approach
I will create a new empty list as `newList`. Then Start a loop on list, and add a condition to check if current value `i` does already exist in `newList`. If yes then don't add it into `newList` and if not or if `i` is the first occurance in the list the add it to `newList`.

# Attrempt 1
```py
# List of number
numbers = [1, 3, 2, 3, 5, 1, 4, 9]
newList = []

for i in numbers:
    if not i in newList:
        newList.append(i)

print(newList)
```

**Output:**
```bash
[1, 3, 2, 5, 4, 9]
```
---

## Mistake GPT found?
This logic is clane and works well but in the standards of DSA this is cheating. Because i am using auto search feature of python. That is `in`. `in` automatically search each and every element  from list, so in raw programming this is cheating.

I already solved this problem in _**[Day - 4](../day_04-Arrays/problem.md)**_ where i have to find a target element exists in a list or not.

## Improvement I did...
After i found my mistake, i  brainstorm a lost and took some hints also to solve this question. After some time i implemented todays  logic from **`Day-4`**. After 1 hr of strugle i came with this.

### What i learned:
1. How to use nested loops
2. How nested loops works
3. Implemented searching
4. How 1 wrong move can change the result.

And may more, like help me needed some time.

## Attempt 2
```py
numbers = [1, 3, 2, 3, 5, 1, 4, 9]
newList = []

for i in numbers:
    target = i
    result = False
    
    for j in newList:
        if j == target:
            result = True
            break

    if result == False:
        newList.append(target)

print(newList)
```
**Output**
```bash
[1, 3, 2, 5, 4, 9]
```
---