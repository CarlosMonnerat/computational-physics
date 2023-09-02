import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, 0.5)
y = np.arange(-np.pi, np.pi, 0.5)
# Plano Bidimensional
x, y = np.meshgrid(x, y)
f_xy = np.sqrt(x ** 2 + y ** 2)
# Plano Tridimensional
z = np.cos(f_xy)
fig, ax = plt.subplots(subplot_kw = {"projection":'3d'})
ax.plot_surface(x, y, z, cmap='cool') # Plotagem da superfície 3D
plt.show()
