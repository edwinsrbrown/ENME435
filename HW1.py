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
w = input("Input value #1: ")
x = input("Input value #2: ")
y = input("Input value #3: ")
z = input("Input value #4: ")

if(w < x):
  tv1 = w
elif(w > x):
  tv1 = x

if(y < z):
  tv2 = y
elif(y > z):
  tv2 = z

tv1,tv2 = tv2,tv1

if(w < x & y < z)
w, x, y, z = tv1, x, tv2, z
if(w < x & y > z)
w, x, y, z = tv1, x, y, tv2
if(w > x & y < z)
w, x, y, z = w, tv1, tv2, z
if(w > x & y > z)
w, x, y, z = w, tv1, y, tv2

print("w = ",w)
print("x = ",x)
print("y = ",y)
print("z = ",z)

