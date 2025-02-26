x = input()
s = []
for i in x:
    if s == []:
        s.append(i)
    else:
        if i ==")" and s[-1] == "(":
            s.pop()
        elif i =="]" and s[-1] =="[":
            s.pop()
        else:
            s.append(i)

if s == []:
    print("YES")
else:
    print("NO")