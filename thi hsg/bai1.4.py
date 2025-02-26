from math import ceil
k = int(input())
tmp = 1
n = k
while k > 9 * 10**(tmp - 1) * tmp:
    n -= 9 * 10**(tmp - 1) * tmp
    tmp += 1
print(10**(tmp - 1) + ceil(n / tmp) - 1, n % tmp - 1)
print(str(10**(tmp - 1) + ceil(n / tmp) - 1)[n % tmp - 1])