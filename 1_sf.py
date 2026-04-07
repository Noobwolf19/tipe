import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

# Méthode par équation du second degré

V_0 = ...
alpha = ...
têta = ...
h = ...
g = 9.81
x_0 = ...
y_0 = ...
z_0 = ...

def equation_traj_y(X):
    return -g / (2 * (V_0 * np.cos(alpha))**2) * X**2 + np.tan(alpha) * X + h


def solve_eq (y):
    delta = (np.tan(alpha))**2 - 4 * h * (-g/(2*(V_0*np.cos(alpha))**2))
    if delta < 0:
        print("Xavier")
    else:
        x_1 = (-(np.tan(alpha)) - np.sqrt(delta))/2*(-g/(2*(V_0*np.cos(alpha))**2))
        x_2 = (-(np.tan(alpha)) + np.sqrt(delta))/2*(-g/(2*(V_0*np.cos(alpha))**2))
        x_max = max(x_1, x_2)
        if x_max < 0:
            print("Marion")
        else :
            return x_max

def bite(n):
    return None