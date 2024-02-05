def palin_check(num):
  if str(num) == str(num)[::-1]:
    return True
palindromes = []

for i in range(1000,100,-1):
  for x in range(1000,100,-1):
    if palin_check(x*i) == True:
      palindromes.append(x*i)
    
print(palindromes)
print(max(palindromes))