import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import timeit


start = timeit.default_timer()

N = 100
dx = 2*np.pi/N
dt = 0.49*(dx**2)
gamma = dt/(dx**2)


x = np.linspace(0, 2*np.pi-dx, 100)
t = np.arange(0, 2, dt)


T = np.zeros((len(t), N))

for i in range(N):
    T[0][i] = np.cos(x[i])**3
    
for i in range(1,len(t)):
    for j in range(N):
        
        T[i][j] = T[i-1][j]
        
    for z in range(N):    
        for k in range(N):
        
            if k == 0:
                T[i][k] = 1/(1+gamma)*(T[i-1][k]+(gamma/2)*(T[i][k+1]+T[i][N-1]+T[i-1][k+1]-2*T[i-1][k]+T[i-1][N-1]))
            
            elif k == N-1:
                T[i][k] = 1/(1+gamma)*(T[i-1][k]+(gamma/2)*(T[i][0]+T[i][k-1]+T[i-1][0]-2*T[i-1][k]+T[i-1][k-1]))
            
            else:
                T[i][k] = 1/(1+gamma)*(T[i-1][k]+(gamma/2)*(T[i][k+1]+T[i][k-1]+T[i-1][k+1]-2*T[i-1][k]+T[i-1][k-1]))
            
            

stop = timeit.default_timer()

print('Time: ', stop - start)  

