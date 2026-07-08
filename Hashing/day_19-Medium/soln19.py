numbers = [100, 4, 200, 1, 3, 2]
seen = {}

# Step 1: Store all numbers in seen
for i in numbers:
    seen[i] = True

longest = 0

# Step 2: Find sequence starts and count
for i in numbers:
    if (i - 1) not in seen:  # i is a start
        current = i
        length = 1
        
        # Step 3: Count forward
        while (current + 1) in seen:
            current += 1
            length += 1
        
        # Step 4: Update longest
        if length > longest:
            longest = length

print(longest)