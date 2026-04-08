# The Problem - Day 12
> Topic: Strings\
> Level: Beginner

You are given a string. Your task is to check whether the string is a palindrome or not.
A palindrome is a word that reads the same forwards and backwards.
You cannot use any built-in reverse function or slicing shortcut.

## Example:
**Input:**
```py
text = "racecar"
```

**Output**:
```bash
True
```

**Input**:

```py
text = "hello"
```
**Output**:
```bash
False
```


## What you need to think about
You just reversed a string in Day 11. And before that you worked with two pointers in Day 3.

Ask yourself this:
"Do I actually need to build the full reversed string to know if it is a palindrome, or **can I check it more directly by comparing characters from both ends**?"
That question points you toward a cleaner and more efficient solution.

# My approach
## Approach - 1
First store the `string` in a variable as `str1`. Then create a reverse of the string and store in a variable as `str2`. Then check the bith strings are same or not. If not, the string is _not palindrome_. And if yes, means string is _palindrome_.

## Logic - 1
```py
text = "racecar"
rev_text = ""

for i in range(len(text) -1, -1, -1):
    rev_text = rev_text + text[i]

if rev_text == text:
    print("True")
else:
    print("False")
```
**Output**:
```bash
True
```

---

## Approach - 2
Using **Two pointer method** i can find the index from left to right or voice-versa. So without creating a reverse string i can compare the string and check is it palendrome or not?

1. So, the string can be only palendrom if its index of `n` is equals to index of `len(n) - 1`.

2. By comparing its both end at a time can be better approach.

## Logic - 2
```py
text = "a"

left = 0
right = len(text) - 1

result = False

while left < right:
    if text[left] == text[right]:
        result = True

        left += 1
        right -= 1
    else:
        break

print(result)
```

**Output**:
```bash
False
```
---


# What i did wrong?
In this case, we can `text = "a"`, and single character is always `True`. But due to loop condition it never runs and default assumption of `result = False` will never make it correct.

# What to improve
Change the assumption of default as `result = False`. Make it default as `result = True`, and in the else block set `result = False` then break.

## Logic - 3
```py
text = "a"

left = 0
right = len(text) - 1

result = True # Fixed

while left < right:
    if text[left] == text[right]:
        left += 1
        right -= 1

    else:
        result = False # Fixed
        break

print(result)
```

**Output**:
```bash
True
```
---

# Logic: GPT Version without `else`
```py
text = "a"

left = 0
right = len(text) - 1

result = True

while left < right:
    if text[left] != text[right]:
        result = False
        break
    left += 1
    right -= 1

print(result)
```
---