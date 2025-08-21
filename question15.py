marks = int(input("entr apne marks: "))
if marks < 25:
    print("D")
elif marks > 25 & marks <45:
    print("C")
elif marks > 45 & marks < 65:
    print("B")
elif marks > 65 & marks < 85:
    print("A")
elif marks > 85:
    print("A+")
else:
    print("Invalid marks entered.")