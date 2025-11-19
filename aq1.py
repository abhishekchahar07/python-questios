#Sum of first N natural numbers
#Problem:
#Write a recursive function to find the sum of the first N natural numbers.
#Input Format:
#A single integer N.
#Output Format:
#Print the sum of the first N natural numbers.
#Sample Input:
#5
#Sample Output:
#15


n = 5
def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)
print(sum(n))
