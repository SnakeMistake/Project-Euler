def ispalindrome(x):
    if str(x)[::-1] == str(x):
        return True
    else:
        return False

lychrels=[]
for i in range(1,10000):
    counter = 0
    lychrel = True
    new = i
    for x in range(50):
        new += int(str(new)[::-1])
        if ispalindrome(new):
            lychrel = False
            break
    else:
        if lychrel == True:
            lychrels.append(i)
print(lychrels)
print(len(lychrels))