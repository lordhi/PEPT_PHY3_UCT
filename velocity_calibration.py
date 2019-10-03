from file_reading import read_file
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

###Things I still want to check - How to handle uncertainties on speed - 10%/standard deviation/propagate
###Should I make Gaussian fit to histogram or is mean good enough

filenames = ["../Data/LSpeed","../Data/MSpeed","../Data/HSpeed"]
p0s = [[1.7, 10, 0.06,-0.005],[3.2,10,0.06,-0.005],[5.1,10,0.06,-0.005]]

#def gauss(x, A, sigma, mu):
#    return (A/(sigma*np.sqrt(2*np.pi)))*np.exp((-1/2)*np.square((x-mu)/sigma))

def f(t,omega, delta, a, c):
    return a*np.sin(omega*t+delta) + c

def magnitude(v1,v2,v3):
    return np.sqrt(np.square(v1) + np.square(v2) + np.square(v3))

#def fit(func, x,y, u, p0):
#    popt, pcov = curve_fit(func, x, y, p0,u, absolute_sigma = True)
#        
#    residuals = y-func(x,*popt)
#    dymin = residuals/u
#    ss_res = np.sum(np.square(residuals))
#    ss_tot = np.sum((y-np.mean(y))**2)
#    r_squared = 1-(ss_res/ss_tot)
#    min_chisq = sum(dymin*dymin)
#    dof = len(x) - len(popt)
    
#    return popt, pcov, min_chisq/dof, r_squared

def findLinearVelocity(t,vx,vy,vz):
    v_mag = magnitude(vx,vy,vz)
    plt.figure()
    plt.xlabel("t (ms)")
    plt.ylabel("Linear velocity (m/s)")
    plt.plot(t, v_mag, 'bo', markersize = 0.3, alpha = 0.3)
    mean = np.mean(v_mag)
    uvmag = np.std(v_mag)
    
    
    print("Mean:", mean, " m/s - Standard deviation:", uvmag, "m/s")
    
    plt.plot(t, np.ones(t.shape) * mean)
    plt.plot(t, np.ones(t.shape) * (mean+uvmag))
    plt.plot(t, np.ones(t.shape) * (mean-uvmag))

def findAngularSpeed(t,x,u, p0):
    t = t[400:800]/1000
    x = x[400:800]/1000
    u = u[400:800]/1000
    
    plt.figure()
    plt.plot(t,x, 'ro', markersize = 0.5)
    
    names = ["omega", "delta", "a", 'c']
    popt, pcov = curve_fit(f, t, x,  p0, u,  absolute_sigma = True)
    
    residuals = x-f(t,*popt)
    dymin = residuals/u
    ss_res = np.sum(np.square(residuals))
    ss_tot = np.sum((x-np.mean(t))**2)
    r_squared = 1-(ss_res/ss_tot)
    min_chisq = sum(dymin*dymin)
    dof = len(t) - len(popt)
    print('Chi square', min_chisq)
    print('Number of degrees of freedom: ', dof)
    print('Chi square per degrees of freedom: ', min_chisq/dof)
    print("R^2: ", r_squared )
    print()
    
    print()
    print('Fitted parameters with 68% C.I.:')
    
    for i, pmin in enumerate(popt):
        print("%2i %-10s %12f +/- %10f" %(i, names[i], pmin, np.sqrt(pcov[i,i])*np.sqrt(min_chisq/dof)))
    print()
    
    
    tmodel = np.linspace(t[0], t[-1], 10000)
    plt.plot(tmodel, f(tmodel, *popt)) 
    
#def test(t,x,u, p0):
#    t = np.arange(8,15, 0.01)
#    x = f(t,2.5,-3,0.06,0)
#    u = np.ones(t.shape)*0.1*x
#    plt.plot(t,x)
#    
#    names = ["omega", "delta", "a"]
#    popt, pcov = curve_fit(f, t, x,  p0, u,  absolute_sigma = True)
#    
#    residuals = x-f(t,*popt)
#    dymin = residuals/u
#    ss_res = np.sum(np.square(residuals))
#    ss_tot = np.sum((x-np.mean(t))**2)
#    r_squared = 1-(ss_res/ss_tot)
#    min_chisq = sum(dymin*dymin)
#    dof = len(t) - len(popt)
#    print('Chi square', min_chisq)
#    print('Number of degrees of freedom: ', dof)
#    print('Chi square per degrees of freedom: ', min_chisq/dof)
#    print("R^2: ", r_squared )
#    print()
#    
#    print()
#    print('Fitted parameters with 68% C.I.:')
#    
#    for i, pmin in enumerate(popt):
#        print("%2i %-10s %12f +/- %10f" %(i, names[i], pmin, np.sqrt(pcov[i,i])*np.sqrt(min_chisq/dof)))
#    print()
#    
#    
#    tmodel = np.linspace(t[0], t[-1], 10000)
#    plt.plot(tmodel, f(tmodel, *popt)) 

for i,filename in enumerate(filenames):
    print(filename)
    print("________________________________")
    t,x,y,z,u,vx,vy,vz,uvx,uvy,uvz = read_file(filename)
    findLinearVelocity(t,vx,vy,vz)
    findAngularSpeed(t,x,u, p0s[i])
    print("_________________________________")
    #test(t,x,u)



    

