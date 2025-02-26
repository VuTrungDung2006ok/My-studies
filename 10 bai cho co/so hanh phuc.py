def ls(n):
    so = set()
    while n != 1 and n not in so:
        so.add(n)
        n = sum(int(i)**2 for i in str(n))
    return n == 1

a =int(input())
if ls(a):
    print("so",a," la so hanh phuc")
else:
    print("so",a,"khong phai la so hanh phuc")
