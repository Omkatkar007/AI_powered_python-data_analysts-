import matplotlib.pyplot as plt
import numpy as np

#  histogram

data = np.random.randn(1000)
plt.boxplot(data) # bins = number of bins
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Box Plot')
plt.show()