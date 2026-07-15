def replace_i(arr, k):
    replaced_arr = []
    n = len(arr)

    # Baseline for index 0
    current_window = sum(arr[1:k + 1])
    replaced_arr.append(current_window)

    # slide for remening index
    for i in range(1, n):
        if i + k < n:
            current_window += arr[i + k]
            
        current_window -= arr[i]

        replaced_arr.append(current_window)

    return replaced_arr

new_arr = replace_i([1,2,3,4], 2)
print(new_arr)