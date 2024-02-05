from itertools import combinations

def pentagonal_generator(n):
	pent=int(n*(3*n-1)/2)
	return pent 

pent_list = []

# The upper limit of this challenge was difficult.  1000 returns no results and takes 4 seconds.  2000 returns no results and takes 18 seconds.
# Any value above 5000 takes so long that the calculation never finishes.  It turns out 3000 is the sweet spot - it returns one result!
for i in range(1,3000):
	pent_list.append(pentagonal_generator(i))

print(pent_list)

for item in combinations(pent_list,2):
	difference = abs(item[0] - item[1])
	sum_pents = item[0] + item[1]
	if sum_pents in pent_list and difference in pent_list:
		print(difference)

