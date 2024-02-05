from itertools import permutations, combinations


# Didn't use this one
def make_three_pan_digital():
	digits = [0,1,2,3,4,5,6,7,8,9]
	multiplicand = 1
	multiplier = 1
	product = 1

# Used this as the model, but ended up folding it into the make_problems function below
def generate_perms():
	digits = "0123456789"
	perms = permutations(digits)
	nums = []
	for perm in perms:
		nums.append("".join(perm))
	return nums

# This figures out places to slice a permutation into 3 numbers.  
# The first becomes the multiplier.  The second becomes the multiplicand.  The third becomes the product
def generate_slices():
	slices = [1,2,3,4,5,6,7,8]
	slice_combos = combinations(slices, r=2)
	slices = []
	for item in slice_combos:
		slices.append(item)
	return slices 


# Got this one wrong at first because I misread the question and included 0 as a pandigital digit.  That actually made it much wackier
# First of all, the extra digit turned the runtime from 10 seconds to ~70 seconds.  Second, it produced a lot of strange cases where the 
# zero was the leading digit of one of the terms and it got left off. 
# This function takes digits 1-9 and figures out all permutations.  Then it finds all the combinations of indexes for slicing.  For each
# permutation it tries all of the slice combinations, creating 3 terms with each loop.  If the first two multiply to the 3rd, it adds a tuple to the problems list
def make_problems():
	digits = "123456789"
	perms = permutations(digits)
	slices = generate_slices()
	problems = []
	for perm in perms:
		num = "".join(perm)
		for indexes in slices:
			multiplier = int(num[:indexes[0]])
			multiplicand = int(num[indexes[0]:indexes[1]])
			product = int(num[indexes[1]:])
			if multiplier * multiplicand == product:
				problems.append((multiplier,multiplicand,product))
	return problems 

problems =make_problems()
print(problems)
products = []

for problem in problems:
	products.append(problem[2])
print(products)
unique_products = set(products)
print(unique_products)
total = 0
for item in unique_products:
	total += item

print(total)







