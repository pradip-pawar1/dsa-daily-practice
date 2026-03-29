numbers = [-9, 9, 3, 1, 8, 9]

max_num = numbers[0]
second_large = numbers[0]

for i in numbers[1:]:
    if i > max_num:
        second_large = max_num
        max_num = i
    elif i > second_large and i != max_num:
        second_large = i

print(f"Largest: {max_num}")
print(f"Second largest: {second_large}")