numbers = [0, 1, 3, 0, 5, 0, 2]
newList = []

count = 0

for i in numbers:
    if i != 0:
        newList.append(i)
    else:
        count += 1

for j in range(count):
    newList.append(0)

print(newList)
