nums = [1, 12, -5, -6, 50, 3]
k = 4

def max_average(arr, k):
    # Build first window 
    currentWindow = sum(arr[:k])
    maxWindow = currentWindow

    # Start moving
    for i in range(k, len(arr)):
        # add new element and subtract last Element
        currentWindow = currentWindow + arr[i] - arr[i - k]
        # update maxWindow
        maxWindow = max(maxWindow, currentWindow)

    return maxWindow/k

avg = max_average([1, 12, -5, -6, 50, 3], 4)
print(avg)
