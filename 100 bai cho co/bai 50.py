n = input()
a = 0
b = 0
c = 0
d = 0
e = len(n)
ki_tu = set("~!@#$%^&*()_+-[];':<,>.?/")
for i in n:
    if i.isupper():
        a += 1
    elif i in ki_tu:
        b += 1
    elif i.islower():
        c += 1
    elif i.isdigit():
        d += 1
    
if a > 0 and b > 0 and c > 0 and d > 0 and e >6:
        print("mk manh")
else:
        print("mk yeu")









