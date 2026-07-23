numbers = [4, 2, -3, 1, 6]
seen = {} # dictionary store sum

result = False # Result
currentSum = 0 # Current sum

# Create map 
for i in numbers:
    # create map 
    currentSum += i

    # if zero occurs
    if currentSum == 0:
        result = True
        break

    # if repetating sum found in seen 
    elif currentSum in seen:
        result = True
        break

    # Add to seen 
    seen[currentSum] = True

# result
print(result)