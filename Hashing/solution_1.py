a = "listen"
b = "silent"

dict_1 = {}
dict_2 = {}

result = True

if len(a) == len(b):
    # create frequency map 
    for i in a:
        if i not in dict_1:
            dict_1[i] = 1
        else:
            dict_1[i] += 1

    for j in b:
        if j not in dict_2:
            dict_2[j] = 1
        else:
            dict_2[j] += 1
else:
    result = False

# check the dicts
for key, val in dict_1.items():
    if key not in dict_2:
        result = False
        break
    elif dict_2[key] != val:
        result = False
        break

print(result)