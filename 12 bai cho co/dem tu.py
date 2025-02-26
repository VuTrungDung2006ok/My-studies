s = input().lower()
dic =  {}
#key:value
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print("Tổng số kí tự: ",len(s))
print("Tổng số từ", len(s.split()))
for i in dic:
    if i == " ":
        continue
    print('Kí tự "'+ str(i) + '":',dic[i])

print('Ky tu " ":', dic[" "])