a = int(input())
n = list(map(int,input().split()))
n = sorted(n)
dodai = len(n)
tich = []
tduong = n[(dodai)-1] * n[(dodai) - 2]
tam = n[0] * n[1]
tich.append(tduong)
tich.append(tam)
print(max(tich))