
# Handle the poker text file
cards = open("0054_poker.txt", "r").read().split()
hand = []
pl1 = []
pl2 = []
score_p1 = 0
counter = 0

# Assign values to face cards
val_dict = {
	"2": 2,
	"3": 3,
	"4": 4,
	"5": 5,
	"6": 6,
	"7": 7,
	"8": 8,
	"9": 9,
	"T": 10,
	"J": 11,
	"Q": 12,
	"K": 13,
	"A": 14}

card_dict = {
	2: "2",
	3: "3",
	4: "4",
	5: "5",
	6: "6",
	7: "7",
	8: "8",
	9: "9",
	10: "T",
	11: "J",
	12: "Q",
	13: "K",
	14: "A"}

straightcheck = "A23456789TJQKA"
# Define various metrics of winning:
def high_card(values1, values2):
	max1 = max(values1)
	max2 = max(values2)
	while max1 == max2:
		values1.remove(max1)
		values2.remove(max2)
		max1= max(values1)
		max2= max(values2)
	if max1 > max2:
		return 1
	if max2 > max1:
		return 2

def pairs(cardcounts1,cardcounts2):
	trips1 = []
	pairs1 = []
	trips2 = []
	pairs2 = []
	for key in cardcounts1:
		if cardcounts1[key] == 3:
			trips1.append(key)
		if cardcounts1[key] == 2:
			pairs1.append(key)
	for key in cardcounts2:
		if cardcounts2[key] ==3:
			trips2.append(key)
		if cardcounts2[key] ==2:
			pairs2.append(key)
	if len(trips1) > len(trips2):
		return 1
	elif len(trips2) > len(trips1):
		return 2
	if len(trips1) > 0:
		if trips1[0] > trips2[0]:
			return 1
		else:
			return 2
	if len(pairs1) > len(pairs2):
		return 1
	elif len(pairs2) >len(pairs1):
		return 2
	if len(pairs1) > 0:
		if pairs1[0] > pairs2[0]:
			return 1
		elif pairs1[0] == pairs2[0]:
			return 0
		else:
			return 2
	else:
		return 0


def straight(values1,values2):
	values1 = sorted(values1)
	values2 = sorted(values2)
	straight1 = ""
	straight2 = ""
	high1 = ""
	high2 = ""
	if 14 in values1:
		straight1 += "A"
	if 14 in values2:
		straight2 += "A"
	for value in values1:
		straight1 += card_dict[value]
	for value in values2:
		straight2 += card_dict[value]
	if straight1[0:5] in straightcheck:
		high1 += straight1[-1]
	if len(straight1) == 6:
		if straight1[1:6] in straightcheck:
			high1 += straight1[-1]
	if straight2[0:5] in straightcheck:
		high2 += straight2[-1]
	if len(straight2) == 6:
		if straight2[1:6] in straightcheck:
			high2 += straight2[-1]
	if len(high1) > len(high2):
		return 1
	if len(high2) > len(high1):
		return 2
	if len(high1) == len(high2) and len(high1)==1:
		if val_dict[high1] > val_dict[high2]:
			return 1
		else:
			return 2
	return 0

def fourofkind(cardcounts1,cardcounts2):
	fours1 = ""
	fours2 = ""
	for key in cardcounts1:
		if cardcounts1[key] == 4:
			fours1 += key
	for key in cardcounts2:
		if cardcounts2[key] ==4:
			fours2 += key
	if fours1 > fours2:
		return 1
	if fours2 > fours1:
		return 2
	else:
		return 0

def fhouse(cardcounts1,cardcounts2):
	fullh1 = False
	fullh2 = False
	if len(cardcounts1) == 2:
		fullh1 = True
	if len(cardcounts2) ==2:
		fullh2 = True
	if fullh2 == True and fullh1 == False:
		return 2
	if fullh1 == True and fullh1 == True:
		if max(cardcounts1) > max(cardcounts2):
			return 1
		else:
			return 2
	if fullh1 == True and fullh2 == False:
		return 1

def flush(hand1,hand2):
	suits1 = set()
	suits2 = set()
	for card in hand1:
		suits1.add(card[1])
	for card in hand2:
		suits2.add(card[1])
	if len(suits1) == 1:
		return 1
	if len(suits2) ==1:
		return 2
	return 0


def sflush(hand1,hand2, values1, values2):
	result1 = flush(hand1,hand2)
	result2 = straight(values1,values2)
	if result1 ==1 and result2 ==1:
		return 1
	if result1 ==2 and result2 ==2:
		return 2

def rflush(hand1,hand2, values1, values2):
	result1 = flush(hand1,hand2)
	result2 = straight(values1,values2)
	if result1 ==1 and result2 ==1:
		if max(values1) == 14:
			return 1
	if result1 ==2 and result2 ==2:
		if max(values2) ==14:
			return 2

# Test winning conditions:
# print(high_card(["2C", "3S", "8S", "8D", "TD"], ["5H", "5C", "6S", "7S", "KD"]))
# print(pairs(["2C", "3S", "8S", "8D", "TD"], ["5H", "5C", "6S", "7S", "KD"]))


# A Net function that checks all winning conditions in order of importance
def check_win(hand1, hand2):
	values1 = [val_dict[item[0]] for item in hand1]
	values2 = [val_dict[item[0]] for item in hand2]
	cardcounts1= {}
	cardcounts2= {}
	for value in values1:
		if value in cardcounts1:
			cardcounts1[value] +=1
		else:
			cardcounts1[value] = 1
	for value in values2:
		if value in cardcounts2:
			cardcounts2[value] +=1
		else:
			cardcounts2[value] = 1
	#check royal flush
	win = rflush(hand1,hand2, values1, values2)
	if win ==1:
		return 1
	if win ==2:
		return 0
	#check straight flush
	win = sflush(hand1,hand2, values1, values2)
	if win ==1:
		return 1
	if win ==2:
		return 0
	# check 4 of a kind
	win = fourofkind(cardcounts1,cardcounts2)
	if win ==1:
		return 1
	if win ==2:
		return 0

	# Check Full house
	win = fhouse(cardcounts1,cardcounts2)
	if win ==1:
		return 1
	if win ==2:
		return 0

	# Check Flush
	win = flush(hand1,hand2)
	if win ==1:
		return 1
	if win ==2:
		return 0

	# Check straight
	win = straight(values1, values2)
	if win ==1:
		return 1
	if win ==2:
		return 0

	# Check triples, two pair, and pair
	win = pairs(cardcounts1,cardcounts2)
	if win ==1:
		return 1
	if win ==2:
		return 0
	# High card
	win = high_card(values1, values2)
	if win==1:
		return 1
	else:
		return 0


# Runs through the file and creates hands of 5.
for card in cards:
	hand.append(card)
	if len(hand) == 5 and counter % 2 == 0:
		pl1 = hand
		hand = []
	elif len(hand) == 5 and counter % 2 == 1:
		pl2 = hand
		hand = []
		# print(counter//10 +1)
		# print(pl1)
		# print(pl2)
		score_p1 += check_win(pl1, pl2)
	counter += 1



print(score_p1)
