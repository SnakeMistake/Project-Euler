# allprimes = []
# for i in range(1,21):
#   allprimes.append(i)
# print(allprimes)
# for term in allprimes:
#   for index, other_term in enumerate(allprimes):
#     if term != other_term:
#       if term%other_term == 0:
#         allprimes[index] = 1
# print(allprimes)

# prime_factors = []
# for index,term in enumerate(allprimes):
#   for i in range(2,term-1):
#     if term%i == 0:
#       allprimes[index] = i
#       prime_factors.append(int(term/i))
# print(allprimes)
# print(prime_factors)

primedict = {}
smallprimes = [2,3,5,7,11,13,17,19]
for i in range(1,21):
  primedict[i] = []
for term in primedict:
  prime_list = []
  for prime in smallprimes:
    breakdown = term
    while breakdown%prime == 0:
      prime_list.append(prime)
      breakdown = breakdown/prime
    primedict[term] = prime_list

print(primedict)

lcm = 1
lcm_factors = []
for prime in smallprimes:
  prime_count = 0
  for term in primedict:
    if primedict[term].count(prime) > prime_count:
      prime_count = primedict[term].count(prime)
  lcm_factors.append(prime**prime_count)
print(lcm_factors)
for term in lcm_factors:
  lcm *= term
print(lcm)