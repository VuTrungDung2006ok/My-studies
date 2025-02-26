n = int(input())
for p in range(1,n+1):
    if (2**p) % p == 2:
        print(p)