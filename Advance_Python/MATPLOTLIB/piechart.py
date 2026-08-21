import matplotlib.pyplot as plt
import numpy as np

#  piechart

lables = ['x', 'xxl', 'xl', 'l', 'm', 's']
sizes = [100, 200, 300, 400, 500, 600]
plt.pie(sizes, labels=lables, autopct='%1.1f%%', shadow=True, startangle=90) # autopct = automatic percentage
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Pie Chart')
plt.show()  