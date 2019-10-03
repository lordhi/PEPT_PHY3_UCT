import numpy as np

def read_file(filename, exclude_boundary = 0):
    """Reads a given file and returns the various coordinate numpy arrays."""
    file = open(filename + ".b", 'r')
    data = []
    for i in range(11):
        data.append([])
    data = list(data)

    file.readline() #headerline
    for line in file:
        splitline = list(map(float, line.split()))
        for i in range(11):
            data[i].append(splitline[i]) 
    for j in range(11):
        data[j] = data[j][5:-5]

    data = list(map(np.asarray, data))
    if exclude_boundary > 0:
        minz = np.min(data[3])
        maxz = np.max(data[3])
        a = data[3]
        for i in range(len(data)):
            data[i] = data[i][np.logical_and(np.greater(a, minz+exclude_boundary), np.less(a, maxz - exclude_boundary))]
    return data
