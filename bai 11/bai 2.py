n, k = list(map(int,input().split()))
b = list(map(float,input().split()))
k = 0
for i in range(len(b)):
    for j in range(i, len(b)):
        if abs(b[i]-b[j]) == k:
            k+=1

print(k)


    


        
