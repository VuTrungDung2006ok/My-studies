def nguyento(x):
    for i in range(2,int(x**0.5)+1):
        if x % i ==0:
            return "NO"
    return "YES"

n = int(input())
if n <2:
    print("NO")
else:
    print(nguyento(n))  