import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

t = np.linspace(0,2,200)
y = np.sin((np.pi*2)*t)
plt.plot(t,y)
plt.title('sin(2πt)')
plt.show()