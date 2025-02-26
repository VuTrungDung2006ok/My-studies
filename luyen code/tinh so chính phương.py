l, r = map(int, input().split())
d = 0
for j in range(l, r + 1):
    if (int(j**0.5) ** 2) == j:
        d += 1
print(d)