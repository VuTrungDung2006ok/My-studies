n = int(input())
ni = input()
kq = ""
d = 1

for i in range(1,len(ni)):
    if ni[i] == ni[i-1]:
        d +=1
    else:
        kq += str(d) + ni[i-1]
        d = 1
kq += str(d) + ni[len(ni)-1]

print(kq)