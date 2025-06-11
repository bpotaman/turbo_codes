import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

n_bins = 20

dist1 = np.array([np.random.uniform(0, 1) for i in range(10000)])

fig, axs = plt.subplots(1)

# We can set the number of bins with the *bins* keyword argument.
axs.hist(dist1, bins=n_bins)
plt.show()