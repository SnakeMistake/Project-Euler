
#runs through the perumatations of a given perimeter p.  Looks for combinations of a and b that are less than the perimeter and that produce
# A hypotenuse that adds up to the perimeter.  If they produce a hypotenuse too large, b moves down stepwise.  If the hypotenuse is too big,
# a moves up stepwise.  If it finds a pythagorean triple, it adds it to the list and ticks b down by one more.
def permutations(p):
	a = 1
	b = p-1
	pythag_triples = []
	for i in range(p-1):
		c = (a**2 + b**2)**.5
		if a + b + c > p:
			b -= 1
		elif a + b + c <p:
			a += 1
		elif a + b + c == p:
			if [a,b,round(c)] not in pythag_triples:
				pythag_triples.append([a,b,round(c)])
				b -= 1
	return pythag_triples

# Runs throught he integers 1 to 10000 finding all the pythagorean triples for that given p (perimeter).  Checks these against a max and returns
# The winners.  I just added a b and c manually to get the answer for Euler
def look_for_max():
	maximum = 0
	for i in range(1001):
		i_perms = permutations(i)
		if len(i_perms) > maximum:
			maximum = len(i_perms)
			print(i_perms)

look_for_max()



