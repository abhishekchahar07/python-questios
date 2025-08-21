a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
c = int(input("Enter number C: "))

if a < b & a < c:
    print("Minimum:", a)
elif  b < c:
    print("Minimum:", b)
else:
    print("Minimum:", c)
