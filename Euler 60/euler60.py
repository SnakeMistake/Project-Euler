from itertools import permutations, combinations

test_list = [3,7,109,673]

def test_prime(x):
	if x == 1:
		return False
	for i in range(2,int((x**.5))+1):
		if x%i == 0:
			return False
	return True

def test_prime_combos(prime_list):
	for combo in permutations(prime_list,r=2):
		test = int(str(combo[0])+str(combo[1]))
		if not test_prime(test):
			return False
	return True

# print(test_prime_combos(test_list))

def gen_primes(n):
	if n == 2:
		return 2
	primes = []
	for i in range(3,n,2):
		if test_prime(i):
			primes.append(i)
	return primes


test= gen_primes(10000)
# print(test)

# Here's the plan -- test every combination of TWO primes up to 10,000.  Keep those.  Then test every combination of THREE
# of those.  Discard those that don't work.  The idea is that every iteration of n...n+1...n+2... should be
# A subset of the solutions from the prior iteration.  I could just use the original list: 3,7,109,673 -- and
# Find a single prime to add on as the fifth.  But I don't know if that group of 4 is the ONLY group of 4 that would work.

combo_dict = {}

for combo in combinations(test,r=2):
	prime_list = list(combo)
	if test_prime_combos(prime_list):
		if prime_list[0] in combo_dict:
			combo_dict[prime_list[0]].append(prime_list[1])
		else:
			combo_dict[prime_list[0]] = [prime_list[1]]
		if prime_list[1] in combo_dict:
			combo_dict[prime_list[1]].append(prime_list[0])
		else:
			combo_dict[prime_list[1]] = [prime_list[0]]
print(combo_dict)

triples = []
answers = []
for prime in combo_dict:
	print(prime)
	primes = combo_dict[prime]
	primes.append(prime)
	for combo in combinations(primes,r=5):
		prime_list = list(combo)
		if test_prime_combos(prime_list):
			print(prime_list)
			answers.append(prime_list)
