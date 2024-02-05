test_pyramid = [[3], [7,4], [2,4,6], [8,5,9,3]]
problem_pyramid = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

biggest_sum = 0

def sumcheck(biggest_sum, new_sum):
  if new_sum > biggest_sum:
    return new_sum
  else:
    return biggest_sum
    
def pathway(pyramid, biggest_sum):
  root = 0
  for a, num_one in enumerate(pyramid[0]):
    if root-a > 0:
      pass
    else:
      for b,num_two in enumerate(pyramid[1]):
        if abs(b-a) > 1:
          pass
        elif a-b > 0:
          pass
        else:
          for c,num_three in enumerate(pyramid[2]):
            if abs(c-b) > 1:
              pass
            elif b-c > 0:
              pass
            else:
              for d,num_four in enumerate(pyramid[3]):
                if abs(d-c) >1:
                  pass
                elif c-d > 0:
                  pass
                else:
                  for e,num_five in enumerate(pyramid[4]):
                    if abs(e-d) >1:
                      pass
                    elif d-e >0:
                      pass
                    else:
                      for f,num_six in enumerate(pyramid[5]):
                        if abs(f-e) >1:
                          pass
                        elif e-f >0:
                          pass
                        else:
                          for g,num_seven in enumerate(pyramid[6]):
                            if abs(g-f) >1:
                              pass
                            elif f-g >0:
                              pass
                            else:
                              for h,num_eight in enumerate(pyramid[7]):
                                if abs(h-g) >1:
                                  pass
                                elif g-h >0:
                                  pass
                                else:
                                  for i,num_nine in enumerate(pyramid[8]):
                                    if abs(i-h) >1:
                                      pass
                                    elif h-i >0:
                                      pass
                                    else:
                                      for j,num_ten in enumerate(pyramid[9]):
                                        if abs(j-i) >1:
                                          pass
                                        elif i-j >0:
                                          pass
                                        else:
                                          for k,num_eleven in enumerate(pyramid[10]):
                                            if abs(k-j) >1:
                                              pass
                                            elif j-k >0:
                                              pass
                                            else:
                                              for l,num_twelve in enumerate(pyramid[11]):
                                                if abs(l-k) >1:
                                                  pass
                                                elif k-l >0:
                                                  pass
                                                else:
                                                  for m,num_thirteen in enumerate(pyramid[12]):
                                                    if abs(m-l) >1:
                                                      pass
                                                    elif l-m >0:
                                                      pass
                                                    else:
                                                      for n,num_fourteen in enumerate(pyramid[13]):
                                                        if abs(n-m) >1:
                                                          pass
                                                        elif m-num_eleven >0:
                                                          pass
                                                        else:
                                                          for o,num_fifteen in enumerate(pyramid[14]):
                                                            if abs(o-n) >1:
                                                              pass
                                                            elif n-o >0:
                                                              pass
                                                            else:
                                                              sum = num_one + num_two + num_three + num_four + num_five + num_six + num_seven + num_eight + num_nine + num_ten + num_eleven + num_twelve + num_thirteen + num_fourteen + num_fifteen
                                                            
                                                              biggest_sum = sumcheck(biggest_sum, sum)
                                                              print(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o)
  return biggest_sum

biggest_sum = pathway(problem_pyramid, biggest_sum)
print(biggest_sum)
      
    
    
