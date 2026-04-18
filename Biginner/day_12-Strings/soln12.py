# text = "12"

# left = 0
# right = len(text) - 1

# result = True # Fixed

# while left < right:
#     if text[left] == text[right]:
#         left += 1
#         right -= 1

#     else:
#         result = False # Fixed
#         break

# print(result)

text = "ab"

left = 0
right = len(text) - 1

result = True

while left < right:
    if text[left] != text[right]:
        result = False
        break
    left += 1
    right -= 1

print(result)