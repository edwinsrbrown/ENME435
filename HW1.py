# Q3
import random as rand

i = 0
z = 0;
while i < 10000:
  i++
  x = rand.randint(1,6)
  y = rand.randint(1,6)
  if (x == y):
    z++
print("The percentage of rolls that are doubles are: ", z/i *100)
