def chiatri(arr):
    if len(arr) > 1:
        #chia danh sach thanh 2 nuaw
        mid = len(arr) // 2
        trai = arr[:mid]
        phai = arr[mid:]
        #sap xep de quy hai nua
        chiatri(trai)
        chiatri(phai)
        a = b = c = 0
    # ket hop hai nua da xap xep 
        while a < len(trai) and b < len(phai):
            if trai[a] < phai[b]:
                arr[c] = trai[a]
                a += 1
            else:
                arr[c] = phai[b]
                b += 1
            c += 1
    # kiem tra neu con phan tu ben trai
            while a < len(trai):
                arr[c] = trai[a]
                a += 1
                c += 1
    # kiem tra neu con phan tu ben phai
            while b < len(phai):
                arr[c] = phai[b]
                b += 1
                c += 1





