n =int(input())
ai = input()
k = int(input())
num = ""
so = []
d = 0
for i in ai:
    if i.isdigit() or i == "-":
        num+=i
    elif num:
        so.append(num)
        num = ""
if num:
    so.append((num))
for j in range(0,len(so)):
    for l in range(j,len(so)):
        if int(so[j]) + int(so[l]) == k:
            d+=1
print(d)

