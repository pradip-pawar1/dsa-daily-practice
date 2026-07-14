def find_max_vowels(string, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    currentVowel = 0

    for char in string[:k]:
        if char in vowels:
            currentVowel += 1

    maxVowels = currentVowel

    for i in range(k, len(string)):
        if string[i] in vowels:
            currentVowel += 1
        if string[i - k] in vowels:
            currentVowel -= 1

        maxVowels = max(currentVowel, maxVowels)
    return maxVowels

max_vowels = find_max_vowels("abciiidef", 3)
print(max_vowels)