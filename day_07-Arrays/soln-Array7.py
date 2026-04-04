numbers = [1, 3, 2, 3, 5, 1, 4, 9]
newList = []

for i in numbers:
    target = i
    result = False
    
    for j in newList:
        if j == target:
            result = True
            break

    if result == False:
        newList.append(target)

print(newList)