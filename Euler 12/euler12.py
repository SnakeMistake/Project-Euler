triang_num = 1
greatest_factors = 1
counter = 2

def factor_check(num):
  factors = 0
  for i in range(1, round(num**0.5)+1):
    if num%i == 0:
      factors +=2
  return factors

while greatest_factors <500:
  triang_num += counter
  if factor_check(triang_num) > greatest_factors:
    greatest_factors = factor_check(triang_num)
    print(f"{triang_num} has {greatest_factors} factors")
  counter += 1
