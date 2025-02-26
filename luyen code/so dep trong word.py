so = int(input())
kq = []
for i in range(so):
    n =input()
    if int(n[0]) // (int(n)%10) == 2 or (int(n)%10) // int(n[0]) == 2:
        kq.append("YES")
    else:
        kq.append("NO")

for k in kq:
    print(k)