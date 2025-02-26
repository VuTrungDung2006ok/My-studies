n = int(input())
s = 0
d = 1
while s <= n:
    s += 1/d
    d += 1

print(d-1)