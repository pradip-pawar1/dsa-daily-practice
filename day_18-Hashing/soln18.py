text = "aabbcccdd"
freq_map = {}

for i in text:
    if i not in freq_map:
        freq_map[i] = 1
    else:
        freq_map[i] += 1

most_key = ""
most_val = 0

for key, val in freq_map.items():
    if val > most_val:
        most_val = val
        most_key = key
    
print(f"{most_key} : {most_val}")