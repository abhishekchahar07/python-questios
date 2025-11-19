s = input()

def check(x):
    # Base case: 0 or 1 length string is always palindrome
    if len(x) <= 1:
        return True
    # If first and last characters differ → not palindrome
    if x[0] != x[-1]:
        return False
    # Recursive call on the middle substring
    return check(x[1:-1])

if check(s):
    print("Palindrome")
else:
    print("Not Palindrome")
