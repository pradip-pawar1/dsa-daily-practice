# The Problem - Day 25

> Topic: Strings\
> Name: Longest Word in a Sentence\
> Level: Medium\
> Source: Claude\
> Date: 2026/04/24


## The Problem
You are given a sentence as a string. Your task is to **find and print the longest word in the sentence**.
If two words have the same length, print the one that appears first.
You cannot use `split()` or any _built-in string splitting function_. You have to extract words manually.

### Example 1 - Valid Case:
**Input**:
```py
text = "the quick brown fox"
```
**Output**:
```bash
quick
```

> Because quick and brown both have 5 characters but quick appears first.

### Example 2 - Single Word:
**Input**:
```py
text = "hello"
```
**Output**:
```bash
hello
```
> Because there is only one word.

## What you need to think about
You cannot use split(). So you need to build words yourself character by character as you walk through the string.
**Ask yourself this**:

How do I know when a word starts and when it ends as I 
walk through the string one character at a time?


# My approach
I know that a word starts when `<space>` ends and ends when just before `<space>` occurs. 

I will loop throught the `text` or `string`. Then for each character `i` i will encounter is considered as a `char` of a word untill i found a `<space>`. And thet `char` `i`, will be appended to a variable `word`.

When i found a `<space>`, i will append the current word to a `dict`, with its frequency. And **reset** the `word` and it's frequency `count`. 

If i will found any single word then its is the final solution.

## Logic - 1

```py
text = "the quick brown fox"

word = "" # empty word
count = 0 # to measure frequency

seenKey = "" # answer
seenVal = 0 # frequency of ans
seen = {} # map

for i in text:
    # if no space in text
    if " " not in text:
        seenKey = text
        break
    
    elif i == " ":
        seen[word] = count
        # reset
        count = 0
        word = ""
    
    else:
        word += i
        count += 1

for key, val in seen.items():
    if val > seenVal:
        seenVal = val
        seenKey = key

print(seenKey)
```
**Output**:
```bash
quick
```


## Mistake and Improvement
There is one bug hiding in your code.
Your loop builds words and adds them to `seen` when it encounters a `space`. But what happens to the last word in the sentence?

`"the quick brown fox"` ends with `"fox"` and there is no space after it. So `"fox"` never gets added to seen. In this example it does not affect the output because `"fox"` is not the longest word. But try this:

```py
text = "the quick brown elephant"
```

Your code will miss `"elephant"` entirely. Trace through and confirm.

## Logic - 2

```py
text = "the quick brown elephant"

word = "" # empty word
count = 0 # to measure frequency

seenKey = "" # answer
seenVal = 0 # frequency of ans
seen = {} # map

for i in text:
    # if no space in text
    if " " not in text:
        seenKey = text
        break
    
    elif i == " ":
        seen[word] = count
        count = 0
        word = ""
    
    else:
        word += i
        count += 1
    
seen[word] = count

for key, val in seen.items():
    if val > seenVal:
        seenVal = val
        seenKey = key

print(seenKey)
```
**Outtput**:
```bash
elephant
```