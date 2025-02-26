a = int(input())
b = list(map(int,input().split()))
le= 0
chan= 0
for i in range(a):
    if b[i] %2 != 0:
        le +=1
    else:
        chan +=1

le = le -1
chan = chan - 1
tongle = ((le*(le+1))//2)
tongchan = ((chan*(chan+1))//2)
print(tongle + tongchan)
