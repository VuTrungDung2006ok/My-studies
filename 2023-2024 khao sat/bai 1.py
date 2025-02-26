n = int(input())
a = []
for j in range(n):
    ni = input()
    d = 1
    kq = ""
    for i in range(1,len(ni)):
        if ni[i] == ni[i-1]:
            d +=1
        else:
            kq += str(d) + ni[i-1]
            d = 1
    kq += str(d) + ni[len(ni)-1]
    a.append(kq)

for k in a:
    print(k)