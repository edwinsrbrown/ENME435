'''
Edwin Brown
UID: 118892924
2/20/2026
HW1
'''
'''
# Q3
print("Q3")
import random as rand

i = 0
z = 0
while i < 10000:
  i += 1 # increment i so we get 10,000 loops
  x = rand.randint(1,6) # select random value form 1-6
  y = rand.randint(1,6)
  if(x == y):
    z += 1 # increment z whenever doubles appears
print("The percentage of rolls that are doubles are: ", z/i *100) 

# Q4
print("Q4")
w = input("w = ")
x = input("x = ")
y = input("y = ")
z = input("z = ")
w, x, y, z = int(w), int(x), int(y), int(z) # converts string inputs into ints

if(w < x and y < z):
  w, y = y, w # swap smaller value variables (4 different cases)
elif(w < x and y > z):
  w, z = z, w
elif(w > x and y < z):
  x, y = y, x
elif(w > x and y > z):
  x, z = z, x

print("After swap w,x,y,z = ", w,x,y,z)

# Q5
print("Q5")
list = [] # initalize numbers as an empty list
for i in range(10):
  number = input("Enter number: ")
  list.append(number)
'''
# Q6
print("Q6")
x = input("Enter a number: ")
for i in range(x):
  print("A", end ='')
'''
# Q7
print("Q7")
'''

      
      


