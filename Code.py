import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

#Plot for U
mean = 0
standard_deviation = 1/4

x_values = np.arange(-3, 3, 0.1)
y_values = scipy.stats.norm(mean, standard_deviation)
plt.title('Random variable U')
plt.plot(x_values, y_values.pdf(x_values))

#Plot for V
mean = 0
standard_deviation = 1/9

x_values = np.arange(-3, 3, 0.1)
y_values = scipy.stats.norm(mean, standard_deviation)
plt.title('Random variable V')
plt.plot(x_values, y_values.pdf(x_values))

mean = 0
standard_deviation = 2

x_values = np.arange(-5, 5, 0.1)
y_values = scipy.stats.norm(mean, standard_deviation)
plt.title('Random variable Y')
plt.plot(x_values, y_values.pdf(x_values))
