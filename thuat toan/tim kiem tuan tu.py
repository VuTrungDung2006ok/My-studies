
def tuantu(list, n):
    i = 0
    while i < len(list):
        if list[i] ==n:
            return list[i], i
        i +=1

lis = [5,8,4,6,9,2]
a = 9
print(tuantu(lis, a))