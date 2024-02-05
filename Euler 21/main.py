#Finds and returns a list of divisors for a given number
def divisor_find(num):
  divisor_list = []
  for i in range(1,num):
    if num%i ==0:
      divisor_list.append(i)
  return divisor_list
    
#runs through the divisor list and adds them all up to get "d"
def divisor_sum(list):
  sum = 0
  for term in list:
    sum += term
  return sum

##Some tests to make sure the divisors and sums are working
# print(divisor_find(100))
# print(divisor_sum(divisor_find(100)))


#This builds a dictionary of d(n) for every number n up to the top item in the range.
d_dict = {}
for i in range(2,10000):
  d_dict[i] = divisor_sum(divisor_find(i))

print(d_dict)

#This removes all the primes
primes = []
for item in d_dict:
  if d_dict[item] == 1:
    primes.append(item)
for item in primes:
  d_dict.pop(item)

print(d_dict)

# #This creates a list of values for d in the dictionary to look for common items
# values_list = []
# for item in d_dict:
#   values_list.append(d_dict[item])

# print(values_list)


#This searches through the dictionary to find the matches where a d value for one number is another number on the list, and the d_value for that number is equal to the original number
amicable_numbers =[]
for item in d_dict:
  if d_dict[item] in d_dict:
    if d_dict[d_dict[item]] == item:
      amicable_numbers.append(item)

print(amicable_numbers)

#This weeds out perfect numbers like 6 because those were unintentionally caught with the seive above
perfect_numbers = []
for item in amicable_numbers:
  if d_dict[item] == item:
    perfect_numbers.append(item)

print(perfect_numbers)
for item in perfect_numbers:
  amicable_numbers.remove(item)

print(amicable_numbers)

#This adds up the amicable numbers to solve the euler challenge
sum = 0
for item in amicable_numbers:
  sum+= item

print(sum)