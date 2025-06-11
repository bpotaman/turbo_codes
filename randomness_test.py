import matplotlib.pyplot as plt
import numpy as np

n_bins = 20

dist1 = np.array([np.random.uniform(0, 1) for i in range(10000000)])

fig, axs = plt.subplots(1)

axs.hist(dist1, bins=n_bins)
plt.show()