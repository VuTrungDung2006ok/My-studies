n = int(input())
d = ((n%10)**2) + ((n//10)**2)
b = 0
for j in range(1, d):
        if d%j ==0:
            b +=1

if b >= 2:
            print("day ko phai la so dep")
elif b <2:
            print("day la so dep,", d) 

            
          
    
