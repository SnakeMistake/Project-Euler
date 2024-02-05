a_list = []
b_list = []
results = []

for i in range(2,101):
	a_list.append(i)
	b_list.append(i)

for a in a_list:
	for b in b_list:
		results.append(a**b)

print(len(set(results)))

