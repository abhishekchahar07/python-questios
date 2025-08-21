# Take an integer N as input. Your task is to calculate and print the sum of the digits of the given number N

n = int(input("Enter a positive integer: "))
sum = 0
while n > 0:
    digit = n % 10  
    sum += digit    
    n //= 10  
print("The sum of the digits is:", sum)
