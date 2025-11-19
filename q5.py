# write a recursive function to rverse a string
s = input("Enter a string: ")
def r(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + r(s[:-1])
result = r(s)
print(r)