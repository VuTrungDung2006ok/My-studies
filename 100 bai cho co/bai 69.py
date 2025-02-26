L = (input().split())
n = len(L)
a = []
b = []
for i in range(0,n):
    if L[i].isdigit():
        a.append(int(L[i]))
    elif L[i].isalpha():
        b.append(L[i])
d = max(b, key=len)
c = min(a)
print(d, c)

