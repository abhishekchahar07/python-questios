A = input()
B = int(input())

ch = chr(B)  

if ch in A:
    print(A.index(ch))
else:
    print(-1)

