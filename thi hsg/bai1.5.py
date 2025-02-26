n = int(input())
d = n // 7 * 2
if n % 7 <= 2:
    print(d, d + n % 7)
elif n % 7 <= 5:
    print(d, d + 2)
else:
    print(d + n % 7 - 5, d + 2)