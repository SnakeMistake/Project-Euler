change = [0,0,0,0,0,0,0,0]
combos=[]
counter = 0
# ones=0
# twos=0
# fives=0
# tens=0
# twentys=0
# fiftys=0
# hundreds=
# twohundreds=0

# def totalchange(onep, twop, fivep, tenp, twentyp, fiftyp, hundredp, twohundredp):
# 	total = onep + twop*2 + fivep*5 + tenp*10 + twentyp*20 + fiftyp*50 + hundredp*100 + twohundredp*200
# 	return total

def calctotal(change):
	total = change[-8] + change[-7]*2 + change[-6]*5 + change[-5]*10 + change[-4]*20 + change[-3]*50 + change[-2]*100 + change[-1]*200
	return total 


def bustcheck(total):
	if total >= 200:
		return True
	else:
		return False


for a in range(2):
	change[-1] = a
	for b in range(3):
		change[-2] = b
		for c in range(5):
			change[-3] = c
			for d in range(11):
				change[-4] = d
				for e in range(21):
					change[-5] = e
					for f in range(41):
						change[-6] = f
						for g in range(101):
							change[-7] = g
							for h in range(201):
								change[-8] = h
								total= calctotal(change)
								if total == 200:
									counter+=1
								if bustcheck(total):
									break


print(counter)
