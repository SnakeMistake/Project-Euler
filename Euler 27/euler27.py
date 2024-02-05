max_primes = 0
primiest_combo = (1,1)

# Starting with a function to run a and b through a quadratic:
def quadratic(a,b,n):
	return n**2 + a*n + b

# Now making a function to check for primes returns True for primes and False for composite numbers
def primecheck(num):
	if num <0:
		return False
	for i in range(2,num):
		if num%i ==0:
			return False
		else:
			pass
	return True


# Now running through values of n and making a list of primes
def consecutive_prime_find(a,b):
	n=0
	prime_list = []
	while True:
		if primecheck(quadratic(a,b,n)):
			prime_list.append(quadratic(a,b,n))
			n+=1
		else:
			return (n,prime_list)


# print(consecutive_prime_find(-79,1601))


# This worked like a dream - 
# found me the answer very quickly.  
# I forgot that the example problem was outside of these bounds (<abs(1000)) so I spent a bunch of time
# trying to find an error that didn't exist
# Note for efficiency -- probably could only check values for b that are already prime!
for a in range(-1000,1001):
	for b in range(-1000,1001):
		# print(a,b)
		result = consecutive_prime_find(a,b)
		if result[0] > max_primes:
			print(result)
			max_primes = result[0]
			print(max_primes)
			primiest_combo = (a,b)
			print(primiest_combo)
		else:
			pass
