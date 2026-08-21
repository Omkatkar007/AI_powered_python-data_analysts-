import matplotlib.pyplot as plt

#  line plot 

x = [1, 6, 12, 44, 50]
y = [10, 20, 30, 40, 50]

plt.plot(x,y, color='green', linestyle='dashed', marker='o', markerfacecolor='blue', 
         linewidth=3, label='Line Plot')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line Plot')


# style

plt.style.use('ggplot')


plt.show()