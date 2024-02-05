f = open("0059_cipher.txt",mode="r").read().split(",")

text = ""
offset_a = 97
offset_b = 97
offset_c = 97




while "number" not in text and offset_c < 125:
	offset_a+=1
	if offset_a>122:
		offset_a = 97
		offset_b +=1
	if offset_b > 122:
		offset_b = 97
		offset_c +=1
	test = []
	for i,item in enumerate(f):
		if i%3 == 0:
			test.append(chr(int(item)^offset_a))
		if i%3 == 1:
			test.append(chr(int(item)^offset_b))
		if i%3 ==2:
			test.append(chr(int(item)^offset_c))
	text = "".join(test)

print(f'{offset_a=}{offset_b=}{offset_c=}')
print(text)
sum = 0
for char in text:
	sum+= ord(char)

print(sum)
