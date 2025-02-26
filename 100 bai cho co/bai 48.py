n = input()
a = []
for i in n:
    if i.isdigit():
        i = int(i)
        a.append(i)
        b = sum(a)
print(b)




