a = int(input())
c = []
d = 0
for j in range(a+1):
        d += j

for i in range (a-1):
    b = int(input())
    c.append(b)


e = d - sum(c)

print(e)

