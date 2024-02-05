highest_product = 1
#Opens the grid file and turns it from a string into a 2d list - 20 lists with 20 integers each.
with open('grid.txt') as x:
  data = x.read()
array_list = data.split()
grid = []
for i in range(20):
  row = []
  for num in array_list[20*i:20*i+20]:
    try:
      row.append(int(num))
    except:
      pass
  grid.append(row)
print(data)


def vert_check(grid, highest_product):
  for i in range(17):
    for x in range(20):
      product = grid[i][x] * grid[i+1][x] * grid[i+2][x] * grid[i+3][x]
      if product > highest_product:
        highest_product = product
        print(highest_product)
  return highest_product
def hor_check(grid, highest_product):
  for i in range(17):
    for x in range(20):
      product = grid[x][i] * grid[x][i+1] * grid[x][i+2] * grid[x][i+3]
      if product > highest_product:
        highest_product = product
        print(highest_product)
  return highest_product
def diag_down_check(grid, highest_product):
  for i in range(17):
    for x in range(17):
      product = grid[i][x] * grid[i+1][x+1] * grid[i+2][x+2] * grid[i+3][x+3]
      if product > highest_product:
        highest_product = product
        print(highest_product)
  return highest_product
def diag_up_check(grid, highest_product):
  for i in range(3,20):
    for x in range(17):
      product = grid[i][x] * grid[i-1][x+1] * grid[i-2][x+2] * grid[i-3][x+3]
      if product > highest_product:
        highest_product = product
        print(highest_product)
  return highest_product

highest_product = vert_check(grid, highest_product)
highest_product = hor_check(grid, highest_product)
highest_product = diag_down_check(grid, highest_product)
highest_product = diag_up_check(grid, highest_product)