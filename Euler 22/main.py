with open('names.txt') as x:
  contents = x.read()

#cleanup - removing quotes and commas.  Turning into a list.
contents = contents.replace(',', " ")
contents = contents.replace('"',"")
names_list =contents.split()
print(names_list)

#dictionary to set up the values for each letter in the alphabet
letter_values = {
  "a":1,
  "b":2,
  "c":3,
  "d":4,
  "e":5,
  "f":6,
  "g":7,
  "h":8,
  "i":9,
  "j":10,
  "k":11,
  "l":12,
  "m":13,
  "n":14,
  "o":15,
  "p":16,
  "q":17,
  "r":18,
  "s":19,
  "t":20,
  "u":21,
  "v":22,
  "w":23,
  "x":24,
  "y":25,
  "z":26,
}
#smaller list to test the functionality
test_list = ["tom", "charlie", "alvin"]

#Missed this step originally - alphabetizing the names list
names_list.sort()

#Sets up a total and then adds up each letter in the name according to the dictionary above.  Afterward, it multiplies the name by the index+1 to give the position in the list.  
total = 0
for i,name in enumerate(names_list):
  name_sum = 0
  for letter in name.lower():
    name_sum += letter_values[letter]
  print(f'the sum of the letters in {name} is {name_sum}')
  name_product = name_sum*(i+1)
  print(f'the number of the name is {i+1} and the product is {name_product}')
  total += name_product
  print(f'the total is now {total}')

print(total)
  
  