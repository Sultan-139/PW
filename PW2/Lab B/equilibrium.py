"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.
def k_imbalance(x):
    return (2*x)**2 / ((a - x)* (b - x)) - K
# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.
n = newton(k_imbalance,x0 = 0.5)

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.
def obj_func(x):
    return k_imbalance(x[0]) ** 2
# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.
nH2 = a - n
nI2 = b - n
nHI = 2 * n

print(f"  H2: {nH2:.4f} mol")
print(f"  I2: {nI2:.4f} mol")
print(f"  HI: {nHI:.4f} mol")

# Qrafik
x_vals = np.linspace(0, 0.99, 200)
plt.figure(figsize=(8, 5))
plt.plot(x_vals, a - x_vals, label='H2', color='blue')
plt.plot(x_vals, b - x_vals, label='I2', linestyle='--', color='green')
plt.plot(x_vals, 2 * x_vals, label='HI', color='red')

plt.axvline(x=n, color='black', linestyle=':', label=f'Denge (x ≈ {n:.2f})')
plt.xlabel('(x)')
plt.ylabel(' (mol)')
plt.title('Chemical Equilibrium (H2 + I2 <=> 2 HI)')
plt.legend()
plt.grid(True)
plt.savefig('equilibrium.png')
plt.close()