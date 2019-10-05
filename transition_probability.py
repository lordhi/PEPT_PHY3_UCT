import numpy as np
import matplotlib.pyplot as plt
import os
from file_reading import read_file


filename = "../Data/q_hig_10"

t,x,y,z,u,vx,vy,vz,uvx,uvy,uvz = read_file(filename)

center_x = (np.max(x) + np.min(x))/2
center_y = (np.max(y) + np.min(y))/2
print(center_x, center_y)


plt.figure()
ax1 = plt.gca()
plt.xlim(1000,10000)
ax1.plot(t,np.square(x-center_x)+np.square(y-center_y), 'bo', markersize = 0.3)

ax2 = ax1.twinx()
ax2.plot(t,x, 'ro', markersize = 0.3)



plt.figure()
plt.gca().set_aspect("equal")
plt.plot(x,y, 'bo')