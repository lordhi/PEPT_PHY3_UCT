from file_reading import read_file
from mayavi import mlab
import matplotlib.pyplot as plt
import numpy as np
import hexbin

t,x,y,z,u,vx,vy,vz,uvx,uvy,uvz = read_file("../Data/h_med_5")

mlab.quiver3d(x,y,z, vx, vy, vz)
mlab.vectorbar(title="Velocity (metres per second)", orientation='Vertical', nb_labels=4)
mlab.show()