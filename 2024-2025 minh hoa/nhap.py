ai = input()
num = ""
so = []
for i in ai:
    if i.isdigit() or i == "-":
        num+=i
    elif num:
        so.append(num)
        num = ""
if num:
    so.append((num))

print(so)