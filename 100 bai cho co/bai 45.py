n = 3
a = []
b = input()
c = [int(i) for i in b.split(',')]
if len(c) == n:
    d = sum(c)
    print(d)
else:
    print("0")