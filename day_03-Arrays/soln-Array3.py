numbers = [1,2,3,4,5, 6,7,8]

left = 0
right = len(numbers) -1 

while left < right:
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

    left +=1
    right -=1

print(numbers)