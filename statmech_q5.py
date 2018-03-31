import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define the expression whose roots we want to find

a = 0.5
R = 1.6

func = lambda x : -8/3 - 6/(np.exp(6*x)-1)+1/(np.exp(x)-1) 

# Plot it

x = np.linspace(-1, 1, 201)

plt.plot(x, func(x))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()

# Use the numerical solver to find the roots

x_initial_guess = -0.1
x_solution = fsolve(func, x_initial_guess)

print "The solution is x = %f" % x_solution
print "at which the value of the expression is %f" % func(x_solution)