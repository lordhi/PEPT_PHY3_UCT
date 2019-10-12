import numpy as np
import matplotlib.pyplot as plt
from file_reading import read_file

def bin(x,y,z, xmin, xmax, xstep, zmin, zmax, zstep, number_of_highest_to_take=20):
	binnedPoints = []

	for i in range(xmin, xmax, xstep):
		row = []
		for j in range(zmin, zmax, zstep):
			point = []
			for c in range(len(x)):
				if x[c] > i and x[c] < i+xstep:
					if z[c] > j and z[c] < j+zstep:
						point.append(y[c])
			if len(point) > number_of_highest_to_take:
				point = sorted(point)[:number_of_highest_to_take]
			row.append(point)
		binnedPoints.append(row)

	return binnedPoints