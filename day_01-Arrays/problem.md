# The Problem: Day 1
>## Topic: Arrays (Python Lists)
You are given a list of numbers. Your task is to find and print the largest number in that list.
You cannot use any built-in function like max(). You have to find it manually using logic.

## Example:
Input:
```
numbers = [3, 7, 1, 9, 4, 6]
```

Output:
```
9
```

## What you need to think about
Ask yourself this one question before writing any code:
"If I were checking this list by hand, one number at a time, how would I remember which number is the biggest so far?"
That one question contains the entire logic of this problem.

---


# My approch
I have list of munbers as array.
E.x, 
```
numbers = [3, 7, 1, 9, 4, 6]
```
I'll Initialize a variable as `max_num = 0`.
Then run a for loop on `numbers`. Inside for loop check current number, if current number is `>` `max_num` then `max_num` is currnt number. Else, the current number is `<` `max_num` then `max_num` remain as it is.

## Attempt 1
```
numbers = [3, 7, 10, 9, 4, 6]

max_num = 0

for i in numbers:
    if i > max_num:
        max_num = i
```

---

# Improvement form GPT:
You initialized `max_num = 0`.

Think about this carefully. What happens if the input list is this:
```
numbers = [-5, -3, -8, -1]
```
Walk through your code mentally. What will max_num be at the end? Is that correct? Now ask yourself: why did you choose 0 specifically? 

What were you assuming about the list when you wrote that?
That assumption is the mistake. And fixing it requires you to think about where the initial value of max_num should actually come from, **not from your imagination, but from the list itself**.

---

# What I did wrong?
I am initializing `max_num = 0` but if number of list is in negative then it never changer because 0 will always bigger, there my condition fails.

# What I changed?
Now, I am assuming that the first occurance of the list or frst element of the list is largest, E.x, `max_num = numbers[0]`. 
Then by traversing throught `for loop` I will check every element and change when the bigger number occurs.

## Attempt 2
```
numbers = [3, 7, 10, 9, 4, 6]

max_num = numbers[0]

# running a for loop
for i in numbers:
    if i > max_num:
        max_num = i

print(f"Gratest number is: {max_num}")
```
---