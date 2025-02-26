a = list(map(int,input().split()))
b = list(map(int,input().split()))
v = int(input("nhap so v: "))
d = 0 
for i in a:
    for j in b:
        if i + j == v:
            d = 1
            break
    if d == 1:
           break        
if d>=1:
            print("True")
else:
            print("False")        
        
    