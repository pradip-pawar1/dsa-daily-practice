# text = "the quick brown fox"
text = "the quick brown elephant"

word = "" # empty word
count = 0 # to measure frequency

seenKey = "" # answer
seenVal = 0 # frequency of ans
seen = {} # map

for i in text:
    # if no space in text
    if " " not in text:
        seenKey = text
        break
    
    elif i == " ":
        seen[word] = count
        count = 0
        word = ""
    
    else:
        word += i
        count += 1
    
seen[word] = count

for key, val in seen.items():
    if val > seenVal:
        seenVal = val
        seenKey = key

print(seenKey)