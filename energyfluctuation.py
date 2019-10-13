from file_reading import read_file
import matplotlib.pyplot as plt
import numpy as np

def twoD_binned_energy_fluctuations(x,y,z,vx,vy,vz, zmin, zstep, xmin, xstep):
	'''Bins data by z and x coordinates. If you need to bin by z and y, simply swap x and y when using the function'''
	data = list(zip(x,y,z,vx,vy,vz))
	zmax = max(z)
	xmax = max(x)

	zbins = []
	xbins = []

	zbins.append(zmin)
	xbins.append(xmin)

	while (zbins[-1] < zmax):
		zbins.append(zbins[-1] + zstep)
	while (xbins[-1] < xmax):
		xbins.append(xbins[-1] + xstep)

	binnedData = []
	for i in range(len(zbins)):
		binnedData.append([])
		for j in range(len(xbins)):
			binnedData[i].append([[],[],[]])

	for i in range(len(data)):
		a = int((data[i][2] - zmin)/zstep)
		b = int((data[i][0] - xmin)/xstep)

		if a >= 0 and a < zbins[-1]:
			if b >= 0 and b < xbins[-1]:
				val = data[i]
				binnedData[a][b][0].append(val[3])
				binnedData[a][b][1].append(val[4])
				binnedData[a][b][2].append(val[5])

	i = len(binnedData)-1
	while i > 0:
		flag = True
		for j in range(len(binnedData[i])):
			if binnedData[i][j] != [[],[],[]]:
				flag = False
		if flag:
			del binnedData[i]
			del zbins[-1]
		else:
			break
		i -= 1

	i = len(binnedData[0])-1
	while i > 0:
		flag = True
		for j in range(len(binnedData)):
			if binnedData[j][i] != [[],[],[]]:
				flag = False
		if flag:
			for j in range(len(binnedData)):
				del binnedData[j][-1]
			del xbins[-1]
		else:
			break
		i -= 1

	x_variances = []
	y_variances = []
	z_variances = []
	for i in range(len(binnedData)):
		x_variances.append([])
		y_variances.append([])
		z_variances.append([])
		for j in range(len(binnedData[i])):
			val = binnedData[i][j]
			if len(val) > 0 and len(val[0]) > 0:
				x_variances[i].append(calcvariance(val[0]))
				y_variances[i].append(calcvariance(val[1]))
				z_variances[i].append(calcvariance(val[2]))
			else:
				x_variances[i].append(0)
				y_variances[i].append(0)
				z_variances[i].append(0)

	x_variances = np.asarray(x_variances)
	y_variances = np.asarray(y_variances)
	z_variances = np.asarray(z_variances)

	return zbins, xbins, x_variances, y_variances, z_variances

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
	zbins, xbins, x_variances, y_variances, z_variances = twoD_binned_energy_fluctuations(x,y,z,vx,vy,vz,min(z),1, min(x),1)

	plt.figure()
	plt.contourf(xbins, zbins,x_variances)
	plt.colorbar()
	plt.xlim(xbins[0], xbins[-1])
	plt.ylim(zbins[0], zbins[-1])
	plt.show()

if __name__ == '__main__':
	plot_variances("../Data/h_hig_5")