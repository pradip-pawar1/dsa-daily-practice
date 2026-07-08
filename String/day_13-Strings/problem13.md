# The Problem Day 13
> Topic: Strings\
> Level: Beginner+


You are given a string. Your task is to **count the frequency of each character** in the string and print each character along with its count.

## Example:
**Input**:
```py
text = "hello"
```

**Output**:
```bash
h 1
e 1
l 2
o 1
```

## What you need to think about
You have counted occurrences of a number in a list before in Day 5. But here you have multiple characters and you need to track all of them at once.

Ask yourself this:

"_What data structure allows me to store a character and its count together_, and update it as I walk through the string?"

# My appraoch
The only data structure in python allows **`key <=> Values`** is **Dictionary**. I have to create a dictionary and create a vale as `string[i]` if `i` is new occurance. And initialize its value with `1` in first iteration as it occurs. Then through the repetation i have to increment the values, of a `key`.

## Logic - 1
```py
text = "hello"
my_dict = {}

for i in text:
    # if not i in my_dict:
    if i not in my_dict: # Improved
        my_dict[i] = 1

    else:
        my_dict[i] += 1

# For pretty output only
for key, value in my_dict.items():
    print(f"{key} : {value}")
```

**Output**:
```bash
h : 1
e : 1
l : 2
o : 1
```
