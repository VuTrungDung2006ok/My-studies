n = int(input())
a = [ [0]*n for i in range(n)]

value = 1 

i = n // 2
j = n - 1

while value <= n*n:
    if a[i][j] == 0:
        a[i][j] = value
        value += 1
    i1 = ( i - 1 ) % n
    j1 = (j + 1) % n
    if a[i1][j1] == 0:
        i = i1
        j = j1
    else:
        i = (i ) % n
        j = (j-1) % n

for row in a:
    print(" ".join([str(i) for i in row]))
