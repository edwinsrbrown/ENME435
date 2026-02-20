# Q3
import random as rand

i = 0
z = 0;
while i < 10000:
  i = i + 1
  x = rand.randint(1,6)
  y = rand.randint(1,6)
  if (x == y):
    z = z + 1
print("The percentage of rolls that are doubles are: ", z/i *100)
