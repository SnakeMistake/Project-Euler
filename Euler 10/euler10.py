import math

sum = 2
x = 3
while x < 2000000:
  for y in range(3,int(math.sqrt(x)+1),2):
    if x%y ==0:
      x+=2
      break
  else:
    sum+=x
    x+=2

print(x)
print(sum)

# primes = [2]
# x = 3

# while x <100000:
#   for prime in primes:
#     if prime <= math.sqrt(x):
#       if x%prime == 0:
#         x+=2
#         break
#   else:
#     primes.append(x)
#     x+=2

# print(primes)