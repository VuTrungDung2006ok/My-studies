L = list(map(int,input().split()))
for i in L:
    if i > 0:
        print(0)
    else:
        b = max(L)
        
        print(b)
        break