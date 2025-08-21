# Take an integer N as input and print the count of digits of that number

n = int(input("Enter a positive integer: "))
count= 0
while n > 0:
    n //=10
    count += 1
print("The count of digits is:", count) 