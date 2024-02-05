#This is an "n choose k" combinatorics problem -- n factorial divided by k factorial times n-k factorial ---

n_fact = 1
k_fact = 1
n_minus_k_fact = 1

for i in range(1,41):
  n_fact *= i

for i in range(1,21):
  k_fact *= i

for i in range(1,21):
  n_minus_k_fact *= i

answer = (n_fact)/(k_fact*n_minus_k_fact)

print(answer)