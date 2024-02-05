x = 2**1000

def mult_digits(num):
  string = str(num)
  sum = 0
  for digit in string:
    sum += int(digit)
  return sum


sum_ans = mult_digits(x)
print(sum_ans)