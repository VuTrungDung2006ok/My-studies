def doiguong(s):
    if s == s[::-1]:
        return True
    else:
        False
a = "AEHIJLMOSTUVWXYZ12358"
b = "A3HILJMO2TUVWXY51SEZ8"

def phanguong(s):
    s1 = " "#chuoi cua ket qua tam thoi theo phai --> trai
    for i in range(len(s)-1,-1,-1):
        c = s[i] #ki tu lay ra trong chuoi s tu phai --> trai
        if c not in a:
            return False
        else:
            #thay c boi ki tu phan guong va them vao s1
            v = b[a.index(c)]
            s1 +=v

    return s1

c = input()
if doiguong(c):
    print(c,"--is a mirrored string")
else:
    print(c, "--is not a palindrome")

if phanguong(c):
    print(c,"--is a regular palindrome")
else:
    print(c, "--is not a palindrome")

if doiguong(c) and phanguong(c):
    print(c,"--is a mirrored palindrome")



