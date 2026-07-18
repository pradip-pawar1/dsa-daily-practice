# Problem 1: Day 1
> Topic: Arrays (Python Lists)\
> Name: Find the largest number\
> Level: Easy\
> Source: Claude\
> Date: 2026-03-28\
> Code File: [Click Here](problem1solution.py)


## The problem
You are given a list of numbers. Your task is to **find and print the largest number** in that list.
You cannot use any built-in function like `max()`. You have to find it manually using logic.

## Example:
**Input**:
```py
numbers = [3, 7, 1, 9, 4, 6]
```

**Output**:
```bash
9
```

## What you need to think about
**Ask yourself this**: one question before writing any code:
"If I were checking this list by hand, one number at a time, how would I remember which number is the biggest so far?"

---

# My approch - Problem 1
I have list of munbers as array.
E.x, 
```py
numbers = [3, 7, 1, 9, 4, 6]
```
I'll Initialize a variable as `max_num = 0`.
Then run a for loop on `numbers`. Inside for loop check current number, if current number is `>` `max_num` then `max_num` is currnt number. Else, the current number is `<` `max_num` then `max_num` remain as it is.

## Attempt 1
```py
numbers = [3, 7, 10, 9, 4, 6]

max_num = 0

for i in numbers:
    if i > max_num:
        max_num = i
```

---

## Improvement form GPT:
You initialized `max_num = 0`.

Think about this carefully. What happens if the input list is this:
```py
numbers = [-5, -3, -8, -1]
```

What were you assuming about the list when you wrote that?
That assumption is the mistake. And fixing it requires you to think about where the initial value of max_num should actually come from, **not from your imagination, but from the list itself**.

---

## Code
```py
numbers = [3, 7, 10, 9, 4, 6]

max_num = numbers[0]

# running a for loop
for i in numbers:
    if i > max_num:
        max_num = i

print(f"Gratest number is: {max_num}")
```

**Output**
```bash
Gratest number is: 0
```
---

# Problem 2 - Day 2
> Topic: Arrays (Python Lists)\
> Name: Find the second largest number\
> Level: Easy\
> Source: Claude\
> Date: 2026-03-29\
> Code File: [Click Here](problem2solution.py)

## The problem
You are given a list of numbers. Your task is to **find the second largest number** in that list.
You cannot use `max()`, `sort()`, or any built-in shortcut. Pure logic only.

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
**Ask yourself this**:
"While I am tracking the largest, what else can I track at the same time that would give me the second largest?"

---


# My approch

As I already know, how to find largest number for list or array. I'll use the same approch to track second largest number. Like; I have list of nunbers as array. 

I'll Initialize a variable as `max_num = 0`, and `second_large = 0`.
Then run a for loop on `numbers`. Inside for loop check current number, if current number is `>` `max_num` then `max_num` is currnt number.And before initilaizing **current largest number to `max_num`**, first add it to `second_large` then current number = `max_num`. Else, the current number is `< max_num` then `max_num` and `second_large` remain as it is.

## Code
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

## What I did wrong?
1. I am initializing `max_num` and `second_large` as 0 but for some specific condition it fails.
2. I am  not handling a case where second largest number is less that `max_num` but still grater that last `second_large`.

## What I changed?
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

# Problem 3 - Day 3

> Topic: Arrays (Python Lists)\
> Name: Reverse the list\
> Level: Easy\
> Source: Claude\
> Date: 2026-03-30\
> Code File: [Click Here](problem3solution.py)

## The problem
You are given a list of numbers. Your task is to reverse the list without using any built-in reverse function or slicing shortcut like `[::-1]` or `.reverse()`.

### Example:

**Input:**
```py
numbers = [1, 2, 3, 4, 5]
```
**Output:**
```bash
[5, 4, 3, 2, 1]
```

---

## What you need to think about
**Ask yourself this**:
"If I have to swap elements from both sides and move inward, how far do I go before I stop?"
That one question holds the entire logic.

---

# My approch
> I was blank for almost 1 hr. But after a small hint i got the logic.

First, I have to find the length of the `list/array`, which can be done by `len(numbers)`. Because, The list have 2 ends. From right to left and left to right and also has a center point. So I'll create a condition where loop will stop at middle.

Then inside loop I'll create a `temp` variable to store current number for left side, then I'll put the last number at that index point at left and then `temp` value at last.

Then increase the value of `left` and `right` by 1.

# Code
```py
numbers = [1, 2, 3, 4, 5]

left = 0
right = len(numbers) -1 

while left < right:
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

    left +=1
    right -=1

print(numbers)
```

**Output**
```bash
[5, 4, 3, 2, 1]
```
---

> I also figured it out that this technique is known as **Two pointer technique**, an this will ofently appears in DSA.
---


# Problem 4 - Day 4

> Topic: Arrays (Python Lists)\
> Name: Check number exists in a list?\
> Level: Easy\
> Source: Claude\
> Date: 2026-03-31\
> Code File: [Click Here](problem4solution.py)

## The problem
You are given a list of numbers. Your task is to find whether a **given number exists in the list or not**, without using the `in` keyword or any built-in search function.
Print True if found, False if not.

### Example:
**Input:**
```py
numbers = [4, 7, 2, 9, 1]
target = 7
```
**Output:**
```bash
True
```

## What you need to think about
You need to walk through the list yourself and check each element one by one.
**Ask yourself this**:
"At what point do I stop searching, and what do I report if I never find it?"

---
# My approach
First i create a variable as `result = False` to store the result. Then I am using simple for loop `for i in list`, where I stores the current iterable element for the list.
Then I'll compare current iterable `i` with target value as `if i == target`. If this condition is true the change the result to `result = True`. And once found the target then break the loop. And print the result.

---
## Code
```py
numbers = [4, 7, 2, 9, 1]
target = 7

result = False

for i in numbers:
    if i == target:
        result = True
        break

print(result)
```

**Output**
```bash
True
```
> Logic is to the point and the Method is known as **Linear search**.
---

# Problem 5 - Day 5
> Topic: Arrays (Python Lists)\
> Name: How many times a given number appears\
> Level: Easy\
> Source: Claude\
> Date: 2026-04-01\
> Code File: [Click Here](problem5solution.py)

## The problem
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
**Ask yourself this**:
"Instead of stopping when I find the target, what should I do every time I find it?"
That one shift in thinking is all you need.

---
# My approach
I'll iterate a list through for loop, and create a variable `count = 0` and each time when I found the `target` number I'll increase the value of `count` by 1.

---
## Code
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

# Problem 6 - Day 6
> Topic: Arrays (Python Lists)\
> Name: Find sum of all even numbers\
> Level: Easy\
> Source: Claude\
> Date: 2026-04-02\
> Code File: [Click Here](problem6solution.py)

## The problem
You are given a list of numbers. Your task is to find the **sum of all even numbers in the list**.
You cannot use sum() or any built-in function.

## Example:
**Input:**
```py
numbers = [1, 2, 3, 4, 5, 6]
```

**Output:**
```bash
12
```
---


## What you need to think about
**Ask yourself this**:
"How do I know if a number is even, and what do I do with it when it is?"

# My appraoch.
To iterate the list i will use `for` loop. I will make a variable as `sum = 0` and inside for loop i'll add a condition to check, weather the curret number `i` is even or not? If it's odd then let it go but if it's even then add current number `i` to `sum` as `sum += i`. 

## Code
```py
numbers = [1, 2, 3, 4, 5, 6]
total = 0

for i in numbers:
    if i%2 == 0:
        total += i
    
print(total)
```

**Output**
```bash
12
```
---

# Problem 7 - Day 7
> Topic: Arrays (Python Lists)\
> Name: Find sum of all even numbers\
> Level: Easy\
> Source: Claude\
> Date: 2026-04-04\
> Code File: [Click Here](problem7solution.py)

## The problem

You are given a list of numbers. Your task is to **remove all duplicates from the list** and print **only the unique numbers**, in the order they first appeared.
You cannot use `set()` or any built-in deduplication function.

### Example:
**Input:**
```py
numbers = [1, 3, 2, 3, 5, 1, 4, 9]
```

**Output:**
```bash
[1, 3, 2, 5, 4, 9]
```

---
# My approach
I will create a new empty list as `newList`. Then Start a loop on list, and add a condition to check if current value `i` does already exist in `newList`. If yes then don't add it into `newList` and if not or if `i` is the first occurance in the list the add it to `newList`.

# Attrempt 1
```py
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

## Mistake & Improvement?
This logic is clane and works well but in the standards of DSA this is cheating. Because i am using auto search feature of python. That is `in`. `in` automatically search each and every element  from list, so in raw programming this is cheating.

**Solution**: After finding the mistake, I brainstorm a lost and took some hints also to solve this question. After some time i implemented todays  logic from [Day-4](problem4solution.py). After 1 hr of strugle i came with this.

## Code
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

# Problem 8 - Day 8
> Topic: Arrays (Python Lists)\
> Name: Move all zeros to end\
> Level: Easy\
> Source: Claude\
> Date: 2026-04-04\
> Code File: [Click Here](problem8solution.py)

## The problem
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

## Code

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
The time complexity of the approacxh is **O(n)**.

---

# Problem 9 - Day 9
> Topic: Arrays (Python Lists)\
> Name: Find missing number\
> Level: Easy-Medium\
> Source: Claude\
> Date: 2026-04-05\
> Code File: [Click Here](problem9solution.py)

## The problem
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
"**If I know the total sum of numbers from 1 to n**, and I know the sum of what is actually in the list, what does the difference tell me?"

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

# Problem 10 - Day 10
> Topic: Arrays (Python Lists)\
> Name: Find missing number\
> Level: Easy-Medium\
> Source: Claude\
> Date: 2026-04-06\
> Code File: [Click Here](problem10solution.py)

## The problem
You are given a list of numbers. Your task is to **find the largest and smallest number at the same time in a single loop pass**.
You cannot use `max()`, `min()`, or any built-in function.

## Example
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
"**Can I track two things simultaneously inside one single loop?**"

That is the entire challenge.

---

# My approach
I will use 2 condition in a same loop. First I'll create 2 variables as `largest = list[0]` and `smallest = list[0]`, both initialize with **first element of the list**. 

When i start a `for loop`, inside i have 2 conditions:
1. As `if i > largest`
2. As `if i < smallest`

When `if i > largest` will execuated, then change the value of `largest` with `i`. And when `if i < smallest` then change the value of `smallest` with `i`.

Make sure that both condition can't be execuated. And both cannot be true at once. 

**Example**: If `i = 4`and `largest & smallest = 4`, not both condition will faile. But if `largest & smallest = 4` and `i = 7`, then one `if` condition will execuate and secodn will faile by default. Same when `i = 1` then `if` will not execuated, as it failse by default. But smallest will change.

## Code

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
---

