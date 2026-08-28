import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # transform string 
        s = s.lower()
        s = re.sub(r"[^a-z0-9]", "", s)

        # Compare strings
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True     

sol = Solution()

test_case = [
    "A man, a plan, a canal: Panama",
    "race a car",
    " ",
    "0P"
    "A1b22b1a",
    "!!!:,$",
    "123456"
]

for test in test_case:
    result = sol.isPalindrome(test)
    print(f"Input: {test} | Output: {result}")