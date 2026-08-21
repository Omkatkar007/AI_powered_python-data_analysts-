import matplotlib.pyplot as plt
import numpy as np

#  histogram

data = np.random.randn(1000)
plt.hist(data, bins=20, edgecolor='black', color='blue', alpha=0.7) # bins = number of bins
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Histogram')        
plt.show()