def phanchia(l, trai, phai):
    i = trai
    j = phai - 1
    p = l[phai]
    
    while i < j:
        while i < phai and l[i] < p:
            i += 1
        while j > trai and l[j] >= p:
            j -= 1
        
        if i < j:
            l[i], l[j] = l[j], l[i]

    if l[i] > p:
        l[i], l[phai] = l[phai], l[i]
    
    return i

def quicksort(l, trai, phai):
    if trai < phai:
        vitriphanchiatrungtam = phanchia(l, trai, phai)
        quicksort(l, trai, vitriphanchiatrungtam-1)
        quicksort(l,vitriphanchiatrungtam +1, phai)

list =[22,11,88,66,55,77,33,44]
quicksort(list, 0, len(list)-1)
print(list)