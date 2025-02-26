n = int(input())
def chuoinhiphan(x):
    if len(x) == n:
        print(x)
    else:
        chuoinhiphan(x+"0")
        chuoinhiphan(x+"1")
x = ""
chuoinhiphan(x)





