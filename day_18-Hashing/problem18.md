# The Problem Day 18
> Topic: Strings + Hashing\
> Level: Beginner+\
> Source: GPT\
> Date: 2026-04-16


You are given a string. Your task is to **find the most frequently occurring character in the string and print it along with its count**.
If two characters have the same highest frequency, _print the one that appears first_ in the string.

## Example:
**Input**:
```py
text = "aabbcccdd"
```
**Output**:
```bash
c 3
```

## What you need to think about
You already know how to build a frequency map using a dictionary. You did it in Day 13.

**Ask yourself this**:
"Once I have the frequency of every character, how do I find the one with the highest count while respecting the order of first appearance?"
Take a breath, solve this one, and come back tomorrow fresh for Day 17 explanation.


# My approach
I will create a new dictionary where store all character with their frequency. Then throught second loop, find most larget value and store in a variable with key.

## Logic - 1
```py
text = "aabbcccdd"
freq_map = {}

for i in text:
    if i not in freq_map:
        freq_map[i] = 1
    else:
        freq_map[i] += 1

most_key = ""
most_val = 0

for key, val in freq_map.items():
    if val > most_val:
        most_val = val
        most_key = key
    
print(f"{most_key} : {most_val}")
```
**Output**:
```bash
c : 3
```