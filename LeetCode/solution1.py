class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_dict = {}

        for i in nums:
            if i in my_dict:
                return True

            my_dict[i] = True
        return False

test_case = [
    [1,2,3,1],
    [1,2,3,4],
    [1,1,1,3,3,4,2,4,2]
]

sol = Solution()

for test in test_case:
    result = sol.containsDuplicate(test)
    print(f"Input : {test} | Output : {result}")