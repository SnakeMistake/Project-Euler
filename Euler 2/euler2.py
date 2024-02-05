fib_list = [1,2]
even_fibs = []
while max(fib_list) <= 4000000:
    fib_list.append(fib_list[-1]+fib_list[-2])

for term in fib_list:
  if term%2 ==0:
    even_fibs.append(term)
print(fib_list)
print(even_fibs)
print(sum(even_fibs))