a = int(input())
b = map(int,input().split())
d = 0
for i in b:
    if i % 2 != 0:
        d+=i
    
print(d)