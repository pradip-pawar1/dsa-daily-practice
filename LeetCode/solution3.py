class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        
        best_profit = 0
        min_price = prices[0]

        for price in prices:
            profit = price - min_price

            if profit > best_profit:
                best_profit = profit

            if price < min_price:
                min_price = price

        return best_profit


# Test 
test_case = [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0),
    ([7, 6, 4, 3, 1], 0),
    ([1, 5], 4),         # Profit possible
    ([5, 1], 0),         # Loss/No profit
    ([5], 0),
    ([], 0),
    ([3, 3, 3, 3], 0),
    ([2, 10, 1, 3], 8),
    ([100, 80, 60, 40, 1], 0),
    ([2, 4, 1, 7], 6),   # Buy at 1, Sell at 7 -> 6 (Better than Buy at 2, Sell at 4 -> 2)
    ([1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 8),  # Buy at 1, Sell at 9 -> 8
]

sol = Solution()

for arr, expected in test_case:
    actual = sol.maxProfit(arr)
    passed = actual == expected
    status = "PASSED" if passed else "FAILED"

    print(f"[{status}] Input: {arr} | Expected: {expected} | Got: {actual}")