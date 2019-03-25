import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import timeit
import math


start = timeit.default_timer()

N = 100
dx = 2*np.pi/N

def explicit(gamma):
	dt = gamma*dx**2



	x = np.linspace(0, 2*math.pi-dx, 100)
	t = np.arange(0, 2, dt)


	T = np.zeros((len(t), N))

	for i in range(N):
	    T[0][i] = np.cos(x[i])**3
	 

	for i in range(len(t)-1):
	    for j in range(N):
	            
	        if j == N-1:
	            T[i+1][j] = T[i][j]+gamma*(T[i][0]-2*T[i][j]+T[i][j-1])
	        elif j == 0:
	            T[i+1][j] = T[i][j]+gamma*(T[i][j+1]-2*T[i][j]+T[i][N-1])
	        else:
	            T[i+1][j] = T[i][j]+gamma*(T[i][j+1]-2*T[i][j]+T[i][j-1])

g = np.linspace(0.2, 0.49, 5)

plt.plot(g, explicit(g))
plt.show()
	            
stop = timeit.default_timer()

print('Time: ', stop - start)  
print max(Error)







    
