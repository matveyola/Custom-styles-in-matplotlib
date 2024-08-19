import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np 
from matplotlib import cycler

# Defining main colors
colors = cycler('color', ["#FDABAB", "#FFD7A6", "#F7FAB2", "#C6F8BD", 
                            "#95F1FA", "#9BBFF8", "#FAC1FA"])
# Defining how the backround will look with .rcParams
mpl.rcParams['xtick.color'] = 'gray' 
mpl.rcParams['xtick.direction'] = 'out'
plt.rcParams['lines.linewidth'] = 2 
# You can use either mpl or plt when calling these functions
# Defining how the backround will look with .rc
plt.rc('axes', facecolor="#E4EAF2", edgecolor='none',
    axisbelow=True, grid=True, prop_cycle=colors)
plt.rc('grid', color='w', linestyle='solid')
plt.rc('ytick', direction='out', color='gray')

# Plotting the graphics
x = np.arange(0,20,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel('Number')
plt.ylabel('Function')
plt.show()