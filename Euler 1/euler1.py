sum = 0
def threes_and_fives(sum, num):
  for i in range(num):
    if i%3 == 0 or i%5 ==0:
      sum += i
  return sum

print(threes_and_fives(sum,1000))