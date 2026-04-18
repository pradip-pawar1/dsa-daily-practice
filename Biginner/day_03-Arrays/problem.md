# The problem: Day 3
## Topic: Arrays (Python Lists)

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
The list has a beginning and an end. Ask yourself this:
"If I have to swap elements from both sides and move inward, how far do I go before I stop?"
That one question holds the entire logic.

---

# My approch
> **I need to take hints from GPT to solve this question**. I was blank for almost 1 hr. But after a small hint i got the logic.

First, i have to find the length of the list/array, which can be done by `len(numbers)`. Because, The list have 2 ends. From right to left and left to right and also has a center point. So I'll create a condition where loop will stop at middle.

Then inside loop I'll create a `temp` variable to store current number for left side, then I'll put the last number at that index point at left and then `temp` value at last.

Then increase the value of `left` and `right` by 1.

# Attempt 1
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
