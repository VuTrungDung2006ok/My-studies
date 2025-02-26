a, b = map(int, input().split())
if a == 0:
    print("NO")
else:
    if b == 0:
        print("WOW")
    else:
        x = -(b / a)
        print(round(x, 2))