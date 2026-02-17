'''
x = 0
while x < 10:
  if x % 3 == 0:
    print("Lasers rule!")
  print(x)
  x += 1

for i in range(10):
  print(i)
'''

import numpy as np
print("All packages imported properly!")

A = np.array([100,200,300])
print(A)
print("Index 2 of A: ", A[2])
print("Type of index 2 of A: ", type(A[2]))

# A[-1] gives the last element of the array

# interactive mode "python -i [name of file]"
