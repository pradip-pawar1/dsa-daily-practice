numbers = [1, 3, 5, 7, 9, 11]
target = 12

result = False

left = 0 # left index
right = len(numbers) - 1 # right index

while left < right: # loop
    addition = numbers[left] + numbers[right]

    if addition == target: # check soln
        result = True
        break

    elif addition > target: # if soln is to0 big
        right -= 1

    elif addition < target: # if soln is too small
        left += 1
    
print(result)