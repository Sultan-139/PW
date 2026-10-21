"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv (columns time, concentration) into arrays t, C.
#         Set C0 = the first concentration.

data = np.loadtxt('kinetics.csv', delimiter=',', skiprows=1)
t = data[:, 0]
C = data[:, 1]
C0 = C[0]

# TODO 2: write total_error(k) = sum of (measured - C0*exp(-k*t))^2.
#         This is the "how bad" number: small when the model matches the data.
def error(k):
    a = np.sum((C - C0 * np.exp(-k * t)) ** 2)
    return a

# TODO 3: minimise total_error with scipy.optimize.minimize (method "SLSQP",
#         bounds [(0, 5)], start x0=0.5). Print the fitted k.
a = minimize(error, x0=0.5, method="SLSQP", bounds=[(0, 5)])
result = a.x[0]
print(result)
# TODO 4: plot the measured data (points) and your fitted curve (line) together.
#         Save as kinetics.png.
plt.figure(figsize=(8, 5))
plt.scatter(t, C, color='red', label='Measured data')

t_curve = np.linspace(t.min(), t.max(), 100)
C_curve = C0 * np.exp(-result * t_curve)
plt.plot(t_curve, C_curve, color='blue', label=f'Fitted curve (k ≈ {result:.2f})')

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title('First-Order Reaction Kinetics')
plt.legend()
plt.grid(True)
plt.savefig('kinetics.png')
plt.close()