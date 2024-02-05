# num = 600851475143 
# divisor_list = []
# prime_list = []
# non_prime_list = []
# for i in range(1, num):
#   if num % i == 0:
#     divisor_list.append(i)
# for term in divisor_list:
#   for i in range(2,term-1):
#     if term%i == 0 and term not in non_prime_list:
#       non_prime_list.append(term)
# for term in divisor_list:
#   if term not in non_prime_list:
#     prime_list.append(term)

# print(divisor_list)
# print(prime_list)
# print(non_prime_list)
# print(max(prime_list))
factor_tree = []
num = 600851475143 
for i in range(1,10000):
  if num%i == 0:
    factor_tree.append(i)
for term in factor_tree:
  num = (num / term)
print(num)
for index,term in enumerate(factor_tree):
  for i in range(2,term-1):
    if term%i ==0:
      factor_tree[index] = i
      factor_tree.append(int(term/i))
print(factor_tree)
product = 1
for term in factor_tree:
  product = product*term
print(product)