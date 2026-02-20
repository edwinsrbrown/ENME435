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
w = input("w = ")
x = input("x = ")
y = input("y = ")
z = input("z = ")
w, x, y, z = int(w), int(x), int(y), int(z)

if(w < x and y < z):
  w, y = y, w
elif(w < x and y > z):
  w, z = z, w
elif(w > x and y < z):
  x, y = y, x
elif(w > x and y > z):
  x, z = z, x

print("After swap w,x,y,z = ", w,x,y,z)


