import matplotlib.pyplot as plt
import random

import numpy as np


x = [i for i in range(0,100)]
# y = np.arange(100)
y = random.sample(range(1, 500), 100)

# print(y)
plt.plot(x,y)
plt.savefig('line.png')
# plt.show()