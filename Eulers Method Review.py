import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp

# Question 1

# step 1: state your initial conditions, time span, and step sizes
#initilize parameters
y = 1
y_prime = 1
h1 = 0.2
h2 = 0.1
t1 = np.arange(0,10,h1)
t2 = np.arange(0,10,h2)

# Step 2: Do the calculations

def Eulers_meth(init_cond1, init_cond2, h, tspan):

    # initilize your solution arrays
    x = np.zeros(len(tspan))
    dx = np.zeros(len(tspan))
    ddx = np.zeros(len(tspan))

    # initilize your initial conditions
    x[0] = init_cond1
    dx[0] = init_cond2


    for i in range(len(tspan)-1):

        # This calculates your slope of the derivative of the independent variable curve
        ddx[i] = (1-x[i]**2)*dx[i] - x[i]

        # This calculates your slope of the indepentdent variable curve
        dx[i+1] = dx[i] + ddx[i]*h

        # This calculates your independent variable value at the next step
        x[i+1] = x[i] + dx[i+1]*h

    return x, dx, ddx

sol1 = Eulers_meth(y, y_prime, h1, t1)
sol2_x, sol2_dx, sol2_ddx = Eulers_meth(y, y_prime, h2, t2)


plt.figure()
plt.plot(t1, sol1[0], label="Step size of 0.2")
plt.plot(t2, sol2_x, label="Step size of 0.1")
plt.xlabel("Time")
plt.ylabel("Y")
plt.legend()
plt.show()
