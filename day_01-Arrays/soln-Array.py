# list of numbers as array
numbers = [3, 7, 10, 9, 4, 6]

# assign max_num
max_num = 0
# running a for loop
for i in numbers:
    if i > max_num:
        max_num = i

print(f"Gratest number is: {max_num}")