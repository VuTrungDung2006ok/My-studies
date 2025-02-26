n = int(input())
ai = list(map(int,input().split()))
s = int(input())
b = []
tong = 0
for i in range(len(ai)):
    tong +=ai[i]
    b.append(ai[i])
    if tong > s:
        for j in b:
            tong-= j

print(tong)

