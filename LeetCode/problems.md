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
