# s = input()
# kq = s.strip("0")
# print(kq)

s = input()
a = []
d = 0
for i in range(1,len(s)):
    if s[i] == "1":
        a.append(i)

for j in range(min(a), max(a)):
    if s[j] =="0":
        d+=1

print(d)
