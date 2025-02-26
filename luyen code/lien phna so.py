t = int(input())
b =[]
for i in range(t):
    n = int(input())
    s = 1
    for j in range(n):
        s = 1/(1+s)
    b.append(round(s,5))

for j in b:
    print(f"{j:.5f}")
