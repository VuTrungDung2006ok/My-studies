a = int(input())
b = int(input())
u =[]
for i in range(1, a+1):
    for i in range(1, b+11):
        if a % i ==0 and b % i ==0:
            u.append(i)
            
print(set(u))

         