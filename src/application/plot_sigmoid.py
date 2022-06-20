import matplotlib.pyplot as plt
import numpy as np
import math


def sigmoid(x):
    a = []
    for item in x:
        a.append(1 / (1 + math.exp(-item)))
    return a


x = np.arange(-10, 10, 0.2)
y = 1 / (1 + np.exp(-x))
plt.figure(figsize=[10, 8])
plt.axhline(y=0.5, color="black", linestyle="--", linewidth=3.5)
plt.xlabel("x", fontsize=25)
plt.ylabel("y", fontsize=25)
plt.plot(x, y, label=r"$\mathrm{sigm}(x) = \frac{e^x}{1+e^x}$", linewidth=3.5)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(fontsize=25)
plt.savefig("../../figs/sigma.pdf")
plt.show()
