#reverse number
n = 123
for i in range(1, 4):
    j=n%10
    n = n // 10
    print(j, end="") 
    