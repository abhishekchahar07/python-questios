# Reverse a string using recursion
# Problem:
#     Write a recursive function to reverse a string.
#
# Input Format:
#     A single string S.
#
# Output Format:
#     Print the reversed string.
#
# Sample Input:
#     hello
#
# Sample Output:
#     olleh

s = input()

def reverse_str(x):
    # Base condition: if string becomes empty, return empty
    if x == "":
        return ""
    # Recursive step: last character + recursion on remaining string
    return reverse_str(x[1:]) + x[0]

print(reverse_str(s))
