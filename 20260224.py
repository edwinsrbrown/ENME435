import matplotlib.pyplot as plt

with open("20260224text.txt") as f:
  data = f.read()

data = data.split('\n')

print(data)

x = [float(row.split('')[0]) for row in data]
y = [float(row.split('')[1]) for row in data]

plt.plot(x,y)

plt.xlabel('X')
plt.ylabel('Y')

plt.title('Title Here')

plt.show()
