from itertools import combinations

def generate_variations(n):
	list_n = list(str(n))
	combo_families = []
	indices = [x for x in range(len(list_n))]
	for i in range(1, len(list_n)):
		index_combos = combinations(indices,r=i)
		for combo in index_combos:
			template = list(str(n))
			list_nums = []
			for i in range(10):
				for index in combo:
					template[index] = str(i)
				num = int("".join(template))
				if prime_check(num):
					list_nums.append(num)
			if len(list_nums) > 7:
				print(list_nums)
	# return combo_families

def prime_check(n):
	if n==1:
		return False
	if n==2:
		return True 
	for i in range(2,int(n**.5)+1):
		if n%i==0:
			return False
	return True


# This took ages -- the correct answer was 121313 -- I ran through to 1million just guessing I'd hit it before then.
# Known issues - this does 10x the work it needs to.  When you iterate through the tens place for example, you're going to get a bunch
# of primes that repeat for 1x, 2x, 3x, 4x and so on.   There's probably a better way to do this with combinatorics or regex


# for i in range(10,1000000):
# 	if i%1000 == 0:
# 		print(i)
# 	generate_variations(i)

