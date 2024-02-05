letter_sum=0
nums_of_letters = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,100:7,1000:8}

for i in range(1,1001):
  if i < 21:
    letter_sum += nums_of_letters[i]
    print(i)
    print(letter_sum)
  elif i < 100:
    string = str(i)
    tens = int(string[0])*10
    ones = int(string[1])
    letter_sum += nums_of_letters[tens]
    if ones != 0:
      letter_sum += nums_of_letters[ones]
    print(i)
    print(letter_sum)
  elif i < 1000:
    string = str(i)
    hundreds = int(string[0])
    tens = int(string[1])*10
    ones = int(string[2])
    letter_sum += nums_of_letters[hundreds] + nums_of_letters[100]
    print(i)
    print(letter_sum)
    if tens <20 and int(string[1:]) > 0:
      letter_sum += nums_of_letters[int(string[1:])] + 3
      print(i)
      print(letter_sum)
    elif tens >= 20:
      letter_sum += nums_of_letters[tens] + 3
      print(i)
      print(letter_sum)
      if ones != 0:
        letter_sum += nums_of_letters[ones]
        print(i)
        print(letter_sum)
  else:
    letter_sum += 11
    print(i)
    print(letter_sum)