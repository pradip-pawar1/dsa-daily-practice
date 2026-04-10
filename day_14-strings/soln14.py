text = "aabbcdeff"
my_dict = {}
result = "" # result

# Loop to find frequency
for i in text:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

# Loop to find first non-repeating character
for i in my_dict:
    if my_dict[i] == 1:
        result = i
        break
    
# check if no-character found non-repeating
if result == "":
    result = None   

print(result)