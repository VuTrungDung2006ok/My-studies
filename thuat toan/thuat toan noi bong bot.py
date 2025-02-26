def noibot(l):
    for i in range(len(l)-1, 0, -1): #xem theory cua https://www.youtube.com/watch?v=Vca808JTbI8&t=1s)
        for j in range(i):
            if l[j] > l[j +1]:
                nhap = l[j]
                l[j] = l[j+1]
                l[j+1] = nhap
    return l

list = [5,3,8,6,7,2,9,10,16,1]
print(noibot(list))