from string import ascii_uppercase
f= open("0042_words.txt",mode='r').read().split('","')
f[0] = f[0][1:]
f[-1]= f[-1][:-1]

max_num = 26**2


def generate_triangle_nums(max_num):
	triangle_nums = []
	counter = 1
	num = 0
	while num <= max_num:
		num = 0.5*counter*(counter+1)
		triangle_nums.append(int(num))
		counter +=1
	return triangle_nums

triangle_nums = generate_triangle_nums(max_num)

letter_values = {y:x+1 for x,y in enumerate(ascii_uppercase)}

triangle_words = []
for item in f:
	total = 0
	for letter in item:
		total += letter_values[letter]
	if total in triangle_nums:
		print(item)
		triangle_words.append(item)

print(triangle_words)
print(len(triangle_words))


