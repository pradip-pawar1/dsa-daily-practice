numbers = [2, 3, 4, 3, 2]
seen = {}
result = -1

for i in numbers:
    if i in seen:
        result = i
        break

    seen[i] = True

print(result)