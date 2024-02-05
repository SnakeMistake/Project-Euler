sum = 1000

def pyth_check(a, b, c):
  return a**2 + b**2 == c**2


for i in range(1000):
  a = i
  sum = 1000-a
  for x in range(sum):
    b = x
    sum = 1000-(a+b)
    c = sum
    if pyth_check(a,b,c) == True:
      print(a,b,c)
      print(a*b*c)

    
  