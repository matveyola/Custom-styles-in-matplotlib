import matplotlib.pyplot as plt
import numpy as np

plt.style.use('pastel.mplstyle')

# x = np.arange(0,20,0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.xlabel('Number')
# plt.ylabel('Function')
# plt.show()

val = np.array([20, 30, 10, 50])
labels = ['Python', 'C#', 'Java', 'SQL']
colors = ["C0", "C1", "C2", "C3", "C4"]
plt.bar(labels, val, color = colors)
plt.show()