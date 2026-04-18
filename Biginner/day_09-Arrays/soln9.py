numbers = [1, 3, 4, 5, 2, 7, 8, 6, 10]
n = len(numbers) + 1

expected_sum = n * (n + 1) / 2
sumNums = 0

for i in numbers:
    sumNums += i

missing = expected_sum - sumNums
print(missing)