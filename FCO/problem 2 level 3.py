def nguyento(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i ==0:
            return False
    return True

n = int(input())
a=[]
for i in range(0,n):
    a.append(int(input()))

for j in a:
    if nguyento(j):
        print("YES")
    else:
        print("NO")