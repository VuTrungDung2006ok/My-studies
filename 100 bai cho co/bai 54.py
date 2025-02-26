L = list(map(int,input().split()))
a = int(input())
b = int(input())
if not 0 < a < b < len(L) :
    print("loi")
else:
    print(min(L[a-1:b]))