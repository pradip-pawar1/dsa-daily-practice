class Solution(object):
    def sortedSquares(self, nums:int):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squaredArray = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        idx = len(nums) - 1

        while left <= right:
            sqr_left = nums[left] ** 2
            sqr_right = nums[right] ** 2

            if sqr_left > sqr_right:
                squaredArray[idx] = sqr_left
                left += 1

            else:
                squaredArray[idx] = sqr_right
                right -= 1

            idx -= 1
        return squaredArray

test_case = [
    ([-4,-1,0,3,10], [0,1,9,16,100]),
    ([-7,-3,2,3,11], [4,9,9,49,121])
]

sol = Solution()

for arr, expArr in test_case:
    actual = sol.sortedSquares(arr)
    passed = actual == expArr
    status = "Pass" if passed else "Fail"

    print(f"Passed Arr: {arr} | Expacted: {expArr} | Result: {status}")