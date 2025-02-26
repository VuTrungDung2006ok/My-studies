a = int(input())
b = list(map(int,input().split()))
for i in range(a) :
    print(max(a[:i+1]))