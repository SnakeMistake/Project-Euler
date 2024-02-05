
def gen_primes(n):
	primes = [2]
	for i in range(3,n,2):
		prime = True
		for x in range(3,int(i**.5)+1,2):
			if i%x == 0:
				prime = False
		if prime == True:
			primes.append(i)
	return primes 

print("starting")
primes = gen_primes(1000000)
print(primes)
print(len(primes))

# I think little optimizations like skip counting are going to be hugely important here.  For example, this only works with odd numbers of terms
# even numbers of terms will return evens (non-primes)

# OK - quick note.  This was the ugliest brute-forceiest one I've done in a while.  There have to be some optimizations here.  
# Many of the solutions on Euler seem to be creating consecutive sum totals to make the math faster and do less calculation for each loop.
# My solution calculates a sum every time it iterates.  It does have a couple of helpful items - cutoffs at the 1mil mark and cutoffs
# When a hit has been found.
def prime_sums(list_of_primes):
	greatest_length = 23
	length = 23
	start = 0
	while length < len(list_of_primes):
		total = sum(list_of_primes[start:start+length])
		if total in list_of_primes and length > greatest_length:
			greatest_length = length
			print(length)
			print(list_of_primes[start:start+length])
			print(total)
			start = 0
			length += 1
			continue
		if total > 1000000:
			start = 0
			length += 1
			print(f'start: {start} length:{length}')
		else:
			start +=1



prime_sums(primes)