from math import factorial
def combinations(n,r):
	return factorial(n)/(factorial(n-r)*factorial(r))

count = 0
for n in range(101):
	for r in range(1,n):
		if combinations(n,r) > 1_000_000:
			count+=1

print(count)