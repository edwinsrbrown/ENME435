import numpy as np
import matplotlib.pyplot as plt

#2
raw_data = np.loadtxt("imudata.txt")

#3
pitch_angle = raw_data[:,4] # 4 is 5th column
x = np.arrange(len(pitch_angle)) # gets 0 - length of pitch angle

#4
plt.plot(x, pitch_angle)
plt.xlabel("Point of Data")
plt.ylabel("Pitch Angles (Degrees)")
plt.title("Raw Pitch Angle of Accelerometer vs Degrees")
plt.legend()
plt.show()

#5
def moving_avg(data, pt):
  stored_avgs = []
  for i in range(len(data) - pt + 1) # e.g. 10 numbers w/ 2-pt moving avg = 9 ranges
    for j in range(pt) # necessary to add values within each range
      total += data[i + j] # used to add up all the numbers in one range
    avg = total / pt # get the average of one of the ranges
    stored_avgs.append(avg) # put each avg into an array

return np.array(stored_avgs)

#6
pt = [2,4,8,16,64,128] # moving average pt ranges

for window in pt:
  pitch_avg = moving_avg(pitch_angle, window)
  x_new = np.arrange(len(pitch_avg) # new length = length of averaged pitch values
  #7          
  mean = np.mean(pitch_avg)
  std = np.std(pitch_avg)

plt.plot(x, pitch_angle)
plt.plot(x_new, pitch_avg)
plt.xlabel("Point of Data")
plt.ylabel("Pitch Angles (Degrees)")
plt.title("Moving Average of Raw Pitch Angle of Accelerometer vs Degrees")
plt.legend()
plt.text(f"Mean = {mean}\nStd = {std}") 
plt.show()
  
                  
      
  
  
