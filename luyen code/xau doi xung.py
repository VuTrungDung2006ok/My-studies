def ktrdoixung(x):
    if x[::-1] == x:
        return True
    return False

b = []
n = int(input())
for i in range(n):
    a = input()
    if ktrdoixung(a) is True:
        b.append("CO")
    else:
        b.append("KHONG")

for j in b:
    print(j)


        