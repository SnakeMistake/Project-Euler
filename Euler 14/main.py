max_len = 5
starting_num = 1

def collatz(num, max_len):
  list = [num]
  while num > 1:
    if num%2 ==0:
      num = num/2
      list.append(num)
    else:
      num = (num*3)+1
      list.append(num)
  if len(list) > max_len:
    print(f"Length: {len(list)}, starting number: {list[0]}")
    return list[0], len(list)
  else:
    return starting_num, max_len

for i in range(1000000):
  starting_num, max_len = collatz(i, max_len)