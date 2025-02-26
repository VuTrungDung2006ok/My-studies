def hoanvi(a):
    if len(a) == 1:
        return [a]
    
    lis = []
    for i in range(len(a)):
        so_dau = [a[i]]
        so_sau = a[:i] + a[i+1:]
        for so in hoanvi(so_sau):
            lis.append(so_dau + so)

    return(lis)

n = 4
a = [1,2,3,4]
for i in hoanvi(a):
    print(i)