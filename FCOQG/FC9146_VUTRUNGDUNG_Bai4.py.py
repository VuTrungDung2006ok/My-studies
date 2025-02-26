def giaithua(x):
    d = 1
    for i in range(1,x+1):
        d *= i
        
    return d

with open('Py5P4.IN.txt', 'r') as file:
    a = file.readline()
    b = []

    e = 2.718281828
    for i in range(0, len(a), 1):
        n = list(map(float,a.split()))
        d = e**(n[0]**2)
        b.append(str(d))

with open('Py5P4.OUT.txt', 'w') as file:
    file.write(f"{b}")
        



