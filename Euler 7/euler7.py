largest_prime = 2
prime_count = 1
x = 3
while prime_count <= 10000:
  for y in range(3,x,2):
    if x%y == 0:
      x+=2
      break
  else:
    largest_prime = x
    prime_count += 1
    x+=2

print(largest_prime)
print(prime_count)
