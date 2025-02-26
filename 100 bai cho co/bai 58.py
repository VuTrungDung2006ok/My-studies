import math
L = list(map(int,input().split()))
x = int(input())
c = max(L)
b = min(L)
if abs(c-x) > abs(b-x):
    print(c)
else:
    print(b)
