import numpy as np 
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Define the boundary conditions 
xi = 0
xf = 20
xeval = np.linspace(xi, xf, 100)

# Define your equations of state
def state(x,y):

    Yprime = y[1]
    Zprime = (2*y[1]+y[0]-x)/7

    return [Yprime, Zprime]

# Guess the second inital condition for trial 1 (-1 in this case)
guess1 = -1
IC_guess1 = [5,guess1]
sol1 = spi.solve_ivp(state, (xi,xf), IC_guess1, teval=xeval)

# Unpack and check the values
x1 = sol1.t
T1 = sol1.y[0]
# This line checks the temperature at the end boundary condition with your first guess
print('T(20) = ', T1[-1])

# Guess the second inital condition for trail 2 (1 in this case)
guess2 = 1
IC_guess2 = [5,guess2]
sol2 = spi.solve_ivp(state, (xi,xf), IC_guess2, teval=xeval)

# Unpack and check the values
x2 = sol2.t
T2 = sol2.y[0]
# This line checks the temperature at the end boundary condition with your second guess
print('T(20) = ', T2[-1])

# Interpolate the correct Initial condition 
actual = guess1 + ( (guess2-guess1) / (T2[-1]-T1[-1]) ) * (8 - T1[-1])
print("The actual initial condition is: ", actual)


# Use this new found conditon to find the 
IC_actual = [5,actual]
sol = spi.solve_ivp(state, (xi,xf), IC_actual, t_eval=xeval)

# Unpack and check the values
x = sol.t
T = sol.y[0]
print('T(20) = ', T[-1])

# Plot it to make sure you are correct
plt.figure()
plt.plot(x,T)
plt.xlabel("Length along the beam")
plt.ylabel("Temperature")
plt.show()