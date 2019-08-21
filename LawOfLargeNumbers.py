import math
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

n = 10000
m = 0
l = []

for i in range(n):
    x=randn()
    if (x > -1) and (x <= 1):
        m = m + 1
    l.append(m/(i+1))

print(l)

plt.scatter(range(n),l)
plt.show()