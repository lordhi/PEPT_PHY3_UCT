import numpy as np
import matplotlib.pyplot as plt
from file_reading import read_file

def get_centers (image):
	x = []
	y = []
	counts = image.get_array()
	ncnts = np.count_nonzero(np.power(10,counts))
	verts = image.get_offsets()
	for offc in range(verts.shape[0]):
		binx,biny = verts[offc][0],verts[offc][1]
		if counts[offc]:
			x.append(binx)
			y.append(biny)


	return np.asarray(x), np.asarray(y)

def plotVelocities(x,y,vx,vy, gridsize=100):
	v = np.sqrt(np.square(np.asarray(vx)) + np.square(np.asarray(vy)))
	xplot = plt.hexbin(x,y,C=vx, gridsize=gridsize)
	yplot = plt.hexbin(x,y,C=vy, gridsize=gridsize)
	plt.colorbar()

	xdata = xplot.get_array()
	ydata = yplot.get_array()
	for i in range(len(xdata)):
		factor = (xdata[i]**2 + ydata[i]**2)**0.5
		xdata[i] /= factor
		ydata[i] /= factor

	x,y = get_centers(xplot)

	plt.figure()
	plt.xlim([-90,70])
	plt.ylim([70,210])
	plt.gca().set_aspect('equal')

	plt.quiver(x,y, xdata, ydata, headwidth=3, headlength=2, headaxislength=1.5)
	plt.show()

__,x,y,__,__,vx,vy,__,__,__,__ = read_file("../Data/q_hig_10")
plotVelocities(x,y,vx,vy, gridsize=50)