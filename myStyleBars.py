from style import pastelBars as pb
from matplotlib import pyplot as plt
import numpy as np

with plt.style.context(pb.pastel(True)):
    val = np.array([20, 30, 10, 50])
    labels = ['Python', 'C#', 'Java', 'SQL']
    colors = ["C0", "C1", "C2", "C3", "C4"]
    plt.bar(labels, val, color = colors)
    for i in range(len(labels)):
        plt.text(i,val[i]*0.75, s = str(val[i]), ha = 'center')
    
    plt.show()
