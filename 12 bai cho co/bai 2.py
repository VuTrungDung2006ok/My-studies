a = input()
b = input()
aa = int(a)
bb = int(b)


x = len(str(aa * bb))


print((x - len(a)) * " " + a)
print("*")
print((x - len(b)) * " " + b)
print(x * "-")

d = 0
for i in range(len(b)-1,-1,-1):
    t =str(int(b[i])*aa)
    print((x-len(t)-d)* " "+ t)
    d +=1

print(x * "-")
print(" " + str(aa*bb))