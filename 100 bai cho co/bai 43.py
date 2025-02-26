a = input()
b = a.split()
d = 0
for i in b:
    if i.isalpha():
        d += 1

print(d)
