import matplotlib.pyplot as plt
import numpy as np

# saving plot

days = np.arange(1, 11)
sales = np.array([100, 150, 68, 250, 300, 350, 400, 200, 500, 550])

plt.figure(figsize=(10, 5))
plt.plot(days, sales, 'bo-')
plt.xlabel('Days')
plt.ylabel('Sales')
plt.title('Sales vs Days')
plt.grid(True)
plt.savefig('sales_vs_days.png')
plt.show()