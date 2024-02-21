#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:28:46 2024

@author: jamesmiller
"""

import numpy as np
import matplotlib.pyplot as plt

# Define time range for plots
timeRange = np.linspace(0, 10, 100)

# Homogeneous solutions are zero since initial conditions are y(0) = y'(0) = 0
homogeneousSolutionFirst = np.zeros(len(timeRange))
homogeneousSolutionSecond = np.zeros(len(timeRange))

# Define the Green's functions for the ODEs
def greensFunctionFirst(t, tau):
    return np.heaviside(t - tau, 1) * np.sin(2 * (t - tau))

def greensFunctionSecond(t, tau):
    return np.heaviside(t - tau, 1) * np.sin(t - tau)

# Define time range for the Green's function and solution calculation
solutionTimeRange = np.linspace(0, 10, 200)
timeStep = solutionTimeRange[1] - solutionTimeRange[0]  # Time step for numerical integration

# Initialize arrays to hold the particular solutions
solutionFirst = np.zeros(len(solutionTimeRange))
solutionSecond = np.zeros(len(solutionTimeRange))

# Compute the particular solution for each ODE by integrating the Green's function
for index, currentTime in enumerate(solutionTimeRange):
    tauValues = np.linspace(0, currentTime, 100)
    for tau in tauValues:
        solutionFirst[index] += greensFunctionFirst(currentTime, tau) * 1 * timeStep  # Assuming source term = 1
        solutionSecond[index] += greensFunctionSecond(currentTime, tau) * 4 * timeStep  # Assuming source term = 4

# Plotting all results
plt.figure(figsize=(18, 6))

# Plot for homogeneous solutions
plt.subplot(1, 4, 1)
plt.plot(timeRange, homogeneousSolutionFirst, label="Homogeneous: y'' + 4y = 0")
plt.title("Homogeneous Solution: y'' + 4y = 0")
plt.xlabel('Time')
plt.ylabel('y')
plt.legend()

plt.subplot(1, 4, 2)
plt.plot(timeRange, homogeneousSolutionSecond, label="Homogeneous: y'' + y = 0")
plt.title("Homogeneous Solution: y'' + y = 0")
plt.xlabel('Time')
plt.ylabel('y')
plt.legend()

# Plot for Green's function solutions
plt.subplot(1, 4, 3)
plt.plot(solutionTimeRange, solutionFirst, label="Green's Function Solution: y'' + 4y = x")
plt.title("Green's Function Solution: y'' + 4y = x")
plt.xlabel('Time')
plt.ylabel('y')
plt.legend()

plt.subplot(1, 4, 4)
plt.plot(solutionTimeRange, solutionSecond, label="Green's Function Solution: y'' + y = 4")
plt.title("Green's Function Solution: y'' + y = 4")
plt.xlabel('Time')
plt.ylabel('y')
plt.legend()

plt.tight_layout()
plt.show()
