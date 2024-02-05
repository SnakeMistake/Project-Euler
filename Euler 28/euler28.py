diagonal_list = [1]
n=2
for x in range(3,1002,2):
	for i in range(4):
		diagonal_list.append(diagonal_list[-1]+n)
	n+=2

# print(diagonal_list)
sum = 0

for item in diagonal_list:
	sum+= item

print(sum)