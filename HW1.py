import random as rand
'''
# Q3
print("Q3")
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
'''
# Q5
print("Q5")
list = [] # initalize empty lists
noDupList = []
for i in range(10):
  number = int(input("Enter number: "))
  list.append(number)

noDupList = set(list) # removes duplicate numbers/entries
noDupList.sort() # sorts list in order from smallest to highest value
small1 = noDupList[0]
small2 = noDupList[1]
print("The two smallest numbers are: ", small1, small2)
'''
# Q6
print("Q6")
x = input("Enter a number: ")
for i in range(int(x)): # converts string input into int
  print("A", end ='') # print A however many times user input is

# Q7
print("Q7")
j = 0
x = 10
while j < 50:
  for i in range(x):
    y = rand.randint(0,1)
    print(y, end ='')
  print()
  x += 1
  j += 1

# Q8
print("Q8")
numbers = 0;
y = False;

while 1: # infinite loop
  x = int(input("Enter the numbers 1-10 in any sequence:  "))
  numbers += 1 # count each input

  if x < 3:
    y = True # idnetifies whenever a number less than 3 is inputted

  if x == 5:
    break # break infinite loop if a 5 is inputted

print("The total numbers entered is ", numbers)

if y == True: # print yes or no depending on inputs
  print("Yes, a number less than 3 was entered")
elif y == False:
  print("No, there was not a number less than 3 entered")
'''       


      
      


