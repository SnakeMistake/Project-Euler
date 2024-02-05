
def factor_find(num):
  factors = []
  #Returns a dictionary with a number as the key and a list of factors as the value
  for i in range(1,num):
    if num%i==0:
      factors.append(i)
  return {num:factors}

#places to store abundant, deficient and perfect numbers.  Deficient means the sum of the proper divisors between 1 and the number (exclusive of the number itself) is LESS than the number itself.  Perfect means EQUAL. Abundant means GREATER
abundant = []
deficient = []
perfect = []
#This runs through 1-1000 and finds all the numbers of each type

for i in range(28124):
  x =factor_find(i)
  sum = 0
  for item in x[i]:
    sum+= item
  if sum > i:
    abundant.append(i)
  # elif sum == i:
  #   perfect.append(i)
  # else:
  #   deficient.append(i)

print(f'abundant: {abundant}')
# print(f'deficient: {deficient}')
# print(f'perfect: {perfect}')

def abundant_sums(list):
  sum_list = []
  for item in list:
    for other_item in list:
      sum = item + other_item
      sum_list.append(sum)
  return sum_list


abundant_sums =set(abundant_sums(abundant))
cannot_be_summed_abundantly = []

for i in range(28124):
  if i not in abundant_sums:
    cannot_be_summed_abundantly.append(i)

total = 0
for item in cannot_be_summed_abundantly:
  total+= item
print(total)  
