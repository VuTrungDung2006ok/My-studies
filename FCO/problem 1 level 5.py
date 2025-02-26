with open("Py3P5.IN.txt", "r") as file:
    lines = file.readlines()

kq = []

for i in range(0, len(lines), 3):
    p = int(lines[i].strip())      
    g = int(lines[i + 1].strip())  
    r = float(lines[i + 2].strip())  
    
    d = 0 
    while p < g:
        p = p + (p * (r / 100))
        d += 1
    
    kq.append(str(d))

with open('Py3P5.OUT.txt', 'w') as file:
    file.write("\n".join(kq) + "\n")