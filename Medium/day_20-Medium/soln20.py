numbers = [1, 3, 2, 1, 4, 3, 1, 2]
seen = {}

# create map for all numbers
for i in numbers:
    if i not in seen:
        seen[i] = 1
    else:
        seen[i] += 1

# return first number has largets value
l_key = 0
l_val = 0

for key, val in seen.items():
    if val > l_val:
        l_val = val
        l_key = key

print(l_key)