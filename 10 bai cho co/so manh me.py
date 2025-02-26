def songuyento(x):
    if x < 0:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
        
def SMM(y):
    for i in range (2,y):
       if y % i == 0 and y % i**2 == 0:
           if songuyento(i):
               return True
    return False
# main


n = 1000
for i in range (2,n+1):
    if SMM(i):                     
        print(i)