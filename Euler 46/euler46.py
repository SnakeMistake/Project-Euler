
#Checks and returns primes up to the value n
def find_primes(n):
	primes = []
	for i in range(2,n):
		prime = True
		for x in range(2,int(i**.5)+1):
			if i%x == 0:
				prime = False
		if prime == True:
			primes.append(i)
	return primes

# squares and doubles the value n
def find_double_squares(n):
	return [2*i**2 for i in range(n)]

# Not sure what the upper bound is  -- Takes around 1-2 seconds if I plug in 10,000 for each.  This takes around 400ms
primes = find_primes(5000)
double_squares = find_double_squares(2000)

# using a set to remove duplicates.  Using mod2 to weed out the evens.
totals = set()
for item in primes:
	for other in double_squares:
		total = item +other
		if total%2 !=0:
			totals.add(total)

for i in range(3,100000,2):
	if i not in totals:
		print(i)
