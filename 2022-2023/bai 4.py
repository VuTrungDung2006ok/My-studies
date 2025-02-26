t = int(input())
kq = []
for i in range(t):
    n , k = map(int,input().split())
    ai = list(map(int,input().split()))
    chan = []
    le = []
    if k % 2==0:
        kq.append(0)
    else:
        for j in ai:
            if j % 2 ==0:
                chan.append(j)
            else:
                le.append(j)
    d = 0            
    for l in chan:
        if d == 1:
            break
        for u in le:
            if l + u ==k:
                kq.append(1)
                d = 1
                break

print("".join(map(str, kq)))
