#write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as  input from use


n = int(input("Enter a positive integer: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print(" the sum of these number is :", sum)
    
