def chon(l):
    for i in range(len(l)):
        m = i
        for j in range(i+1,len(l)):
            if l[j] < l[m]:
                m = j
        l[i],l[m] = l[m],l[i]    
    return l

list = [5,3,8,6,7,2]
print(chon(list))
