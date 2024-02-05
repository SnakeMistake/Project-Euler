from itertools import permutations


def divisible_pandigitals():
	digits = "".join([str(x) for x in range(10)])
	perm_list = permutations(digits)
	pandigitals=  []
	for item in perm_list:
		pandigital = "".join(item)
		one= int(pandigital[1:4])
		two = int(pandigital[2:5])
		three = int(pandigital[3:6])
		four= int(pandigital[4:7])
		five= int(pandigital[5:8])
		six= int(pandigital[6:9])
		seven = int(pandigital[7:10])
		# if one%2 == 0: and two%3==0 and three %5 ==0 and four%7 ==0 and five%11 ==0 and six%13==0 and seven%17==0:
		if one%2 ==0 and two%3 ==0 and three%5==0 and four%7==0 and five%11==0 and six%13==0 and seven%17==0:

			pandigitals.append(pandigital)
	return pandigitals



answers = divisible_pandigitals()

sum_ans = 0
for item in answers:
	sum_ans += int(item)

print(sum_ans)