a,b,c=map(int,input().split())
for i in range(min(a,b,c), 0, -1):
    if a % i ==0 and b % i ==0 and c % i ==0:
        print(i)
        break