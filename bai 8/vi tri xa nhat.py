n = list(map(int,input().split()))
x = 11
min_distance = abs(n[0]-x)
closest_value = n[0]
for i in n : 
    distance = abs(i-x)
    if  distance < min_distance:
        min_distance = distance
        closest_value = i
print(closest_value)