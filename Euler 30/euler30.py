def fifthpowercheck(num):
	stringnum = str(num)
	sum = 0
	for digit in stringnum:
		sum+= int(digit)**5
	if sum == num:
		return True
	else:
		return False


#For testing purposes -- same function but to the fourth power to test the givens in the prompt
def fourthpowercheck(num):
	stringnum = str(num)
	sum = 0
	for digit in stringnum:
		sum+= int(digit)**4
	if sum == num:
		return True
	else:
		return False

answer_list = []
for i in range(10000000):
	if fifthpowercheck(i) ==True:
		answer_list.append(i)

print(answer_list)
final_ans = 0
for answer in answer_list:
	final_ans += answer
print(final_ans)