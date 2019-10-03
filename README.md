# PEPT_PHY3_UCT
All Java files are for preprocessing data and can be ignored for non-computational groups
processData.py is also a preprocessing script and can be ignored

Runs gives the breakdown of all the data that was taken, when it was taken and the naming convention.

file_reading.py is a module which can be imported in order to read the data files without needing to concern yourself for the formatting.
Data is returned as a tuple of arrays as follows:
  (time, xposition, yposition, zposition, uncertainty_on_position, x_velocity, y_velocity, z_velocity, uncertainty_x_velocity, uncertainty_y_velocity, uncertainty_z_velocity)

Hexbin.py is for binning and plotting. Its main function plots the velocities on a quiver plot, binned hexagonally
plotitng.py has some general purpose plotting functions
