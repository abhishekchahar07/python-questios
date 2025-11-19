# 9. Power of a number (x^n)
#
# Problem:
#     Write a recursive function to find x raised to the power n.
#
# Input Format:
#     Two integers x and n are separated by a space.
#
# Output Format:
#     Print the value of x^n.
#
# Sample Input:
#     2 5
#
# Sample Output:
#     32

x, n = map(int, input().split())

def power(a, b):
    # Base case: anything to power 0 is 1
    if b == 0:
        return 1
    # Recursive case: a * a^(b-1)
    return a * power(a, b - 1)

print(power(x, n))
