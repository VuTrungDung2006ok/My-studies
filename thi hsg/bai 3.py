import math
l, r , a, b = map(int,input().split())
a1 = r // a
a2 = l // a
tonga = a1 - a2
b1 = r // b
b2 = l // b
tongb = b1 - b2
boichung = (tonga * tongb) // math.gcd(a, b)
print(tonga + tongb - boichung)



