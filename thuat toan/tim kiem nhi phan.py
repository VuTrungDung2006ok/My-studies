def nhiphan(list, n):
    l = 0
    r = len(list) - 1
    while l <= r:
        m = (l+r)//2
        if list[m] == n:
            return m
        else:
            if list[m] < n:
                l = m
            else:
                r = m


list = [4,7,8,12,45,99]
a = 45
print(nhiphan(list,a))