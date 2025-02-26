a = int(input())
b , c = 1, 1
while b + c <= a:
    b ,c = c, b +c
if a == c:
    print("yes")
else:
    print("no")
