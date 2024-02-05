from itertools import product
primes = ["1", "2","3","5","7", "9"]

def generate_primes_to_test():
	full_primes = []
	for x in range(2,8):
		prime_list = product(primes,repeat=x)
		for item in prime_list:
			string_prime = "".join(item)
			if prime_check(int(string_prime)):
				print(string_prime)
				non_p = 0
				for i in range(1, len(string_prime)):
					if prime_check(int(string_prime[:i])) == False:
						non_p += 1
					if prime_check(int(string_prime[i:])) == False:
						non_p += 1
				if non_p == 0:
					full_primes.append(int(string_prime))
	return full_primes
				



def prime_check(x):
	if x == 1:
		return False
	for i in range(2,round(x**.5)+1):
		if x%i == 0:
			return False
	return True

# print(prime_check(4))
print('start')
answers = (generate_primes_to_test())
sum_ans = 0
for answer in answers:
	sum_ans += int(answer)
print(sum_ans)
print('done')