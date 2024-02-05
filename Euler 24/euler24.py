practice_list = [0,1,2]

# def makecombos(num_list):
# 	for item in num_list:
# 		string = ""
# 		string += item



def orderedcombos_test():
	for a in range(3):
		for b in range(3):
			if b != a:
				for c in range(3):
					if c != a and c != b:
						num = a*100 + b*10 + c
						print(num)


# This is pretty goofy but it works - a bunch of nested for loops iterates through the last digit first and then works upwards.  It skips any case in which the digit matches one previously used.
def orderedcombos():
	counter = 1
	for a in range(10):
		for b in range(10):
			if b != a:
				for c in range(10):
					if c != a and c != b:
						for d in range(10):
							if d !=a and d!= b and d!=c:
								for e in range(10):
									if e !=a and e!= b and e!=c and e !=d:
										for f in range(10):
											if f !=a and f!=b and f!= c and f!=d and f!=e:
												for g in range(10):
													if g != a and g !=b and g!=c and g!=d and g!=e and g!=f:
														for h in range(10):
															if h != a and h !=b and h!=c and h!=d and h!=e and h!=f and h!=g:
																for i in range(10):
																	if i != a and i !=b and i!=c and i!=d and i!=e and i!=f and i!=g and i!=h:
																		for j in range(10):
																			if j!= a and j !=b and j!=c and j!=d and j!=e and j!=f and j!=g and j!=h and j!=i:
																				num = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) +str(j)
																				print(num)
																				if counter == 1000000:
																					return num
																				counter+=1


# orderedcombos()



#Trying again with itertools imported --
import itertools

#This appears to work quickly, but it produces tuples with repeats of digits included.  I think the way to fix this is to use a different tool called "permutations"
# combos = itertools.product("0123456789", repeat=10)
# for comb in combos:
# 	print(comb)

#Trying again with permutations:
perms = itertools.permutations("0123456789")

#itertools returns an iterable oject.  This line converts it into a list
perm_list = list(perms)

#this finds the millionth object in the list and prints it out.
print(perm_list[1000001])

#this uses the join method to print that item as a numerical sequence:
print("".join(perm_list[1000001]))