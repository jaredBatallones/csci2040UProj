# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 11:28:57 2025

@author: nothi
"""

import numpy as np
import matplotlib.pyplot as plt

# Actual data for days 0 to 11
days_actual = np.arange(7)
actual_remaining = [60, 52, 47, 41, 35, 25, 14]
plt.figure(figsize=(12, 8))

# 1) Plot actual data as blue bars (for days 0 to 11)
plt.bar(days_actual, actual_remaining, color='blue', label='Actual (Bars)')

# 2) Compute best-fit (trend) line using the actual data
coeffs = np.polyfit(days_actual, actual_remaining, 1)
slope, intercept = coeffs

# Create an extended x-axis for 14 days (0 to 13)
x_extended = np.arange(8)
trend = np.poly1d(coeffs)
trend_vals = trend(x_extended)
plt.plot(x_extended, trend_vals, color='red', label='Trend (Best Fit)')

# Compute the x-intercept (predicted finish day)
x_intercept = -intercept / slope

# 3) Plot ideal line (green) for only 10 points (days 0 to 9), 7 hrs/day burn from 69
ideal_days = np.arange(8)
ideal_remaining = []
remaining = 60
for d in ideal_days:
    ideal_remaining.append(max(remaining, 0))
    remaining -= 9
plt.plot(ideal_days, ideal_remaining, color='green', marker='o', label='Ideal (9 hrs/day)')

# Optional: Draw a vertical dashed line at the predicted finish day (x-intercept)
plt.axvline(x=x_intercept, color='purple', linestyle='--', label=f'Predicted Finish (Day {x_intercept:.2f})')

# Print the slope, intercept, and x-intercept (predicted finish day)
print(f"Slope: {slope:.3f}")
print(f"Intercept: {intercept:.3f}")
print(f"Best-Fit Line: y = {slope:.3f}x + {intercept:.3f}")
print(f"Predicted completion day (x-intercept): {x_intercept:.2f}")

# Label and show plot
plt.title('Burndown with Actual, Best-Fit, and Ideal')
plt.xlabel('Day')
plt.ylabel('Hours Remaining')
plt.xticks(np.arange(9))  # Show ticks for days 0 to 13
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.show()