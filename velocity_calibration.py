from file_reading import read_file
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

filenames = ["../Data/LSpeed","../Data/MSpeed","../Data/HSpeed"]
angular_p0s = [[1.7, 10, 0.06,-0.005],[3.2,10,0.06,-0.005],[5.1,10,0.06,-0.005]]

def f(t,omega, delta, a, c):
    return a*np.sin(omega*t+delta) + c

def magnitude(v1,v2,v3):
    return np.sqrt(np.square(v1) + np.square(v2) + np.square(v3))


def fit(func, x,y,  p0, names, u=None):
    if u is not None:
        popt, pcov = curve_fit(func, x, y, p0,u, absolute_sigma = True)
        residuals = y-func(x,*popt)
        dymin = residuals/u
    else:
        popt, pcov = curve_fit(func, x, y, p0, absolute_sigma = True)
        residuals = y-func(x,*popt)
        dymin = residuals
    
    ss_res = np.sum(np.square(residuals))
    ss_tot = np.sum((y-np.mean(y))**2)
    r_squared = 1-(ss_res/ss_tot)
    min_chisq = sum(dymin*dymin)
    dof = len(x) - len(popt)
    print('Chi square', min_chisq)
    print('Number of degrees of freedom: ', dof)
    print('Chi square per degrees of freedom: ', min_chisq/dof)
    print("R^2: ", r_squared )
    print()
    
    print('Fitted parameters with 68% C.I.:')
    
    for i, pmin in enumerate(popt):
        print("%2i %-10s %12f +/- %10f" %(i, names[i], pmin, np.sqrt(pcov[i,i])))
    print()
    return popt
    

def findAngularSpeed(t,x,u, p0):
    t = t[400:800]/1000  #Select narrow region and convert to seconds
    x = x[400:800]/1000
    u = u[400:800]/1000
    
    names = ["omega", "delta", "a", 'c']
    popt = fit(f,t,x, p0, names, u = u)
    
    ##################################################PLOTTING HERE############################################################
    plt.figure()
    plt.title("Angular fit")
    plt.plot(t,x, 'ro', markersize = 0.5)  #Plots the raw data
    tmodel = np.linspace(t[0], t[-1], 10000)
    plt.plot(tmodel, f(tmodel, *popt)) #Plots using the returned fit parameters

def findLinearVelocity(t,v_mag):
    mean = np.mean(v_mag)
    std = np.std(v_mag)
    print("Mean:", mean, " m/s - Standard deviation:", std, "m/s")
    

for i,filename in enumerate(filenames):
    print(filename)
    print("______________________________________")
    t,x,y,z,u,vx,vy,vz,uvx,uvy,uvz = read_file(filename)
    v_mag = magnitude(vx,vy,vz)
    print("______________Linear Speed______________")
    findLinearVelocity(t,v_mag)
    print("_______________Angular Speed_______________")
    findAngularSpeed(t,x,u, angular_p0s[i])
    print("______________________________________")



    

