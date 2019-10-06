import numpy as np
import matplotlib.pyplot as plt
from file_reading import read_file
from scipy.signal import find_peaks

filename = "../Data/t_hig_10"
bead_size = 5

t,x,y,z,u,vx,vy,vz,uvx,uvy,uvz = read_file(filename)

plt.plot(t,x)

indices, properties  = find_peaks(x, height = 0, distance = 100, width = 5)
plt.plot(t[indices], x[indices] , 'ro')

count = 0
for i in range(len(indices)):
    try:
        if (np.absolute(x[indices[i]]-x[indices[i+1]]) > bead_size):
            count+=1
            plt.plot(t[indices[i]],x[indices[i]], 'gs')
    except IndexError:
        pass
print(count)
