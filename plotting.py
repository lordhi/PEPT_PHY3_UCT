import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


filename = "./Data/26 September/t_med_5"


def read_file(filename):
    """Reads a given file and returns the various coordinate numpy arrays."""
    file = open(filename + ".a", 'r')
    
    t = []
    x= []
    y = []
    z = []
    u = []
    
    for i,line in enumerate(file):
        if i>8:  # header lines
            splitline = line.split()
            t.append(float(splitline[0]))
            x.append(float(splitline[1]))
            y.append(float(splitline[2]))
            z.append(float(splitline[3]))
            u.append(float(splitline[4]))
            
    t = np.asarray(t)
    x= np.asarray(x)
    y= np.asarray(y)
    z= np.asarray(z)
    u= np.asarray(u)
    
    return t,x,y,z,u

    
def plot_coords(coord1, coord2, xlabel='t', ylabel='x', xlim = None, ylim = None, equal_axes = False, savefile = "plot"):
    plt.figure()
    ax =  plt.gca()
    ax.tick_params(direction = 'in')
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks_position('both')
    if xlim:
        plt.xlim(xlim[0], xlim[1])
    if ylim:
        plt.ylim(ylim[0], ylim[1])
    if equal_axes:
        plt.gca().set_aspect('equal')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    plt.plot(coord1, coord2, 'bo', markersize = 0.3)
    plt.savefig(savefile + ".png")

def plot_3d(t,x,y,z,u):
    plt.figure()
    ax = plt.axes(projection="3d")
    plot = ax.scatter3D(x,y,z, c=u, cmap = 'hsv')
    ax.view_init(azim=360)
    ax.set_aspect('equal')
    plt.colorbar(plot)
    plt.xlabel("x")
    plt.ylabel('y')
    plt.savefig('test.png')
    plt.show()

def calc_velocity(t, coord):
    v = np.zeros(len(t)-10)
    coefficients = [0.1, 0.15, 0.25, 0.25, 0.15, 0.1]
    for i in range(5, len(t)-5):
        vel = 0
        for j in range(5,-1,-1):
            vel += coefficients[j] * (coord[i+j]- coord[i+j-5])/(t[i+j]-t[i+j-5])
        v[i-5] = vel
    return v

def plot_velocity(t,x,y,z, title = "Data", savefile = "plot"):
    vx = calc_velocity(t,x)
    vy = calc_velocity(t,y)
    vz = calc_velocity(t,z)
    mag_v = np.sqrt(np.square(vx) + np.square(vy) + np.square(vz))
    
    plt.figure()
    ax =  plt.gca()
    ax.set_aspect('equal')
    ax.tick_params(direction = 'in')
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks_position('both')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    
    plt.quiver(x[5:-5],y[5:-5], vx,vy, mag_v)
    plt.colorbar()
    plt.savefig(savefile + ".png")


def main():
    t,x,y,z,u = read_file(filename)
#    plot_coords(t,z, ylabel = "z", xlim = [0,2000])
#    plot_coords(t,x, ylabel = "x", xlim = [0,2000])
#    plot_coords(t,y, ylabel = "y", xlim = [0,2000])
#    plot_coords(x,y, xlabel = "x", ylabel = "y", equal_axes = True, savefile = "xy")
#    plot_coords(x,u,xlabel = 'x', ylabel = 'u')
#    plot_coords(y,u,xlabel = 'y', ylabel = 'u')
#    plot_coords(z,u,xlabel = 'z', ylabel = 'u')
#    plot_coords(t,u,xlabel = 't', ylabel = 'u', xlim = [0,2000])
#    plot_3d(t,x,y,z,u)
    plot_velocity(t,x,y,z, title = "Quarter Mixture, 3 rps, 5 mm tracer", savefile = "q_hig_5_vplot")

if __name__ == '__main__':
    main()