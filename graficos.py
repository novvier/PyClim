import matplotlib.pyplot as plt
import numpy as np

na = np.linspace(0, 365, 366)
delta = -23.45 * np.cos(360.0 * na * np.pi / (365.0 * 180.0))
plt.plot(na, delta)
plt.grid(True)
plt.xlabel("Nro. de días")
plt.ylabel("Declinación")