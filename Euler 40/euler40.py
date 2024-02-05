digit_count = 0
targets = [1,10,100,1000,10000,100000,1000000]
counter = 0
product_digits = []

while len(targets)>0:
	counter += 1
	if digit_count+len(str(counter)) >= targets[0]:
		digit_skip = targets[0]- digit_count
		product_digits.append(str(counter)[digit_skip-1])
		targets.pop(0)
	digit_count += len(str(counter))

print(product_digits)
ans = 1

for item in product_digits:
	ans*= int(item)

print(ans)