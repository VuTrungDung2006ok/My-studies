n = int(input())
a = list(map(int, input().split()))

s = [0]*n
s[0] = a[0]

for i in range(1, n):
	if s[i-1] <= 0:
		s[i] = a[i]
	else:
		s[i] = s[i-1] + a[i]

print(max(s))