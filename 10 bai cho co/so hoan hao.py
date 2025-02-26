def sohoanhao(n):
    d = 0
    for i in range(1, n):
        if n % i == 0:
            d += i
    if d == n:
        return True
    else:
        return False


def uoc(n):
    L = []
    for i in range(1, n):
        if n % i == 0:
            L.append(i)
    return L


a = int(input())

if sohoanhao(a):
    print("day la so hoan hao")
    print("cac uoc", a, "la", uoc(a))
else:
    print("day ko phai so hoan hao")