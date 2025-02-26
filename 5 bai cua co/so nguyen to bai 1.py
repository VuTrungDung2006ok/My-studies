a , b = map(int,input().split())
c = b **2 - a**2
for i in range(2, int(c**0.5)):
    if c % i == 0 :
        print("no")
        break
    else:
        print("yes")
