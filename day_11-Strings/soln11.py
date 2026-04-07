text = "hello"

right = len(text) -1
new_str = ""

# while loop approach
while right >= 0:
    new_str = new_str + text[right]
    right -= 1

print(f"While loop: {new_str}")

# For loop approach
new_text = ""

for i in range(len(text) - 1, -1, -1):
    new_text = new_text + text[i]

print(f"For loop: {new_text}")