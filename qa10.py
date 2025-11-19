# 10. Count digits in a number
#
# Problem:
#     Write a recursive function to count the digits in a number.
#
# Input Format:
#     A single integer N.
#
# Output Format:
#     Print the number of digits.
#
# Sample Input:
#     12345
#
# Sample Output:
#     5

n = int(input())

def count_digits(x):
    # Base case: when number becomes 0, return 0
    if x == 0:
        return 0
    # Recursive case: remove one digit → x // 10
    return 1 + count_digits(x // 10)

# Special case: if input is 0, digits = 1
if n == 0:
    print(1)
else:
    print(count_digits(n))
