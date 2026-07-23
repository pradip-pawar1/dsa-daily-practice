def remove_duplicate(arr):
    slow = 0 
    # fast = 1 

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1

arr = [1, 1, 2, 3, 3, 4, 5, 5]
arr2 = [1, 1, 1, 1]

count1 = remove_duplicate(arr)
count2 = remove_duplicate(arr2)

print(arr[:count1])
print(arr2[:count2])

# if slow & fast are equal = move fast
# if slow & fast are not equal = move slow & copy fast