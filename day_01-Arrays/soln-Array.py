# list of numbers as array
numbers = [-3, -7, -10, -9, -1, 0]

# taking number from list
max_num = numbers[0]

# running a for loop
for i in numbers:
    if i > max_num:
        max_num = i

print(f"Gratest number is: {max_num}")