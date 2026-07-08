# Sliding window technique
def max_sum(arr:list, k:int):
    # Time complexity = O(n)

    n = len(arr)

    # if array is less that subarray
    if n < k:
        return 0
    
    windowSum = sum(arr[:k]) # Sum of k
    maxSum = windowSum # Max sum
    # sliding window
    for i in range(k, n):
        windowSum = windowSum + arr[i] - arr[i - k]
        maxSum = max(maxSum, windowSum)

    return maxSum

numbers = [2, 1, 5, 1, 3, 2]
k = 3
# numbers = [1, 1, 1, 1, 1]
# k = 2
print(max_sum(numbers, k))