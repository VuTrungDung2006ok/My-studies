d = 0
for a in range (1, 6):
    for b in range(0, 6):
        for c in range(0,6):
            if a!=b and a!=c and b!=c and a + b + c != 0:
                d+=1
    
                       
print(d)