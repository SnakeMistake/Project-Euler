#This library allows us to set a precision for our decimals.  I set it to 100 here.
import decimal
decimal.getcontext().prec = 5000

#Placeholder global variables to get the max string:
integer = 0
max_repeat = 0
# attempts to get the reciprocal -- the first one limits us to around 10 digits.  The second method imports the decimal library to set a larger precision
def getrecip(x):
	return str(1/x)

def getlongrecip(x):
	longrecip = 1/decimal.Decimal(x)
	return str(longrecip)

#This currently works for the non-repeaters (their decimals don't go up past 10 or so).  It also works for those that go straight into their repeating decimals.
# It does not currently weed out those whose repeating decimals start later on (like 1/6).
#It also currently overrides in cases like 1/7 where it finds, say 96 characters in a row that repeat in the next 96... not accounting for the little micro-repeats
# within those sections
def checkrepeats(string_num,max_repeat):
	if len(string_num) < 50:
		return 0
	else: 
		for i in range(30):
			if string_num[i] == string_num[i+1] and string_num[i] == string_num[i+2] and string_num[i] == string_num[i+3]:
				return 1
		k = max_repeat
		while True:
			for i in range(len(string_num)-k+1):
				if string_num[i:i+k] == string_num[i+k:i+2*k]:
					possible_repeat = string_num[i:i+k]
					for num in range(2,len(possible_repeat)):
						if possible_repeat[:num] == possible_repeat[num:2*num]:
							return num
					return k
			k+=1	
		return k



# Testing cases 1-21 to figure out if it works...and updating to 1001
for i in range(1,1001):
	print(i)
	# print(f'i is {i} and the reciprocal is {getlongrecip(i)}')
	# print(f'The longest repeating string is {checkrepeats(getlongrecip(i),max_repeat)}')
	repeat_check = checkrepeats(getlongrecip(i),max_repeat)
	if repeat_check > max_repeat:
		integer = i
		max_repeat=repeat_check

print(integer)
print(max_repeat)