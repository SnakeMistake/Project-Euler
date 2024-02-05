from itertools import permutations

def gen_pandigitals(length):
	digits = [str(x) for x in range(1,length+1)]
	pandigitals = []
	for item in permutations(digits):
		num = "".join(item)
		if primecheck(int(num)):
			pandigitals.append(num)
	return pandigitals


def primecheck(x):
	if x == 1:
		return False
	if x ==2:
		return True
	for i in range(2,round(x**.5)+1):
		if x%i == 0:
			return False
	else:
		return True


print(gen_pandigitals(7))