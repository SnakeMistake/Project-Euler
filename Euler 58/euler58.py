corners = [1,3,5,7,9]
print("starting")
primes = 3
total = 5
length = 3
n=1

def next_corners(last,n):
	new_corners = []
	for i in range(4):
		last+= 2*n
		new_corners.append(last)
	return new_corners

def update_prime_count(nums):
	pris = 0
	for num in nums:
		prime = True
		if num == 1:
			prime = False
		for i in range(2,int(num**.5)+1):
			if num%i ==0:
				prime = False
				break
		else:
			if prime == True:
				pris+=1
	return pris
	

while primes*10 > (total):
	n+=1
	length+=2
	last = corners[-1]
	corners = next_corners(last,n)
	primes+= update_prime_count(corners)
	total +=4
	if n%1000 ==0:
		print(round(100*primes/(total),2))
		print(primes)
		print(total)
		print(length)
print(primes)
print(corners)
print(length)




# print(calc_prime_ratio(corners))
