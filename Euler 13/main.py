sum = 0
with open('numbers.txt') as x:
  numbers = x.read()

nums = numbers.split()
print(nums)

for num in nums:
  sum += int(num)
print(sum)