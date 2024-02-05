def factorial(x):
	product = 1
	for i in range(1,x+1):
		product *= i
	return product

def sums_of_factorials(x):
	string_x = str(x)
	sum =0
	for digit in string_x:
		sum += factorial(int(digit))
	return sum 


# I think we only need to go up to 7 digits because sums seem to fall way behind the numbers themselves once you hit 10 million or so. 
# I haven't figured out the exact cutoff beyond which it doesn't make sense to check
for i in range(10000000):
	if sums_of_factorials(i) == i:
		print(i)


print("done")