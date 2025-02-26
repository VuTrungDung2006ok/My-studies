n = list(map(int,input().split()))
d = 0
b = 0

for i in n:
    if i % 2 ==0:
        d += 1
        b += i
if d!=0:
    c = b/ d
    print(c)
else:
    print("khong tinh duoc")



