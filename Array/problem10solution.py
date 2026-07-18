numbers = [4, 7, 1, 9, 3, 6]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print(f"Largest : {largest}")
print(f"Smallest : {smallest}")