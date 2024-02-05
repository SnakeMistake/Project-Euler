from itertools import permutations

nine_dig_pandigits = permutations("123456789")
targets = []
for item in nine_dig_pandigits:
	pan_d = int("".join(item))
	targets.append(pan_d)

targets.reverse()
# print(targets)

def check_mults(targets):
	for target in targets:
		string_num = str(target)
		for i in range(1,5):
			first = int(string_num[:i])
			str_first = str(first)
			second = first*2
			str_second = str(second)
			third = first*3
			str_third = str(third)
			fourth = first*4
			str_fourth = str(fourth)
			fifth = first*5
			str_fifth = str(fifth)
			sixth = first*6
			str_sixth = str(sixth)
			if string_num[i:i+len(str_second)] == str_second:
				if len(str_first) + len(str_second) == 9:
					print(string_num)
				if string_num[i+len(str_second):i+len(str_second)+len(str_third)] == str_third:
					if len(str_first) + len(str_second) + len(str_third) == 9:
						print(string_num)
					if string_num[i+len(str_second)+len(str_third):i+len(str_second)+len(str_third)+len(str_fourth)] == str_fourth:
						if len(str_first) + len(str_second) + len(str_third) +len(str_fourth)== 9:
							print(string_num)
						if string_num[i+len(str_second)+len(str_third)+len(str_fourth):i+len(str_second)+len(str_third)+len(str_fourth)+len(str_fifth)] == str_fifth:
							if len(str_first) + len(str_second) + len(str_third) +len(str_fourth) +len(str_fifth)== 9:
								print(string_num)
							if string_num[i+len(str_second)+len(str_third)+len(str_fourth)+len(str_fifth):i+len(str_second)+len(str_third)+len(str_fourth)+len(str_fifth)+len(str_sixth)] == str_sixth:
								if len(str_first) + len(str_second) + len(str_third) +len(str_fourth) +len(str_fifth) +len(str_sixth)== 9:
									print(string_num)



print(check_mults(targets))