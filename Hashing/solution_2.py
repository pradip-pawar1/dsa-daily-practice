numbers = [1, 3, 2, 3, 5, 1, 4, 2, 2]
my_dict = {}
new_lst = []


for i in numbers:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

for key, val in my_dict.items():
    if val > 1:
        new_lst.append(key)

print(new_lst)