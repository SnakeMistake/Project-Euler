max_sum = 0
for a in range(91,100):
    for b in range(90,101):
        dig_sum = 0
        target = a**b
        for digit in str(target):
            dig_sum += int(digit)
        if dig_sum > max_sum:
            max_sum = dig_sum
print(max_sum)