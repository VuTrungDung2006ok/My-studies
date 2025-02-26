a = int(input("so tien ban muon mua"))
b =(a//10) + ((a//10)//3)
if ((a//10)%3) >= 1:
    b =(a//10) + ((a//10)//3) + 1
if ((a//10)%3) <= 1:
    b =(a//10) + ((a//10)//3) + ((a//10)%3)
print(b)

    

