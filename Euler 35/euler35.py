
# Checks a number to see if it's prime.  Only checks up to the square root to save some time.
def primecheck(x):
	if x ==1:
		return False
	if x ==2:
		return True
	for i in range(2,round(x**.5)+1):
		if x%i == 0:
			return False
	return True



# The greyed out text was causing a bug -- the program would find all of the correct numbers but would skip 2 -- the only even prime!
# This seemed like a good idea to me because I thought it would save time. It turns out, the program actually takes about 1 second LONGER
# with these lines of code.  

def check_next_in_circ(x):
	# for digit in str(x):
	# 	if int(digit)%2 ==0:
	# 		return False
	new_x = int(str(x)[-1] + str(x)[:-1])
	# print(new_x)
	if primecheck(new_x):
		return new_x
	else:
		return False


# runs through the numbers 1-1million looking for circular primes.  At first I misunderstood the prompt in a couple of ways:
# It's not just a reverse string [::-1] of a given number.  It's also not every possible permutation of digits.  A circular
# number refers to the same order of digits, but starting at any given one and proceeding in a loop.  
def find_circular_primes():
	circular_primes = []
	count = 0
	for i in range(1,1000001):
		if primecheck(i):
			test = i
			for tries in range(len(str(i))):
				test = check_next_in_circ(test)
				# print(test)
				if test == False:
					break
			if test >0:
				circular_primes.append(i)
				count+=1
				print(i)

	return count


print(find_circular_primes())
print('done')

