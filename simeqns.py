# --------------------------------------------
# Tom Galligan, 10/9/17, University of Oxford
# --------------------------------------------
# code to solve the simultaneous equations in Q8 on B2 PS1.
# To run, simply type 'python simeqns.py N' into the command line, replacing 
# N with the number of function evaluations in each dimension you 
# wish to do (works well with 100).

import numpy as np
import matplotlib.pyplot as plt
import os,sys
c=299792458 # define constants to be used later
lp = 420.2e-9
ln = 700.1e-9
l0 = 448.1e-9
n=int(sys.argv[1]) # read in command line argument (number of data points per dimension)
theta = np.linspace(0,180,n)*np.pi/180 # construct the grid of points we're sampling
v = np.linspace(0,c-1,n) # c-1 to avoid div/zero error
R = np.zeros((n,n)) # initialise 

def gamma(u): # define the lorentz factor
	return (1-(u/c)**2)**(-0.5) 

def residual(V,THETA): # define the residual function
	
	return (np.abs(lp-l0*gamma(V)*(1+(V/c)*np.cos(THETA))) + 
		np.abs(ln-l0*gamma(V)*(1-(V/c)*np.cos(THETA))))

for i in range(n): # calculate residual at each point in the grid 
	for j in range(n):
		R[i,j] = residual(v[i],theta[j])

v_ind, theta_ind = np.unravel_index(R.argmin(), R.shape) # find point in the grid with lowest residual
v_best = v[v_ind] # find corresponding v and theta
theta_best = theta[theta_ind]

print 'v = ', v_best, ', theta = ', theta_best*180/np.pi, 'degrees'

#check
lp_check = l0*gamma(v_best)*(1+(v_best/c)*np.cos(theta_best))
ln_check = l0*gamma(v_best)*(1-(v_best/c)*np.cos(theta_best))

print 'lp = ', lp_check, ', ln = ', ln_check

np.savetxt('R.dat',R) # save residual array for plotting if you like. Easiest in matlab.