m , n , a = map(int,input().split())
while 0 > m or n > 200 or 0 > a > 10:
    m , n , a = map(int,input().split())

s = m * n
tien = s * a

print(tien)
