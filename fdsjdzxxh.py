import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

t = np.linspace(-2,2,200)
y = (np.exp(-0.6*t))*(np.sin((np.pi*2)*t))
plt.plot(t,y)
plt.title('exp(-0.6*t)*sin(2πt)')
plt.show()