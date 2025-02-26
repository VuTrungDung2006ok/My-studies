def nguyento(x):
    if x == 2:
        return x
    if x > 2:
        for i in range(2, int(x**0.5)+1):
            if x % i ==0:
                return 
        return x
    
n = int(input())
b = []
for i in range(2, (10**5)+1):
    if len(b) < n:
        if nguyento(i) != None:
            b.append(i)

print(b)
