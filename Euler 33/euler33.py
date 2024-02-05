# This works surprisingly well --- seems to take any fraction and reduce it.  Finds the greatest common factor for x and y and then divides each by that gcf.  Returns and integer
def simplify_frac(x,y):
	x_factors = set()
	y_factors = set()
	for i in range(1,x+1):
		if x%i ==0:
			x_factors.add(i)
	for i in range(1,y+1):
		if y%i ==0:
			y_factors.add(i)
	common_factors = x_factors.intersection(y_factors)
	gcf = max(common_factors)
	return int(x / gcf), int(y/gcf)

# This takes a fraction and then expands it to every form up to a denominator of 100.
def expand_frac(x,y):
	expanded_fracs = []
	for i in range(1,round(100/y)+1):
		new_frac = (x*i,y*i)
		expanded_fracs.append(new_frac)
	return expanded_fracs


# This one didn't end up panning out

# def find_cancel_fracs():
# 	cancel_fracs = set()
# 	for x in range(1,100):
# 		for y in range(x+1,100):
# 			print(x,y)
# 			simple_x,simple_y = simplify_frac(x,y)
# 			if simple_x != x and len(str(simple_y))<len(str(y)) and str(simple_x) in str(x) and str(simple_y) in str(y):
# 				if y%10 != 0 and y%11 != 0:
# 					x_digits = set(str(x))
# 					y_digits = set(str(y))
# 					expanded_fracs = expand_frac(simple_x,simple_y)
# 					for frac in expanded_fracs:
# 						if frac[0] < x:
# 							numerator_digits = set(str(frac[0]))
# 							denominator_digits = set(str(frac[1]))
# 							if numerator_digits.difference(x_digits) == denominator_digits.difference(y_digits) and len(denominator_digits.difference(y_digits))>0:
# 								print(numerator_digits)
# 								print(x_digits)
# 								print(numerator_digits.difference(x_digits))
# 								cancel_fracs.add((x,y))
# 	return cancel_fracs 

# print(find_cancel_fracs())


# For this solution (which ended up working), I built up from my expand_frac function rather than generate all the possible fractions and then whittle down.
# It may have been possible to solve with the method above, but it was easier to debug with fewer fractions printing out, neatly organized -- as this one did.
def find_cancelling_fracs():
	cancelling_fracs = []
	for x in range(1,9):
		for y in range(x+1,10):
			test_list = expand_frac(x,y)
			for item in test_list:
				if item[1] <10:
					x_digit = str(item[0])
					y_digit = str(item[1])
					for frac in test_list:
						if frac[1] > 10 and frac[1]%10 != 0 and frac[1]%11 != 0:
							unsimple_num_digits = set(str(frac[0]))
							unsimple_denom_digits = set(str(frac[1]))
							if x_digit in unsimple_num_digits and y_digit in unsimple_denom_digits:
								if unsimple_num_digits.difference(set(x_digit)) == unsimple_denom_digits.difference(set(y_digit)):
									cancelling_fracs.append(frac)
	return cancelling_fracs


# From here on down, I'm taking the solutions and finding their product, then reducing, to give the answer in the format they asked for.
answers = find_cancelling_fracs()
answer_num = 1
answer_denom = 1
for item in answers:
	answer_num *= item[0]
	answer_denom *= item[1]

print(simplify_frac(answer_num,answer_denom))
