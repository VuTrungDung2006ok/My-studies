n = int(input())
ai = list(map(int,input().split()))
s = []
for i in range(len(ai)-1):
    tong = ai[i] + ai[i+1]
    s.append(tong)

print(max(s))
    