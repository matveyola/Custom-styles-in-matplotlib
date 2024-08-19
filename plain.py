import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,20,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel('Number')
plt.ylabel('Function')
plt.show()