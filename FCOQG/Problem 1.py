lines = (input())

a = []
for i in range(0,len(lines),1):
    n = lines[i].strip()
    for i in n:
        if n.isdigit():
            a.append(str(n))
            d = len(a)
            
print(d)


