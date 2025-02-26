chan = {0,2,4,6,8}
le = {1,3,5,7,9}
sochan = 0
sole = 0
n = input()
for i in n:
    if int(i) in chan:
        sochan +=1
    if int(i) in le:
        sole +=1

if sochan == sole:
    print("YES")
else:
    print("NO")

