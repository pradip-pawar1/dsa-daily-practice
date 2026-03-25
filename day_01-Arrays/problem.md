# The Problem
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