import matplotlib.pyplot as plt


x = [100, 300, 400, 500, 600]
y = [100, 200, 300, 400, 500]

# 1. Define the plot and assign the label
plt.scatter(x, y, color='red', marker='o', s=100, label='Scatter Plot', alpha = 0.5) # s = size of the marker # alpha = transparency of the marke

# 2. TRIGGER THE LABEL TO DISPLAY
plt.legend() 

# 3. Render the chart
plt.show()