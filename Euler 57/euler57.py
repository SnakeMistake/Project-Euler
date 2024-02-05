from fractions import Fraction

series = [Fraction(1,2)]
net_series = []
def expanddenoms(n):
    for i in range(n):
        new_denom = series[-1] + 2
        new_frac = Fraction(1,new_denom)
        series.append(new_frac)
        net_series.append(new_frac+1)



expanddenoms(1000)
counter = 0
for item in net_series:
    if len(str(item.numerator)) > len(str(item.denominator)):
        counter +=1

print(counter)