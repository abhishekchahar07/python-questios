s = input()
vowel = 0
consonent = 0
for i in s:
    if i in 'aeiouAEIOU':
        vowel += 1
    else:
        consonent += 1
print(vowel)
print(consonent)
   