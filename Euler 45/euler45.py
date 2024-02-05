def generate_triangle_nums(n):
	triangle_nums = []
	for i in range(1,n):
		triangle_nums.append(int(i*(i+1)/2))
	return triangle_nums


def generate_pentagonal_nums(n):
	pentagonal_nums = []
	for i in range(1,n):
		pentagonal_nums.append(int(i*(3*i-1)/2))
	return pentagonal_nums

def generate_hexagonal_nums(n):
	hexagonal_nums= []
	for i in range(1,n):
		hexagonal_nums.append(int(i*(2*i-1)))
	return hexagonal_nums

hexagonal_nums =set(generate_hexagonal_nums(100000))
pentagonal_nums = set(generate_pentagonal_nums(100000))
triangle_nums = set(generate_triangle_nums(100000))

overlap = hexagonal_nums.intersection(pentagonal_nums)
double_overlap = overlap.intersection(triangle_nums)

print(overlap)
print(double_overlap)

