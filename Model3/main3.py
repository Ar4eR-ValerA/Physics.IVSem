import math
import cmath
import matplotlib.pyplot as plt
import numpy as np

'''
1
0
0.001
1e-10
1.
0.001
0.1
'''

c0_1 = math.sqrt(float(input("c0_1: ")))
c0_2 = math.sqrt(float(input("c0_2: ")))
dt = float(input("dt: "))
omega = float(input("omega: "))
omega_r = float(input("omega_r: "))
omega_0 = float(input("omega_0: "))
gamma = float(input("gamma: "))


def itereration(t: float, c_1: complex, c_2: complex):
    dc_1 = (-omega_r * cmath.exp(1j * omega * t) * c_2) / 1j
    dc_2 = (-omega_r * cmath.exp(1j * omega * t) * c_1 + ((omega_0 - 1j * gamma / 2.) * c_2)) / 1j

    c_1 = c_1 + dc_1 * dt
    c_2 = c_2 + dc_2 * dt

    prob1 = (c_1 * complex.conjugate(c_1)).real
    prob2 = (c_2 * complex.conjugate(c_2)).real

    return c_1, c_2, prob1, prob2


def run(n: int):
    c_1 = c0_1
    c_2 = c0_2
    t = 0.
    prob_list_1 = []
    prob_list_2 = []
    t_list = []
    while t < n:
        c_1, c_2, prob_1, prob_2 = itereration(t, c_1, c_2)
        t_list.append(t)
        prob_list_1.append(prob_1)
        prob_list_2.append(prob_2)
        t += dt
    plt.title("Probability")
    plt.plot(t_list, prob_list_1)
    plt.plot(t_list, prob_list_2)
    plt.legend(["Probability on zero level", "Probability on first level"], loc="upper right")
    plt.plot(t_list, np.zeros(len(t_list)))
    plt.show()


run(100)
