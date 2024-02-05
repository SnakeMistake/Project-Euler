# def generate_palindromes():
# 	palindromes = [str(x) for x in range(1,10)]
# 	for item in palindromes:
# 		if len(item) %
# 	print(palindromes)


palindromes = []

for i in range(1000000):
	if str(i)[::-1] == str(i):
		binary_i = str(bin(i))[2:]
		if binary_i == binary_i[::-1]:
			palindromes.append(i)

answer = 0

for item in palindromes:
	answer += int(item)

print(answer)
