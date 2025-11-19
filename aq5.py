# Problem:
# Write a recursive function to find the Nth Fibonacci number.
#
# Input Format:
# A single integer N.
#
# Output Format:
# Print the Nth Fibonacci number.
#
# Sample Input:
# 6
#
# Sample Output:
# 8

n = int(input())

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(n))
