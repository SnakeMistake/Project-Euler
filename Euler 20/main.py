def factorial(num):
  product = 1
  while num >1:
    product *= num
    num -=1
  return product

target = factorial(100)
print(target)
string_num = str(target)
print(string_num)
sum=0
for digit in string_num:
  sum += int(digit)
  print(sum)
  