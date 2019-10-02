import numpy as np

def read_file(filename):
    """Reads a given file and returns the various coordinate numpy arrays."""
    file = open(filename + ".b", 'r')
    
    t = []
    x= []
    y = []
    z = []
    u = []
    vx = []
    vy = []
    vz = []
    uvx = []
    uvy = []
    uvz = []
    file.readline() #headerline
    for i,line in enumerate(file):
        splitline = line.split()
        t.append(float(splitline[0]))
        x.append(float(splitline[1]))
        y.append(float(splitline[2]))
        z.append(float(splitline[3]))
        u.append(float(splitline[4]))
        vx.append(float(splitline[5]))
        vy.append(float(splitline[6]))
        vz.append(float(splitline[7]))
        uvx.append(float(splitline[8]))
        uvy.append(float(splitline[9]))
        uvz.append(float(splitline[10]))
            
    t = np.asarray(t)
    x= np.asarray(x)
    y= np.asarray(y)
    z= np.asarray(z)
    u= np.asarray(u)
    vx= np.asarray(vx)
    vy= np.asarray(vy)
    vz= np.asarray(vz)
    uvx= np.asarray(uvx)
    uvy= np.asarray(uvy)
    uvz= np.asarray(uvz)
    
    return t,x,y,z,u,vx,vy,vz,uvx,uvy,uvz