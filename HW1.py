'''
# Q3
import random as rand

i = 0
z = 0
while i < 10000:
  i += 1
  x = rand.randint(1,6)
  y = rand.randint(1,6)
  if(x == y):
    z = z + 1
print("The percentage of rolls that are doubles are: ", z/i *100)
'''
# Q4
import numpy as np

tv1 = 0;
tv2 = 0;
w = input("w = ")
x = input("x = ")
y = input("y = ")
z = input("z = ")
w, x, y, z = int(w), int(x), int(y), int(z)

if(w < x & y < z):
  tv1 = w
  tv2 = y
  w, x, y, z = tv2, x, tv1, z
if(w < x & y > z):
  tv1 = w
  tv2 = z
  w, x, y, z = tv2, x, y, tv1
if(w > x & y < z):
  tv1 = x
  tv2 = y
  w, x, y, z = w, tv2, tv1, z
if(w > x & y > z):
  tv1 = x
  tv2 = z
  w, x, y, z = w, tv2, y, tv1

print("After swap w,x,y,z = ",w,x,y,z)


