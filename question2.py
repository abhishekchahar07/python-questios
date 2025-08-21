a = int(input("Enter a number: "))
c=0
while a > 0:
    digit = a % 10
    c = c + 1
    a //= 10
print(c)