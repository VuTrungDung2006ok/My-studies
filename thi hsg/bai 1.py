def giai_thua(n):
    d = 1
    for i in range(1, n+1):
        d *= i
    return d

def ca(n):
    a = 2 * n
    c = n + 1
    b = giai_thua(a) // (giai_thua(c) * giai_thua(n))
    return b

n = int(input())
print(ca(n))