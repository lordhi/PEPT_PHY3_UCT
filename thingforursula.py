from file_reading import read_file
from mayavi import mlab

t,x,y,z,u,vx,vy,vz,uvx,uvy,uvz = read_file("../Data/h_med_5")
mlab.figure( size=(1000,800))
mlab.quiver3d(x,y,z,vx,vy,vz)
mlab.vectorbar(title="Velocity (metres per second)", orientation='Vertical', nb_labels=4)
mlab.show()