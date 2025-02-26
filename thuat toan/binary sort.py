def binary(a):
    if len(a) <= 1:
        return a
    else:
        mid = len(a) //2
        p = a[mid]
        l = []
        r = []
        m = []
        for x in a:
            if x < p:
                l.append(x)
            elif x > p:
                r.append(x)
            elif x == p:
                m.append(x)
        return binary(l) + m + binary(r)
    
a = list(map(int,input().split()))
print(binary(a))