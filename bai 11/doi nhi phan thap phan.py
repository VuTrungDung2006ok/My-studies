def doi(n):
    kq = ""
    while n>0:
        du = n % 2
        kq = str(du) + kq
        n = n //2
    return kq
#main
a = list(map(int,input().split(",")))
for i in range(len(a)):
    print(doi(a[i]))
    