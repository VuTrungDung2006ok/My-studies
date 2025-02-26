n = int(input())
d = 0
while n < 0:
    print ("vui long nhapp lai")
    n = int(input())
    
for i in range(1, 999):
    a = 2 ** i
    if a == n:
        d += 1
    
if d == 1:
    print("dung")
elif d ==0:
    print("sai")    