# Problem:
# Using recursion, print numbers from N to 1.
# Input Format:
# A single integer N.
# Output Format:
# Print numbers from N to 1 separated by a space.
# Sample Input:
# 5
# Sample Output:
# 5 4 3 2 1

n = int(input())

def print_numbers(n):
    if n == 0:
        return
    print(n, end=" ")
    print_numbers(n - 1)

print_numbers(n)
