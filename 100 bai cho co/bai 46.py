a = input()
b = 0
c = 0
d = 0
for i in a:
    if i.isupper():
        b +=1
    elif i.islower():
        c +=1
    elif i.isdigit():
        d +=1

print(b,c,d)