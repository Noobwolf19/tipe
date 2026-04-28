import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

# Méthode par équation du second degré

V_0 = 25
alpha = 1
têta = ...
h = 1.80
g = 9.81
x_0 = ...
z_0 = ...

# Equation trajectoire y(x) INUTILE POUR LE MOMENT
def equation_traj_y(X):
    return -g / (2 * (V_0 * np.cos(alpha))**2) * X**2 + np.tan(alpha) * X + h

# Résout l'équation du mouvement pour obtenir la portée de la balle
def solve_eq (V_0, h):
    a = -g / (2 * (V_0 * np.cos(alpha))**2)
    b = np.tan(alpha)
    c = h
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("Xavier")
        return None
    x_1 = (-b - np.sqrt(delta)) / (2 * a)
    x_2 = (-b + np.sqrt(delta)) / (2 * a)
    x_max = max(x_1, x_2)
    if x_max < 0:
        print("Marion")
        return None
    return x_max


V_0 = 35
x = np.linspace(0, 115, 230)
y = np.array([equation_traj_y(i) for i in x])

plt.figure()
plt.plot(x, y)






plt.show()