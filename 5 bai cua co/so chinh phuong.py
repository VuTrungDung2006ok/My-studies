def doixung(n):
    s = str(n)
    if s == s[: : -1]:
        return True
    else:
        return False
    
def nguyento(n):
    for i in range(2, n):
        if n % i ==0:
            return True
    return False

def nguyentodep(n):
    if doixung(n) and nguyento(n):
        return True
    else:
        return False

a, b = map(int,input().split())

for i in range(a, b+1):
