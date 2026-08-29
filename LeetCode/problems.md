# LeetCode Problems
## The problem - Day 01

> Topic: Hashing\
> Name: Contains Duplicate\
> Level: Easy\
> Source: [LeetCode #217](https://leetcode.com/problems/contains-duplicate/description/)\
> Date: 27 Aug 2026

### Problem Statement

Given an integer array nums, return True if any value appears at least twice in the array, and return False if every element is distinct.

### Solution
**Local File**: [Answer](solution1.py)\
**LeetCode File** [Details](https://leetcode.com/submissions/detail/2122141471/)

1. Create an empty `dict` _my_dict_. 
2. Run a for loop on numbers.
3. If current number `i` already exists in _my_dict_ return `True`.
4. If current number `i` does not found in _my_dict_, then return defalut value as  `False`.

---

## The problem - Day 02

> Topic: Two Pointer\
> Name: Valid Palindrome\
> Level: Easy\
> Source: [LeetCode #125](https://leetcode.com/problems/valid-palindrome/description/)\
> Date: 28 Aug 2026

### Problem Statement
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward.
 Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a **palindrome**, or `false` otherwise.

**Example 1**:
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

**Example 2**:
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

### Solution
**Local file**: [Answer](solution2.py)\
**LeetCode file**: [Details](https://leetcode.com/submissions/detail/2122630199/)
1. Convert the `str` to lower case using `str.lower()` method
2. Using `re` module remove all **non-alphanumeric characters** : `re.sub(r"[^a-z0-9]", "", str)`
3. Using two pointer approach compare the string
    - Return `True` if both pointer match properly
    - Return `False` if pointer values fail

---

## The problem - Day 03

> Topic: Sliding Window\
> Name: Best Time to Buy and Sell Stock\
> Level: Easy\
> Source: [LeetCode #121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)\
> Date: 29 Aug 2026

### Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the $i^{\text{th}}$ day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

_Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return_ `0`.

### Solution
**Local file**: [Answer](solution3.py)\
**LeetCode file**: [Details](https://leetcode.com/submissions/detail/2123583769/)

1. Create a variable `min_price = arr[0]` to store minimum buy price
2. Create a variable `best_profit = 0` to save final biggert profit
3. Run a `for` loop on **stocks**
4. Current value `i` is the sell price.
    - Calculate profit: $profit = buy\ price - see\ price$
    - Check best profit
    - Check smallest buy price
5. retuen `best_profit`