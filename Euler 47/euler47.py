def prime_factorize(n):
	if n ==1:
		return []
	x = 2
	while True:
		if n%x ==0:
			li= prime_factorize(int(n/x))
			li.append(x)
			break
		x+=1
	return li

four_distinct_list =[]
for i in range(2,150000):
	if len(set(prime_factorize(i))) == 4:
		four_distinct_list.append(i)
		
print(four_distinct_list)
for item in four_distinct_list:
	if item +1 in four_distinct_list:
		if item+2 in four_distinct_list:
			print(item, item+1, item+2)
			if item+3 in four_distinct_list:
				print (item, item+1, item+2, item+3)