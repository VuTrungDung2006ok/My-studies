num1 = ["zero" ,"one","two","three","four","five","six","seven","eight","nine",]
num2 = ["and","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen",]
ch = ["and","ten","twenty","thirty","forty", "fifty", "sixty", "seventy","eighty", "ninety"]
def doc3n(x):

    donvi = x % 10
    chuc = x //10 % 10
    tram = x // 100
    kq = num1[tram] + " hundred " + ch[chuc] + " " + num1[donvi]
    if 
    


    if tram == 0:
        kq = num2[donvi]
        return kq
    
    if chuc == 1:
            kq = num1[tram] + " hundred " + "and" + " " + num2[donvi]
            
            return kq
    return kq

n = int(input())
print(doc3n(n))

