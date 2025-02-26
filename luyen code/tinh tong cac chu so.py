t = int(input())
a = []
tong = []
for i in range(t):
    n = input()
    a.append(n)
    e = 0
    for j in a[i]:
        e = e + int(j)
    tong.append(e)

for k in tong:
    print(k)
