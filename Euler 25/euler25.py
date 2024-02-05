#Let's make the fibonacci sequence again.  This time I might need a list:

fib_list = [1,1]

def next_fib(nums):
	new_term = nums[-1] + nums[-2]
	nums.append(new_term)
	return nums


#This returns the first number in the fibonacci sequence that has 1000 digits as well as the index of that number.  Apparently project euler didn't want a python index as much as a traditional (starting at ONE) index
for i in range(10000):
	fib_list = next_fib(fib_list)
	if len(str(fib_list[-1])) == 1000:
		print(fib_list[-1])
		print(len(fib_list)-1)
		break

# 