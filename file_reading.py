import numpy as np

def read_file(filename):
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
    data = tuple(map(np.asarray, data))
    return data