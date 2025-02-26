import math

so = int(input())
n = list(map(int,input().split()))
be = []
lon = []
kq = []
for i in range(len(n)):
    if n[i] == min(n):
        be.append(i+1)
    elif n[i] == max(n):
        lon.append(i+1)

for b in be:
    for l in lon:
        kq.append(abs(b-l)+1)

print(min(kq))