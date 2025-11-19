a = input()
a = a + a
a = ''.join(ch for ch in a if not ch.isupper())
for v in 'aeiou':
    a = a.replace(v, '#')
print(a)
