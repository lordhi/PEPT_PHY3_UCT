from file_reading import read_file
import matplotlib.pyplot as plt
import numpy as np

def energy_fluctuation(x,y,z,vx,vy,vz, zmin, zstep):
	'''Returns a 2D array, where each row gives a z value and variance in x,y and z velocity'''
	data = sorted(list(zip(x,y,z,vx,vy,vz)), key=lambda x: x[2])
	
	fluctuations = ([],[],[],[])

	currentZ = zmin
	i = 0
	c = 0

	while i < len(data):
		fluctuations[0].append(currentZ)
		for i in range(1,4):
			fluctuations[i].append([])

		while(i < len(data) and data[i][2] <= currentZ + zstep):
			val = data[i][3]
			fluctuations[1][c].append(val)
			fluctuations[2][c].append(data[i][4])
			fluctuations[3][c].append(data[i][5])

			i+= 1

		c += 1
		currentZ += zstep
	variance = [[],[],[],[]]
	for i in range(len(fluctuations[0])):
		variance[0].append(fluctuations[0][i])
		variance[1].append(calcvariance(fluctuations[1][i]))
		variance[2].append(calcvariance(fluctuations[2][i]))
		variance[3].append(calcvariance(fluctuations[3][i]))

	variance = tuple(map(np.asarray, variance))

	return variance

def calcvariance(velocities):
	if len(velocities) > 0:
		velocities = np.asarray(velocities)
		velocities = velocities - np.mean(velocities)
		velocities = np.square(velocities)
		var = sum(velocities)/len(velocities)
		return var
	return 0

def plot_variances(filename):
	_,x,y,z,_,vx,vy,vz,_,_,_ = read_file(filename)
	zsteps, x_variance, y_variance, z_variance = energy_fluctuation(x,y,z,vx,vy,vz,min(z),1)

	plt.figure()
	plt.plot(zsteps, x_variance, label="x")
	plt.plot(zsteps, y_variance, label="y")
	plt.plot(zsteps, z_variance, label="z")
	plt.legend()
	plt.show()

if __name__ == '__main__':
	plot_variances("../Data/h_hig_10")