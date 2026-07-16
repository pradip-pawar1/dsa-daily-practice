def find_small_length(arr, target):
    left = 0
    total = 0
    result = float('inf')

    # move right pointer 
    for right in range(len(arr)):
        total += arr[right]

        while total > target:
            window_len = right - left + 1
            if result > window_len:
                result = window_len
            total -= arr[left]
            left += 1

    return result
      
print(find_small_length([2,1,5,2,3,2], 7)) # output 3
print(find_small_length([2,5, 3, 7, 9, 2, 3], 6)) # output 1
print(find_small_length([2,5, 3, 7, 9, 2, 3], 15)) # output 2

