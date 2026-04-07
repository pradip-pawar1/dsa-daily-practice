# The Problem - Day 11
> Topic: Strings\
> Level: Beginner


You are given a string. Your task is to reverse the string without using any built-in reverse function or slicing shortcut like `[::-1]`.

## Example
**Input**:
```py
text = "hello"
```

**Output**:
```bash
"olleh"
```


## What you need to think about
You have already reversed a list in Day 3 using the two-pointer technique. A string is just a sequence of characters.
Ask yourself this:
"Can I apply the **same thinking I used for list reversal** here, keeping in mind that strings in Python are immutable?"

That last part is the new challenge in this problem.

---

# My approach
This is first question of strings. And after lots of brain storming, i took hints form GPT. and he said, i have a `string`, and if i come with last element to first element of list and create new string with the same reverse order then i can achive my desired output.

## Logic: Attempt - 1
```py
text = "hello"

right = len(text) - 1
new_str = ""

for i in text:
    new_str = new_str + text[right]
    right -=1

print(new_str)
```
**Output**
```bash
olleh
```

Output achived.

# Improvement form GPT
As i am using `for i in text`, but not using `i` anywhere. But every thing should have purpose. So use `range()` function.

## Logic: Attempt - 2
```py
text = "hello"

right = len(text) -1
new_str = ""

while right >= 0:
    new_str = new_str + text[right]
    right -= 1

print(new_str)
```

Same output. Insted of using `range()` function i used `while` loop.

**Range Function Example**:
```py
text = "hello"
new_str = ""

for i in range(len(text) - 1, -1, -1):
    new_str = new_str + text[i]
print(new_str)
```
---

