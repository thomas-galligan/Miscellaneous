import numpy as np
from matplotlib import pyplot as plt

#define the matrix describing the ellipsoid. We go for a simple example here (the pauli sigma-x matrix)

A = np.array([[3,1],[1,4]])

#v = [x,y] #position vector in R2

#generate random points in R2:

x = 100*np.random.rand(1000)
y = 100*np.random.rand(1000)
v = np.vstack((x,y))
for i in range(1000):
	for j in range(1000):
		if np.dot(np.transpose(v[:,i]),np.dot(A,v[:,i])) >=1:
			v[:,i] = 0 


plt.scatter(v[0,:],v[1,:])
plt.show()
