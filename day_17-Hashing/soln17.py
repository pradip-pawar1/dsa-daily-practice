numbers = [2, 7, 4, 1, 9]
target = 11

seen = {}
result = False

for i in numbers:
    complement = target - i

    if complement in seen:
        result = True
        break

    seen[i] = True

print(result)
print(seen)