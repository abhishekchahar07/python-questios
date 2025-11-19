#print numbers from 1 to N
#Problem:
#Using recursion, print numbers from 1 to N.
#Input Format:
#A single integer N.
#Output Format:
#Print numbers from 1 to N separated by a space.
#Sample Input:
#5
#Sample Output:
#1 2 3 4 5

n = int(input())
def num(i,n):
    if i > n: 
        return
    print(i, end=" ")
    num(i+1,n)
num(1,n)