# Sum of digits of a number
# Problem:
#    Find the sum of the digits of a given number using recursion.
#
# Input Format:
#    A single integer N.
#
# Output Format:
#    Print the sum of its digits.
#
# Sample Input:
#    1234
#
# Sample Output:
#    10

n = int(input())

def sum_digits(n):
    # Base condition: If number is 0, return 0
    if n == 0:
        return 0
    # Recursive step: last digit + recursion on remaining number
    return (n % 10) + sum_digits(n // 10)

print(sum_digits(n))
