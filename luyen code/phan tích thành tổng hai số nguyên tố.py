def sangnguyento(x):
    b = [1] * (x+1)
    b[0] = b[1] = 0
    for i in range(2,int(x**0.5)+1):
        if b[i] == 1:
            for j in range(i*i, x+1, i):
                b[j] = 0

    nt = [i for i in range(2, x+1) if b[i] == 1]
    return nt

kq = []
n = int(input())
a = sangnguyento(n)
a_set = set(a)
for i in a:
    st = n - i
    if st in a_set and i < st:
        kq.append((i,st))

if kq == []:
    print(0)
else:
    print(len(kq))
    for j in kq:
        print(" ".join(map(str, j)))