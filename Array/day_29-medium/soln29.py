def longest_length(arr, target):
    left = 0
    total = 0
    result = 0

    for right in range(len(arr)):
        total += arr[right]  # always expand first

        if total > target:   # shrink if exceeded
            total -= arr[left]
            left += 1

        if total == target:  # record if equal
            result = max(result, right - left + 1)

    return result

# Attempt 1
# def longest_length(arr, target):
#     left = 0
#     sum = 0
#     result = 0

#     for right in range(len(arr)):
#         sum += arr[right]

#         while sum == target:
#             window_len = right - left + 1

#             if result < window_len:
#                 result = window_len
#             sum -= arr[left]
#             left += 1

#     return result

print(longest_length([1, 2, 3, 1, 1, 1], 6))
print(longest_length([1, 2, 3, 7, 1], 6))
print(longest_length([1, 2, 3, 4, 5], 3))
print(longest_length([2, 1, 2, 3, 1, 1, 1], 6))