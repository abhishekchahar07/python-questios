# 1.sing recursion print numbers from n to 1
def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)
    

n = int(input())
print_numbers(n)
