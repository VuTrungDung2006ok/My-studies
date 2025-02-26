def nguyento(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i ==0:
            return False
    return True

n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))

for i in a:
    for j in range(i-1, 1,-1):
        k = i - j
        if nguyento(j) ==True and nguyento(k)==True: 
            print(i , "=", j ,"+" ,k)
            break

s = input()
m = int(input())
for i in range(0,m):
    l , r = (map(int,input().split()))
    chuoi = s[l-1:r] # day la code tim vi tri
    if chuoi == chuoi[::-1]: # cai code 2 la cau doi xung
        print(1)
    else:
        print(-1)

                        
a = int(input())
b = int(input())
c = a * b
for k in range(10,21):
    du1 = a % k
    du2 = b % k                                          # https://cdn.ucode.vn/uploads/20108/upload/wofeOxmn.pdf 
    if c > a * du2 + b * du1 -(du1*du2):
        c = a * du2 + b * du1 -(du1*du2)
    
print(c)
    


