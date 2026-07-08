# a = "abcdef"
# b = "bdfxyz"

a = "aabbcc"
b = "abcabc"

aSeen = {} # map of a
bSeen = {} # map of b

count = 0 # result

# Create map of a 
for i in a:
    if i not in aSeen:
        aSeen[i] = True

# create map of b    
for i in b:
    if i not in bSeen:
        bSeen[i] = True

# find reslut         
for j in aSeen:
    if j in bSeen:
        count += 1

print(count) # show result