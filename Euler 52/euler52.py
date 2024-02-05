def check2to6(n):
	two = sorted(str(2*n))
	three = sorted(str(3*n))
	four = sorted(str(4*n))
	five = sorted(str(5*n))
	six = sorted(str(6*n))
	if two == three and two == four and two == five and two == six:
		print(n)

for i in range(1000000):
	check2to6(i)
