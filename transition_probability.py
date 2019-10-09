import numpy as np
import matplotlib.pyplot as plt
from file_reading import read_file
from scipy.signal import find_peaks

def smooth_data(y, window_size):
    window = np.ones(window_size)/window_size
    smoothed_y = np.convolve(y,window,mode='same')
    return smoothed_y


filenames = ["f_hig_5","f_low_51","f_med_5", "h_hig_5", "h_hig_10","h_low_10", "h_low_51", "h_med_5", "h_med_10","q_hig_5","q_hig_10", "q_low_10", "q_low_51", "q_med_5_2", "q_med_10", "t_hig_5", "t_hig_10", "t_low_5", "t_low_10", "t_med_5", "t_med_10"]

for filename in filenames:
    bead_size = 5  #Using smallest size, since even 10mm can make 5mm changes
    
    t,x,y,z,u,vx,vy,vz,uvx,uvy,uvz = read_file("../Data/" + filename)
    
    x = smooth_data(x, 10)  # Smoothing data to make peak finding better
    
    #Can be used to plot if wanted
#    t = t[10000:30000]
#    x = x[10000:30000]
#    plt.figure()
#    plt.plot(t,x)
    
    indices, properties  = find_peaks(x, prominence = 1, distance = 30, width = 5)  # Finds peaks in x, prominence main setting, distance and width settings reduce false peaks
#    plt.plot(t[indices], x[indices] , 'ro')
    
    count = 0
    for i in range(len(indices)):  # For each peak
        try:
            if (np.absolute(x[indices[i]]-x[indices[i+1]]) > bead_size):  # maybe consider checking 2 points away for overall trends
                count+=1
#                plt.plot(t[indices[i]],x[indices[i]], 'gs')
        except IndexError: # Can't be bothered to figure out indexing
            pass 
    print(filename)
    print("Total cycles:" , len(indices))
    print("Transitions:", count)
    print("Fraction:" , count/len(indices))
