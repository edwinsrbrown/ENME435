'''
command prompt syntax:

python -i 20260210.py --> makes the anaconda prompt itself interactive (e.g. can call variables and it will print values)
exit() --> used to leave a script, necessary for leaving interactive mode
cls --> clears screen of previous commands on prompt

python syntax:

\t --> create a ta of space 
\n --> move following info to a new line
'''

A = 100.1
print("The value of A is: ",A)
print(type(A))

B = int(A)
print(type(B))

print('    *')
print('   * *')
print('  *****')
print(' *     *')
print('*       *')

print("The answer is: ", (14*12)/(33*144-187))

C = "World Lidar Day"
print(C)

D = "World Lidar \tDay"
print(D)

E = "World Lidar \nDay"
print(E)
