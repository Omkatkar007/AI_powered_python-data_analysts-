import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 30, 40, 50]



plt.bar(categories, values, color='blue', alpha=0.7) # alpha = transparency of the bar
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()