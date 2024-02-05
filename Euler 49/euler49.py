from itertools import permutations,combinations

'''
Note to self If I ever try this one again --
To check for the permutations, it's inefficient to generate a ton of theoretical permutations and then check from that list
Instead, compare sorted(str(num1)) to sorted(str(num2)) to sorted(str(num3))
'''

def gen_primes(start,stop):
	x = start
	primes = []
	while x < stop:
		prime = True
		for i in range(2,int(x**.5)+1):
			if x%i == 0:
				prime = False
		if prime ==True:
			primes.append(x)
		x+=1
	return primes 

targets = set(gen_primes(1000,10000))

def check_for_perms(num):
	perm_list = set()
	for item in permutations(str(num)):
		perm_str = "".join(item)
		if perm_str[0] != "0":
			perm_list.add(int(perm_str))
	return perm_list


def series_check(num_list):
	sorted_list = sorted(list(num_list))
	# series_list = []
	for i,item in enumerate(sorted_list):
		for other_item in sorted_list[i+1:]:
			difference = other_item-item
			if item +2*difference in sorted_list:
				first = item 
				second = other_item
				third = item+2*difference
				first_perms = check_for_perms(first)
				if second in first_perms and third in first_perms:
					print(first,second,third)




series_check(targets)






# check_for_perms(targets)

